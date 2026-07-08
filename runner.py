import re
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


class Response:

    def __init__(self, output):
        self.final_output = output


class Runner:

    @staticmethod
    def run_sync(agent, query):

        # Weather Agent
        if agent.name == "Weather Agent":

            location = "London"

            match = re.search(r"in\s+([A-Za-z ]+)", query)

            if match:
                location = match.group(1)

            weather = agent.tools[0](location)

            prompt = f"""
{agent.instructions}

Weather Data

{weather}

Answer the user.
"""

        # SQL Agent
        elif agent.name == "SQL Agent":
            
            # Step 1: Request the model to write the SQLite query
            sql_prompt = f"""
You are a translation assistant. Convert the user's natural language request into a valid SQLite query.
Do not explain anything. Return ONLY the raw SQL query.

Database Schema:
Table: `employees`
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT NOT NULL)
- `department` (TEXT NOT NULL)
- `salary` (REAL)
- `hire_date` (TEXT)

User Request: {query}
SQL Query:
"""
            sql_response = client.chat.completions.create(
                model=agent.model,
                messages=[
                    {
                        "role": "system",
                        "content": sql_prompt
                    }
                ]
            )
            
            raw_sql = sql_response.choices[0].message.content.strip()
            
            # Clean up the output in case the LLM returned markdown code blocks
            clean_sql = re.sub(r"```sql\s*", "", raw_sql)
            clean_sql = re.sub(r"```\s*", "", clean_sql)
            clean_sql = clean_sql.strip()
            
            print(f"\n[SQL Agent] Generated SQL Query: {clean_sql}")
            
            # Step 2: Run the query against the SQLite database using our tool
            query_result = agent.tools[0](clean_sql)
            
            print(f"[SQL Agent] Execution Result:\n{query_result}\n")
            
            # Step 3: Call the model with the result to generate the final response
            prompt = f"""
{agent.instructions}

User Query: {query}
Generated SQL Query: {clean_sql}
SQL Execution Result:
{query_result}

Please explain the SQL execution results to answer the user's query.
"""

        else:

            prompt = f"""
{agent.instructions}

Question

{query}
"""

        response = client.chat.completions.create(

            model=agent.model,

            messages=[
                {
                    "role": "system",
                    "content": prompt
                }
            ]
        )

        return Response(
            response.choices[0].message.content
        )

import os
import sqlite3
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_current_weather(location: str):
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": WEATHER_API_KEY,
        "q": location
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    return {
        "location": data["location"]["name"],
        "temperature": current["temp_c"],
        "condition": current["condition"]["text"],
        "humidity": current["humidity"],
        "wind": current["wind_kph"]
    }


def execute_sql_query(sql_query: str) -> str:
    """Executes a SQL query against the local SQLite database and returns the results as a string."""
    db_path = "company.db"
    
    # Connect and initialize database/tables if they do not exist
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create the employees table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL,
        hire_date TEXT
    )
    """)
    
    # Populate the table with sample data if it is empty
    cursor.execute("SELECT COUNT(*) FROM employees")
    if cursor.fetchone()[0] == 0:
        employees = [
            ("Alice Smith", "HR", 60000, "2022-01-15"),
            ("Bob Jones", "Engineering", 85000, "2021-06-20"),
            ("Charlie Brown", "Engineering", 90000, "2020-03-10"),
            ("Diana Prince", "Marketing", 70000, "2023-02-01"),
            ("Evan Wright", "Sales", 65000, "2022-11-15")
        ]
        cursor.executemany(
            "INSERT INTO employees (name, department, salary, hire_date) VALUES (?, ?, ?, ?)",
            employees
        )
        conn.commit()
    
    try:
        cursor.execute(sql_query)
        if cursor.description is None:
            conn.commit()
            conn.close()
            return "Query executed successfully, no rows returned."
            
        columns = [description[0] for description in cursor.description]
        rows = cursor.fetchall()
        conn.close()
        
        if not rows:
            return "No results found."
            
        # Format results as a readable table-like string
        result_str = f"Columns: {', '.join(columns)}\n"
        for row in rows:
            result_str += f"{row}\n"
        return result_str
        
    except Exception as e:
        conn.close()
        return f"Error executing query: {str(e)}"

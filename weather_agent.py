from agent import Agent
from tool import get_current_weather

weather_agent = Agent(
    name="Weather Agent",
    instructions="""
You are an expert Weather  assistant.

Answer ONLY weather-related questions.

Always use the weather tool.
""",
    tools=[get_current_weather],
)

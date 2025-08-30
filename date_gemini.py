from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from typing_extensions import TypedDict
import datetime
import os

# api_key = os.getenv("GEMINI_KEY")
provider = GoogleProvider()


# provider = GoogleProvider(api_key=""YOUR_API_KEY"")
model = GoogleModel("gemini-2.0-flash", provider=provider)
agent = Agent(model)


class DateResponse(TypedDict):
    day: int
    month: str
    year: int
    hour: int
    minutes: int
    seconds: int


@agent.tool_plain
def get_current_datetime() -> str:
    """Returns the current date and time in Year-Month-Day Hours:Minutes:Seconds format."""
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"The current date and time is: {current_datetime}")
    return current_datetime


# 3. Run the agent with a simple query
result = agent.run_sync("What is todays date and time?", output_type=DateResponse)

# 4. Print the result
print(result.output)
print(result)

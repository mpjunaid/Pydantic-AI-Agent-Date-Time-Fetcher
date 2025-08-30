from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider
import datetime

from typing_extensions import TypedDict

# 1. Define the Ollama model

ollama_model2 = OpenAIChatModel(
    model_name="llama3.1:latest",
    provider=OllamaProvider(base_url="http://localhost:11434/v1"),
)

# 2. Instantiate the Pydantic AI agent with the model
agent = Agent(ollama_model2)


class DateResponse(TypedDict):
    day: int
    month: str
    year: int


@agent.tool_plain
def get_current_date() -> str:
    """Returns the current date in YYYY-MM-DD format."""
    todays_date = datetime.date.today().strftime("%Y-%m-%d")
    print(f"Today's date is: {todays_date}")
    return todays_date


# 3. Run the agent with a simple query
result = agent.run_sync("What is todays date?", output_type=DateResponse)

# 4. Print the result
print(result.output)
print(result)

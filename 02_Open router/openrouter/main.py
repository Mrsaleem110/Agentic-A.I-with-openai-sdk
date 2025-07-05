import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# Load API key from .env
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "google/gemini-2.0-flash-exp:free"

# Disable tracing
set_tracing_disabled(disabled=True)

# Async main function
async def main():
    client = AsyncOpenAI(api_key=OPENROUTER_API_KEY, base_url=BASE_URL)

    agent = Agent(
        name="My Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(agent, "Tell me about Agentic A.I .")
    print("\n🧠 AI Response:\n")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
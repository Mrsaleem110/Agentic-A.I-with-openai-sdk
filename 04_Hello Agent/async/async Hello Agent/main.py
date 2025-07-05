import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio

load_dotenv()

gemini_key=os.getenv("Gemini_key")

if not gemini_key:
    raise ValueError ("Key Not Founded")

client=AsyncOpenAI(
    api_key = gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model=OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=client,

)
config=RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

async def main():
    agent=Agent(
        name="Assistant",
        instructions='You Are helpful agent',
        model=model
    )
    result = await Runner.run(agent,"Tell me about recursion in programming." ,run_config=config)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
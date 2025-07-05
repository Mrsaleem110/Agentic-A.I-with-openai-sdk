import os
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI
from agents.run import RunConfig

load_dotenv()

gemini_key=os.getenv("Gemini_key")

if not gemini_key:
    raise ValueError ("Key not Founded!")

client=AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)    
model = OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
    openai_client=client,
)
config=RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)
agent=Agent(
    name="Assistant",
    instructions='You are helpful agent',
    model=model
)
result = Runner.run_sync(agent,"Hello! how r u?",run_config=config)
print(result.final_output)
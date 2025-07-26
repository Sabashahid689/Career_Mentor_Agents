# main.py
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from roadmap_tool import get_career_roadmap

load_dotenv()
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(model= "gemini-2.0-flash" , openai_client=client)
config = RunConfig(model=model,  tracing_disabled=True)

career_agent = Agent(
    name="CareerAgent",
    instructions="you ask about interests and suggest a  career field.",
    model=model
)
skill_agent = Agent(
    name="SkillAgent",
    instructions="You share the roadmap using the get_career_roadmap tool.",
    model=model,
    tools=[get_career_roadmap]
)
job_agent = Agent(
    name="JobAgent",
    instructions="You suggest job titles in the chosen career.",
    model=model
)

def main():
    print("/0001F393 Career Mentor Agent/n")
    interest = input("What are your interests? ")

    result1 = Runner.run_sync(career_agent, interest, run_config=config)
    field = result1.final_output.strip()
    print("/n Sugguested Career: , field")

    result2 = Runner.run_sync(skill_agent, field, run_config=config)
    print("/n Required Skills:", result2.final_output)

    result3 = Runner.run_sync(job_agent, field, run_config=config)
    print("/n possible Jobs:", result3.final_output)

if __name__ == "__main__":
    main()
from crewai import Agent
from utils.llm import get_llm

messaging_agent = Agent(
    role="Outreach Specialist",
    goal="Write a short professional cover letter (max 150-200 words)",
    backstory="Networking expert",
    llm=get_llm(),
    verbose=True
)
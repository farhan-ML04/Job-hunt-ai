from crewai import Agent
from utils.llm import get_llm

resume_agent = Agent(
    role="Resume Writer",
    goal="Create a concise ATS-friendly resume (max 1 page). No extra explanation.",
    backstory="ATS expert",
    llm=get_llm(),
    verbose=True
)
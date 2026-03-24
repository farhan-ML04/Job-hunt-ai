from crewai import Agent
from utils.llm import get_llm

jd_analyst = Agent(
    role="Job Analyst",
    goal="Extract ONLY top 8-10 key skills in bullet points. Keep output short and clean.",
    backstory="Expert HR",
    llm=get_llm(),
    verbose=True
)
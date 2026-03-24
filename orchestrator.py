from crewai import Crew
from agents.jd_agent import jd_analyst
from agents.resume_cl_agent import resume_agent
from agents.messaging_agent import messaging_agent
from agents.tasks import jd_task, resume_task, cover_letter_task
from utils.llm import get_llm

def run_pipeline(jd, resume):

    # Step 1: JD Analysis
    task1 = jd_task(jd_analyst, jd)

    # Step 2: Resume Improvement
    task2 = resume_task(resume_agent, resume, "Extracted skills from JD")

    # Step 3: Cover Letter
    task3 = cover_letter_task(messaging_agent, resume, jd)

    crew = Crew(
        agents=[jd_analyst, resume_agent, messaging_agent],
        tasks=[task1, task2, task3],
        llm=get_llm(),
        verbose=True
    )

    result = crew.kickoff()
    outputs = result.tasks_output

    return {
    "jd_analysis": outputs[0].raw,
    "resume": outputs[1].raw,
    "cover_letter": outputs[2].raw
}
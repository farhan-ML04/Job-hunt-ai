from crewai import Task

def jd_task(agent, jd):
    return Task(
        description=f"Analyze this job description and extract key skills:\n{jd}",
        agent=agent,
        expected_output="List of key skills, tools, and requirements"
    )


def resume_task(agent, resume, jd_analysis):
    return Task(
        description=f"""
Improve this resume:

{resume}

Based on this job analysis:
{jd_analysis}
""",
        agent=agent,
        expected_output="Improved ATS-friendly resume"
    )


def cover_letter_task(agent, resume, jd):
    return Task(
        description=f"""
Write a professional cover letter using:

Resume:
{resume}

Job Description:
{jd}
""",
        agent=agent,
        expected_output="A strong personalized cover letter"
    )
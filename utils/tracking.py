import os
from datetime import datetime

def save_cover_letter(content):
    os.makedirs("data/cover_letters", exist_ok=True)

    filename = f"data/cover_letters/cover_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write(content)

    return filename


def log_application(job_title, company, summary):
    file_path = "data/applications_log.csv"

    with open(file_path, "a") as f:
        f.write(f"{job_title},{company},{summary}\n")
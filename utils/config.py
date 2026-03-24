import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
USAJOBS_API_KEY = os.getenv("USAJOBS_API_KEY")
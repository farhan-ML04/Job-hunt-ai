import requests
from utils.config import USAJOBS_API_KEY

def fetch_jobs(keyword):
    url = "https://data.usajobs.gov/api/search"

    headers = {
        "Authorization-Key": USAJOBS_API_KEY,
        "User-Agent": "your_email@example.com"
    }

    params = {
        "Keyword": keyword,
        "ResultsPerPage": 5
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()
    jobs = []

    try:
        for item in data["SearchResult"]["SearchResultItems"]:
            job = item["MatchedObjectDescriptor"]
            jobs.append({
                "title": job["PositionTitle"],
                "company": job["OrganizationName"],
                "description": job["UserArea"]["Details"]["JobSummary"]
            })
    except:
        pass

    return jobs
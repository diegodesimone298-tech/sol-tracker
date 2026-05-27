from fastmcp import FastMCP

mcp = FastMCP("Job Search")

MOCK_JOBS = [
    {"title": "Software Engineer", "company": "Acme Corp", "location": "San Francisco, CA", "salary": "$120,000 - $160,000"},
    {"title": "Backend Developer", "company": "Globex", "location": "Austin, TX", "salary": "$100,000 - $140,000"},
    {"title": "Frontend Engineer", "company": "Initech", "location": "New York, NY", "salary": "$110,000 - $150,000"},
    {"title": "Data Engineer", "company": "Umbrella Inc", "location": "Seattle, WA", "salary": "$130,000 - $170,000"},
    {"title": "DevOps Engineer", "company": "Hooli", "location": "Remote", "salary": "$115,000 - $155,000"},
    {"title": "ML Engineer", "company": "Pied Piper", "location": "San Francisco, CA", "salary": "$140,000 - $180,000"},
]


@mcp.tool()
def search_jobs(query: str, location: str) -> list[dict]:
    """Search for jobs matching a query and location."""
    query_lower = query.lower()
    location_lower = location.lower()

    results = [
        job for job in MOCK_JOBS
        if query_lower in job["title"].lower()
        or (location_lower and location_lower in job["location"].lower())
    ]

    return results or MOCK_JOBS[:3]


if __name__ == "__main__":
    mcp.run()

# Job Search MCP Server

A minimal MCP server exposing a `search_jobs` tool with mock data.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python server.py
```

Runs over stdio by default (standard MCP transport).

## Tool

### `search_jobs(query, location)`

Returns a list of jobs matching the query or location.

**Response fields:** `title`, `company`, `location`, `salary`

**Example response:**
```json
[
  {
    "title": "Software Engineer",
    "company": "Acme Corp",
    "location": "San Francisco, CA",
    "salary": "$120,000 - $160,000"
  }
]
```

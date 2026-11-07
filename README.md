# Application Reliability Monitoring System

A Python-based application monitoring tool designed to detect service availability issues, measure response times, track incidents, and record recovery events.

## Project Overview

This project simulates a basic Site Reliability Engineering (SRE) monitoring workflow.

It continuously checks an application's health endpoint, identifies service disruptions, tracks incident duration, and records recovery information.

## Key Features

- HTTP health checks
- Application response time measurement
- Automatic incident detection
- Incident lifecycle tracking
- Downtime calculation
- Incident history stored in JSON
- Logging of monitoring events
- Automated tests using Pytest

## Technologies

- Python
- Flask
- Requests
- Pytest
- Git

## Project Structure

application-reliability-monitor/
- app/
  - main.py
- monitoring/
  - health_check.py
  - test_health_check.py
- logs/
  - health_check.log
  - incidents.json
- docs/
- requirements.txt
- .gitignore
- README.md

## How It Works

1. The Flask application exposes a `/health` endpoint.
2. The monitoring script sends HTTP requests every 5 seconds.
3. The script measures response times.
4. If the application becomes unavailable, an incident is recorded.
5. When the application recovers, downtime is calculated.
6. Incident information is saved for future analysis.

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd application-reliability-monitor
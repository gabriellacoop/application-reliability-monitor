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
- Prometheus
- Grafana
- Docker
- Docker Compose
- Git

## Project Structure

application-reliability-monitor/
- app/
  - main.py
- monitoring/
  - health_check.py
  - test_health_check.py
- prometheus/
  - prometheus.yml
- docs/
  - incident-response.md
- logs/ (generated at runtime)
- docker-compose.yml
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
git clone https://github.com/gabriellacoop/application-reliability-monitor.git
cd application-reliability-monitor
```

## Running Tests

The project includes automated tests using pytest and Flask's test client.

To run the test suite:

```bash
python -m pytest -v
```

The tests validate:

- Health check endpoint (`/health`)
- JSON response format
- Main application endpoint (`/`)
- Prometheus metrics endpoint (`/metrics`)

Tests run independently without requiring the Flask server to be running.
```
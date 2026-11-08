
# Application Reliability Monitoring System

A Python-based application monitoring system designed to monitor service availability, measure response times, detect incidents, track recovery events, and visualize application health metrics.

## Project Overview

This project simulates a Site Reliability Engineering (SRE) monitoring workflow.

It continuously monitors an application's health endpoint, detects service disruptions, tracks incident duration, and records recovery information.

Prometheus collects application metrics, while Grafana provides dashboards to visualize application health and monitoring data.

## Key Features

- HTTP health checks
- Application response time measurement
- Automatic incident detection
- Incident lifecycle tracking
- Downtime calculation
- Incident history stored in JSON
- Logging of monitoring events
- Prometheus metrics collection
- Grafana monitoring dashboard
- Docker-based monitoring infrastructure
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

## Architecture

The monitoring system consists of the following components:

1. Flask exposes application endpoints and Prometheus metrics.
2. The Python monitoring script checks application availability every 5 seconds.
3. Incident events and recovery information are recorded in JSON and log files.
4. Prometheus collects metrics from the application.
5. Grafana visualizes application health, response times, and availability.

## Project Structure

```text
application-reliability-monitor/
├── app/
│   ├── __init__.py
│   └── main.py
├── monitoring/
│   ├── health_check.py
│   └── test_health_check.py
├── prometheus/
│   └── prometheus.yml
├── docs/
│   └── incident-response.md
├── logs/
│   └── (generated at runtime)
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/gabriellacoop/application-reliability-monitor.git
cd application-reliability-monitor
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask application:

```bash
python app/main.py
```

The application runs at:

```text
http://127.0.0.1:5001
```

Health endpoint:

```text
http://127.0.0.1:5001/health
```

Prometheus metrics endpoint:

```text
http://127.0.0.1:5001/metrics
```

## Running the Monitoring Script

Open a separate terminal and execute:

```bash
python monitoring/health_check.py
```

The monitoring script checks application availability every 5 seconds and records incidents, response times, and recovery events.

## Prometheus and Grafana

Start the monitoring infrastructure using Docker Compose:

```bash
docker compose up -d
```

Prometheus:

```text
http://localhost:9090
```

Grafana:

```text
http://localhost:3000
```

The Grafana dashboard includes:

- Application Health
- Total Health Checks
- Response Time
- Prometheus Target Availability

Prometheus collects application metrics, while Grafana visualizes service health and availability.

The built-in Prometheus `up` metric is used to identify whether the application metrics endpoint is reachable.

To stop the Docker containers:

```bash
docker compose down
```

## Incident Simulation

The project supports basic incident simulation by stopping and restarting the Flask application.

When the application becomes unavailable:

- The monitoring script detects the failure.
- An incident is recorded.
- Prometheus identifies the unavailable target.
- Grafana displays the availability change.

When the application recovers:

- The incident is marked as resolved.
- Downtime is calculated.
- Recovery information is saved in the incident history.

## Running Tests

The project includes automated tests using Pytest and Flask's test client.

Run the test suite:

```bash
python -m pytest -v
```

The tests validate:

- Health check endpoint (`/health`)
- JSON response format
- Main application endpoint (`/`)
- Prometheus metrics endpoint (`/metrics`)

Tests run independently without requiring the Flask server to be running.

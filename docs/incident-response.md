# Incident Response Runbook

## 1. Purpose

This document describes the basic process for identifying, investigating, and resolving application availability incidents.

## 2. Incident Detection

The monitoring system checks the application health endpoint every 5 seconds.

An incident is detected when:
- The application cannot be reached.
- The health endpoint returns an unsuccessful HTTP response.

## 3. Initial Investigation

When an incident occurs:

1. Check the health monitoring output.
2. Review `logs/health_check.log`.
3. Identify whether the application is responding.
4. Check for connection errors or unsuccessful HTTP responses.

## 4. Incident Resolution

If the application is unavailable:

1. Verify that the Flask application is running.
2. Check whether the configured port is correct.
3. Restart the application if necessary.
4. Confirm that the health endpoint returns HTTP 200.

## 5. Recovery Verification

The incident is considered resolved when:

- The application responds successfully.
- The health endpoint reports `healthy`.
- The monitoring system detects recovery.
- Downtime is recorded.

## 6. Incident Records

Incident information is stored in:

`logs/incidents.json`

Records include:
- Incident ID
- Incident status
- Start timestamp
- Resolution timestamp
- Downtime duration

## 7. Future Improvements

- Automated notifications
- Incident severity classification
- Prometheus metrics
- Grafana dashboards
- Improved root cause analysis
import requests
import time
import logging
import json
from datetime import datetime

URL = "http://127.0.0.1:5001/health"

INCIDENT_FILE = "logs/incidents.json"
incident_counter = 0

logging.basicConfig(
    filename="logs/health_check.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def save_incident(incident):
    with open(INCIDENT_FILE, "a") as file:
        file.write(json.dumps(incident) + "\n")


# Tracks the current incident
incident_start = None
incident_start_monotonic = None
current_incident = None

while True:
    try:
        start_time = time.time()

        response = requests.get(URL, timeout=5)

        response_time = (time.time() - start_time) * 1000

        if response.status_code == 200:

            # Check if an incident was previously active
            if incident_start is not None:

                duration = time.monotonic() - incident_start_monotonic

                if current_incident is not None:
                    current_incident["status"] = "resolved"
                    current_incident["resolved_at"] = datetime.now().isoformat()
                    current_incident["downtime_seconds"] = round(duration, 2)

                    save_incident(current_incident)
                    current_incident = None

                recovery_message = (
                    f"INCIDENT RESOLVED | "
                    f"Downtime: {duration:.2f} seconds"
                )

                print(recovery_message)
                logging.info(recovery_message)

                incident_start = None
                incident_start_monotonic = None

            message = f"HEALTHY | Response time: {response_time:.2f} ms"

            print(message)
            logging.info(message)

        else:
            if incident_start is None:
                incident_start = datetime.now()
                incident_start_monotonic = time.monotonic()
                incident_counter += 1

                current_incident = {
                    "incident_id": f"INC-{incident_counter:03d}",
                    "status": "ongoing",
                    "started_at": incident_start.isoformat(),
                    "resolved_at": None,
                    "downtime_seconds": None
                }

                message = (
                    f"INCIDENT STARTED | "
                    f"HTTP status: {response.status_code}"
                )
            else:
                message = f"INCIDENT ONGOING | HTTP {response.status_code}"

            print(message)
            logging.warning(message)

    except requests.exceptions.RequestException as error:

        if incident_start is None:
            incident_start = datetime.now()
            incident_start_monotonic = time.monotonic()
            incident_counter += 1

            current_incident = {
                "incident_id": f"INC-{incident_counter:03d}",
                "status": "ongoing",
                "started_at": incident_start.isoformat(),
                "resolved_at": None,
                "downtime_seconds": None
            }

            message = f"INCIDENT STARTED | {error}"
        else:
            message = f"INCIDENT ONGOING | {error}"

        print(message)
        logging.error(message)

    time.sleep(5)
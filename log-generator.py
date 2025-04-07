import json
import time
import uuid
from datetime import datetime, timezone, timedelta
import random

log_levels = [
    {"severity_text": "INFO", "severity_number": 20},
    {"severity_text": "WARNING", "severity_number": 30},
    {"severity_text": "CRITICAL", "severity_number": 50}
]

scopes = ["robot_events", "robot_utils", "main", "utils"]
resources = ["API-Gateway", "Robot-Service", "Controller"]
bodies = [
    "Robot Event Updated to Service",
    "Sending robot event update payload to Robot service",
    "!!!! ERROR_ID= 6000 REDIS CONNECTION FAILED !!!!",
    "(\"name 'spanId' is not defined\",)",
    "Request: Processing Time : 12",
    "all_request table updated"
]

def current_timestamps():
    now = datetime.now(timezone(timedelta(hours=5, minutes=30)))
    epoch_nano = int(time.time() * 1e9)
    return {
        "observed_timestamp": str(epoch_nano),
        "observed_timestamp_rfc3339": now.isoformat(),
        "event_timestamp": str(epoch_nano + random.randint(1000, 10000))
    }

def generate_log():
    ts = current_timestamps()
    level = random.choice(log_levels)
    return {
        "observed_timestamp": ts["observed_timestamp"],
        "observed_timestamp_rfc3339": ts["observed_timestamp_rfc3339"],
        "instrumentation_scope": random.choice(scopes),
        "host_name": "4c0101bc0a9f",
        "severity_text": level["severity_text"],
        "severity_number": level["severity_number"],
        "event_timestamp": ts["event_timestamp"],
        "body": random.choice(bodies),
        "resource": random.choice(resources),
        "span_id": str(uuid.uuid4()),
        "trace_id": str(uuid.uuid4())
    }

log_file = "sample-logs/app.log"

while True:
    log = generate_log()
    with open(log_file, "a") as f:
        f.write(json.dumps(log) + "\n")
    time.sleep(2)  

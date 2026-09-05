from pprint import pprint
from app.collector.sample_events import events
from app.normalization.normalizer import normalize_event
from app.detection.engine import detect_failed_logins
print("Python SOC Monitor started")


normalized_events = []
for event in events:
    normalized_event = normalize_event(event)
    normalized_events.append(normalized_event)
    pprint(normalized_event)

result = detect_failed_logins(normalized_events)

if result["matched"]:
    print("ALERT: Multiple failed logins detected")
    print("Rule:", result["rule"])
    print("Severity:", result["severity"])
    print("Username:", result["username"])
    print("Failed login count:", result["failed_count"])
    print("Threshold:", result["threshold"])
    print("Time window:", result["time_window_seconds"], "seconds")

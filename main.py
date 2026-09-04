from app.collector.sample_events import events
from app.normalization.normalizer import normalize_event

print("Python SOC Monitor started")


failed_count = 0

for event in events:
    normalized_event = normalize_event(event)
    print(normalized_event)

    if normalized_event["event_type"] == "failed_login":
        failed_count = failed_count + 1

        if failed_count == 3:
           print("ALERT: Multiple failed logins detected")

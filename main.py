from app.collector.sample_events import events
from app.normalization.normalizer import normalize_event
from app.detection.engine import detect_failed_logins
print("Python SOC Monitor started")


normalized_events = []
for event in events:
    normalized_event = normalize_event(event)
    normalized_events.append(normalized_event)
    print(normalized_event)

if detect_failed_logins(normalized_events):
    print("ALERT: Multiple failed logins detected")
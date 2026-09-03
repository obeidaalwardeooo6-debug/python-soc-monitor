from app.collector.sample_events import events

print("Python SOC Monitor started")

failed_count = 0

for event in events:
    print(event)

    if event["event_type"] == "failed_login":
        failed_count = failed_count + 1

        if failed_count == 3:
           print("ALERT: Multiple failed logins detected")

def normalize_event(event):
    event_id = event.get("event_id", event.get("EventID"))

    if event.get("event_type") is not None:
        event_type = event.get("event_type")
    elif event_id == 4625:
        event_type = "failed_login"
    else:
        event_type = "unknown"





    normalized_event = {

    "timestamp": event.get("timestamp", event.get("TimeCreated")),
    "event_id": event_id,
    "event_type": event_type,
    "username": event.get("username", event.get("AccountName")),
    "source_ip": event.get("source_ip", event.get("IpAddress")),
    "host": event.get("host", event.get("Computer")),
    "source": event.get("source", "windows_security")
}

    if normalized_event["username"] is None:
     raise ValueError("Missing required field: username")

    if normalized_event["timestamp"] is None:
     raise ValueError("Missing required field: timestamp")

    if normalized_event["event_id"] is None:
     raise ValueError("Missing required field: event_id")

    if normalized_event["source_ip"] is None:
     raise ValueError("Missing required field: source_ip")

    if normalized_event["host"] is None:
     raise ValueError("Missing required field: host")


    return normalized_event
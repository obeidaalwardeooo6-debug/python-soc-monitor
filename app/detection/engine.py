from app.detection.rules import FAILED_LOGIN_THRESHOLD

def detect_failed_logins(events):
    failed_count = 0

    for event in events:
        if event["event_type"] == "failed_login":
            failed_count = failed_count + 1


    if failed_count >= FAILED_LOGIN_THRESHOLD:
        return True

    return False
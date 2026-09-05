from datetime import datetime
from pprint import pprint
from app.detection.rules import (
    FAILED_LOGIN_THRESHOLD,
    FAILED_LOGIN_RULE_NAME,
    FAILED_LOGIN_SEVERITY,
    FAILED_LOGIN_TIME_WINDOW_SECONDS
)

def detect_failed_logins(events):
    failed_count = 0
    failed_times = []
    failed_by_user = {}


    for event in events:
        if event["event_type"] == "failed_login":
            failed_count = failed_count + 1

            event_time = datetime.fromisoformat(event["timestamp"])
            failed_times.append(event_time)


            username = event["username"]


            if username not in failed_by_user:
               failed_by_user[username] = []

            failed_by_user[username].append(event_time)


    print("Failed by user:")
    pprint(failed_by_user)

    matched = False
    matched_username = None
    matched_count = 0

    for username, times in failed_by_user.items():
        times.sort()

        for i in range(len(times) - FAILED_LOGIN_THRESHOLD + 1):
            start_time = times[i]
            end_time = times[i + FAILED_LOGIN_THRESHOLD - 1]

            time_difference = (end_time - start_time).total_seconds()

            if time_difference <= FAILED_LOGIN_TIME_WINDOW_SECONDS:
                matched = True
                matched_username = username
                matched_count = len(times)
                break

        if matched:
            break

    if matched:
        return {
            "matched": True,
            "rule": FAILED_LOGIN_RULE_NAME,
            "severity": FAILED_LOGIN_SEVERITY,
            "username": matched_username,
            "failed_count": matched_count,
            "threshold": FAILED_LOGIN_THRESHOLD,
            "time_window_seconds": FAILED_LOGIN_TIME_WINDOW_SECONDS
        }

    return {
        "matched": False,
        "rule": FAILED_LOGIN_RULE_NAME,
        "severity": FAILED_LOGIN_SEVERITY,
        "username": None,
        "failed_count": matched_count,
        "threshold": FAILED_LOGIN_THRESHOLD,
        "time_window_seconds": FAILED_LOGIN_TIME_WINDOW_SECONDS
    }
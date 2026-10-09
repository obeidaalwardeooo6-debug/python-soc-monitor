from uuid import uuid4
ALERT_STATUSES = ("new", "investigating", "resolved")
ALERT_SEVERITIES = ("low", "medium", "high", "critical")


def create_alert(severity, rule_id, description, timestamp, source_ip, host):
    return {
        "status": "new",
        "severity": severity,
        "rule_id": rule_id,
        "description": description,
        "timestamp": timestamp,
        "source_ip": source_ip,
        "host": host,
        "id": str(uuid4())
    }

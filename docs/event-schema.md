# Event Schema

Every normalized security event in Python SOC Monitor should use the following standard fields:

- `timestamp` - When the event occurred
- `event_id` - The event identifier
- `event_type` - The normalized event type
- `username` - The user associated with the event
- `source_ip` - The source IP address
- `host` - The host where the event occurred
- `source` - The source of the security event
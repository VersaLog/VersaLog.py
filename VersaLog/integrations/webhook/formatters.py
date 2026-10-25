import datetime


def format_payload(level, message, format="generic"):
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    if format == "generic":
        return {
            "source": "VersaLog",
            "level": level,
            "message": message,
            "timestamp": timestamp,
        }
    if format == "discord":
        return {"content": f"[{level}] {message}"}
    if format == "slack":
        return {"text": f"[{level}] {message}"}
    raise ValueError("format must be 'generic', 'discord', or 'slack'")

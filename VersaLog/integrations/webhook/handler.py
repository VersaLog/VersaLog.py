from .formatters import format_payload
from .sender import send_json


LEVELS = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50,
}


class WebhookHandler:
    def __init__(self, url, level="ERROR", format="generic", timeout=3.0, headers=None):
        if not isinstance(url, str) or not url.strip():
            raise ValueError("url must be a non-empty string")
        normalized_level = str(level).upper()
        if normalized_level not in LEVELS:
            raise ValueError(
                "level must be one of: " + ", ".join(LEVELS.keys())
            )
        if format not in ("generic", "discord", "slack"):
            raise ValueError("format must be 'generic', 'discord', or 'slack'")
        if timeout <= 0:
            raise ValueError("timeout must be greater than 0")

        self.url = url
        self.level = normalized_level
        self.format = format
        self.timeout = timeout
        self.headers = dict(headers or {})
        self.last_success = None

    def should_handle(self, level):
        return LEVELS.get(str(level).upper(), 0) >= LEVELS[self.level]

    def emit(self, message, level):
        payload = format_payload(str(level).upper(), str(message), self.format)
        self.last_success = send_json(
            self.url, payload, timeout=self.timeout, headers=self.headers
        )
        return self.last_success

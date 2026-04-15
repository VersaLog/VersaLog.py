from .core import VersaLog
from .handler import VersaLogHandler
from .integrations.auto import auto_setup
from .integrations.fastapi import setup_fastapi_logging
from .integrations.flask import setup_flask_logging
from .integrations.django import setup_django_logging

__copyright__ = "Copyright 2025 by Kayu0514"
__version__ = "2.6.0"
__author__ = "Kayu0514"
__url__ = "https://github.com/kayu0514"

__all__ = ["VersaLog", "VersaLogHandler", "auto_setup", "setup_fastapi_logging","setup_flask_logging", "setup_django_logging"]
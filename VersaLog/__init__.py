from .core import VersaLog
from .handler import VersaLogHandler
from .integrations.fastapi import setup_fastapi_logging

__copyright__ = "Copyright 2025 by Kayu0514"
__version__ = "2.5.5"
__author__ = "Kayu0514"
__url__ = "https://github.com/kayu0514"

__all__ = ["VersaLog", "VersaLogHandler", "setup_fastapi_logging"]
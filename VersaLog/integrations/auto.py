import sys

from .generic import setup_logging
from .fastapi import setup_fastapi_logging
from .flask import setup_flask_logging
from .django import setup_django_logging


def auto_setup(versalog):
    """
    Automatically detects the runtime environment
    and applies the appropriate logging configuration.
    """

    if "uvicorn" in sys.modules:
        setup_fastapi_logging(versalog)
        return "fastapi"

    if "gunicorn" in sys.modules:
        setup_fastapi_logging(versalog)
        return "gunicorn"

    if "flask" in sys.modules:
        setup_flask_logging(None, versalog)
        return "flask"

    if "django" in sys.modules:
        setup_django_logging(versalog)
        return "django"

    setup_logging(versalog)
    return "generic"
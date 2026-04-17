import logging
from ..handler import VersaLogHandle


def setup_django_logging(versalog):
    handler = VersaLogHandler(versalog)

    root = logging.getLogger()
    for h in root.handlers[:]:
        root.removeHandler(h)
    root.setLevel(logging.NOTSET)
    root.addHandler(handler)

    for name in ["django", "django.request", "django.server", "django.db.backends"]:
        logger = logging.getLogger(name)
        for h in logger.handlers[:]:
            logger.removeHandler(h)
        logger.propagate = True
        logger.setLevel(logging.NOTSET)
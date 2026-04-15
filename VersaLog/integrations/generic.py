import logging
from ..handler import VersaLogHandler


def setup_logging(versalog):
    handler = VersaLogHandler(versalog)

    root = logging.getLogger()

    for h in root.handlers[:]:
        root.removeHandler(h)

    root.setLevel(logging.NOTSET)
    root.addHandler(handler)
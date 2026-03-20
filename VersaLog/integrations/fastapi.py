import logging
from ..handler import VersaLogHandler


def setup_fastapi_logging(versalog):
    handler = VersaLogHandler(versalog)

    handler.setFormatter(
        logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")
    )

    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(logging.DEBUG)

    for name in ["uvicorn", "uvicorn.error", "uvicorn.access"]:
        logger = logging.getLogger(name)
        logger.handlers.clear()
        logger.propagate = True
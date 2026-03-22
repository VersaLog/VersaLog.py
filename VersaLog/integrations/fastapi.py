import logging
from ..handler import VersaLogHandler


def setup_fastapi_logging(versalog):
    handler = VersaLogHandler(versalog)

    handler.setFormatter(
        logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")
    )

    root = logging.getLogger()

    for h in root.handlers[:]:
        root.removeHandler(h)

    root.setLevel(logging.NOTSET)
    root.addHandler(handler)

    for name in [
        "uvicorn",
        "uvicorn.error",
        "uvicorn.access",
        "asyncio"
    ]:
        logger = logging.getLogger(name)

        for h in logger.handlers[:]:
            logger.removeHandler(h)

        logger.propagate = True

        logger.setLevel(logging.NOTSET)
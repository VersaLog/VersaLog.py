from VersaLog import *

logger = VersaLog(enum="detailed")

logger.add_webhook(
    url="",
    level="ERROR",
    format="discord",
)

logger.error("error")
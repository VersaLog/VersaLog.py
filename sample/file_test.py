from VersaLog import *

logger = VersaLog(mode="file")
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")
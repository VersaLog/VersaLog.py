from VersaLog import *

# show_file False
logger = VersaLog(mode="detailed", show_file=False)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_file True
logger = VersaLog(mode="detailed", show_file=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_tag False
logger = VersaLog(mode="detailed", show_tag=False)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_tag True
logger = VersaLog(mode="detailed", show_tag=True, tag="VersaLog")
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# all True
logger = VersaLog(mode="detailed", all=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")
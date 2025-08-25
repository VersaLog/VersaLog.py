from VersaLog import *

# show_file False
logger = VersaLog(mode="simple")
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_file True
logger = VersaLog(mode="simple", show_file=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_tag False
logger = VersaLog(mode="simple")
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_tag True
logger = VersaLog(mode="simple", show_tag=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# notice False
logger = VersaLog(mode="simple")
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# notice True
logger = VersaLog(mode="simple", notice=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# silent False
logger = VersaLog(mode="simple", all_save=True, silent=False)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# silent True
logger = VersaLog(mode="simple", all_save=True, silent=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# enable_all True
logger = VersaLog(mode="simple", tag="VersaLog",enable_all=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")
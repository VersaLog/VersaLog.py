from VersaLog import *

# show_file False
logger = VersaLog(enum="simple")
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_file True
logger = VersaLog(enum="simple", show_file=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_tag False
logger = VersaLog(enum="simple")
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_tag True
logger = VersaLog(enum="simple", show_tag=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# notice False
logger = VersaLog(enum="simple")
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# notice True
logger = VersaLog(enum="simple", notice=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# silent False
logger = VersaLog(enum="simple", all_save=True, silent=False)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# silent True
logger = VersaLog(enum="simple", all_save=True, silent=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# enable_all True
logger = VersaLog(enum="simple", tag="VersaLog",enable_all=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")
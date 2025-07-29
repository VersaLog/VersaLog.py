from VersaLog import *

# show_file False
logger = VersaLog(mode="simple2", show_file=False, show_tag=False, notice=False)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_file True
logger = VersaLog(mode="simple2", show_file=True, show_tag=False, notice=False)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_tag False
logger = VersaLog(mode="simple2", show_file=False, show_tag=False, notice=False)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# show_tag True
logger = VersaLog(mode="simple2", show_file=False, show_tag=True, notice=False, tag="VersaLog")
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# notice False
logger = VersaLog(mode="simple2", show_file=False, show_tag=False, notice=False)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# notice True
logger = VersaLog(mode="simple2", show_file=False, show_tag=False, notice=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")

# enable_all True
logger = VersaLog(mode="simple2", enable_all=True)
logger.info("ok")
logger.error("err")
logger.warning("war")
logger.debug("deb")
logger.critical("cri")
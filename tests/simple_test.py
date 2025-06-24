from VersaLog import *

# show_file False
logger = VersaLog(mode="simple")
logger.info("ok")
logger.err("err")
logger.war("war")

# show_file True
logger = VersaLog(mode="simple", show_file=True)
logger.info("ok")
logger.err("err")
logger.war("war")
from VersaLog import *

# show_file False
logger = VersaLog(mode="detailed", show_file=False)
logger.info("ok")
logger.err("err")
logger.war("war")

# show_file True
logger = VersaLog(mode="detailed", show_file=True)
logger.info("ok")
logger.err("err")
logger.war("war")
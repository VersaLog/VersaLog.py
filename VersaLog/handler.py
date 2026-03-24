import logging

class VersaLogHandler(logging.Handler):
    def __init__(self, versalog):
        super().__init__()
        self.versalog = versalog

    def emit(self, record):
        msg = record.getMessage()

        if record.levelno >= logging.ERROR:
            self.versalog.error(msg)
        elif record.levelno == logging.DEBUG:
            self.versalog.debug(msg)
        else:
            self.versalog.info(msg)
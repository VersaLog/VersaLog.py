import logging

class VersaLogHandler(logging.Handler):
    def __init__(self, versalog):
        super().__init__()
        self.versalog = versalog

    def emit(self, record):
        msg = self.format(record)

        if record.levelno >= logging.CRITICAL:
            self.versalog.critical(msg)
        elif record.levelno >= logging.ERROR:
            self.versalog.error(msg)
        elif record.levelno >= logging.WARNING:
            self.versalog.warning(msg)
        elif record.levelno >= logging.INFO:
            self.versalog.info(msg)
        else:
            self.versalog.debug(msg)
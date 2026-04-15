from .generic import setup_logging


def setup_flask_logging(app, versalog):
    setup_logging(versalog)

    app.logger.handlers.clear()
    app.logger.propagate = True
from flask import Flask
from VersaLog import VersaLog, setup_flask_logging

log = VersaLog(enum="detailed", show_tag=True, tag="API")

app = Flask(__name__)

setup_flask_logging(app, log)

@app.route("/")
def root():
    log.info("Hello")
    return {"msg": "ok"}
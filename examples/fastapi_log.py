from fastapi import FastAPI
from VersaLog import VersaLog, setup_fastapi_logging

log = VersaLog(enum="detailed", show_tag=True, tag="API")

setup_fastapi_logging(log)

app = FastAPI()

@app.get("/")
def root():
    log.info("Hello")
    return {"msg": "ok"}
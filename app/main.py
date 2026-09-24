import math
import os
import time

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    version = os.getenv("APP_VERSION", "1.0.0")
    feature_flag = os.getenv("ENABLE_PREMIUM_UI", "false").lower() == "true"
    pod_name = os.getenv("HOSTNAME", "local-dev-machine")

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "version": version,
            "feature_flag": feature_flag,
            "pod_name": pod_name,
        },
    )


@app.get("/api/pod")
def get_pod():
    return {"pod_name": os.getenv("HOSTNAME", "local-dev-machine")}


@app.get("/stress")
def stress_cpu(seconds: int = 20):
    seconds = max(1, min(seconds, 60))
    end_time = time.monotonic() + seconds

    while time.monotonic() < end_time:
        math.factorial(5000)

    return {"status": "CPU stressed", "seconds": seconds}
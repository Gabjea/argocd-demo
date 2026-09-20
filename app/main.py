import os
import math
import time
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

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
            "pod_name": pod_name
        }
    )

@app.get("/api/pod")
def get_pod():
    return {"pod_name": os.getenv("HOSTNAME", "local-dev-machine")}

@app.get("/stress")
def stress_cpu():
    end_time = time.time() + 2
    while time.time() < end_time:
        math.factorial(5000)
    return {"status": "CPU stressed"}
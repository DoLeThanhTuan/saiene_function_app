from fastapi import FastAPI

from api.healthcheck.healthcheck_controller import router as healthcheck_router
from configs.env import get_settings

settings = get_settings()

app = FastAPI()

app.include_router(healthcheck_router,prefix="/api/healthcheck",tags=["Health Check"])

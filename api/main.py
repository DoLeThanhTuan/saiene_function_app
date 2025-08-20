from fastapi import FastAPI

from api.healthcheck.healthcheck_controller import router as healthcheck_router
from api.errorcheck.errorcheck_controller import router as errorcheck_router
from utils.application import create_fastapi

app = create_fastapi()


app.include_router(healthcheck_router,prefix="/api/healthcheck",tags=["Health Check"])
app.include_router(errorcheck_router,prefix="/api/errorcheck",tags=["Error Check"])

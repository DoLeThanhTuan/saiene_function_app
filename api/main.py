from fastapi import FastAPI

from api.healthcheck.healthcheck_controller import router as healthcheck_router


app = FastAPI()

app.include_router(healthcheck_router,prefix="/api/healthcheck",tags=["Health Check"])

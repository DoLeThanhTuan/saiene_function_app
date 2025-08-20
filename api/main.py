
from api.healthcheck.healthcheck_controller import router as healthcheck_router
from utils.application import create_fastapi

app = create_fastapi()

app.include_router(healthcheck_router,prefix="/api/healthcheck",tags=["Health Check"])

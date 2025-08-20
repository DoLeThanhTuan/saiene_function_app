from fastapi import FastAPI

from api.healthcheck.healthcheck_controller import router as healthcheck_router
from configs.env import get_settings
from exceptions.app_exception import AppException
from exceptions.handler import app_exception_handler, system_exception_handler
from exceptions.system_exception import SystemException

settings = get_settings()
fastapi_params = {
        "title": settings.app_name,
        "version": settings.api_version,
    }
app = FastAPI(**fastapi_params)

__EXCEPTION_HANDLERS__ = [
        (AppException, app_exception_handler),
        (SystemException, system_exception_handler),
    ]

for exc, handler in __EXCEPTION_HANDLERS__:
    app.add_exception_handler(exc, handler)

app.include_router(healthcheck_router,prefix="/api/healthcheck",tags=["Health Check"])

from fastapi import FastAPI, Request
from core.configs.env import get_settings
from core.utils.response import response_success
from core.utils.application import create_fastapi

settings = get_settings()

route: str = f"{settings.api_prefix}/healthcheck"
app: FastAPI = create_fastapi(route)


@app.get("/")
def health_check(request: Request):
    return response_success(f'Health check is ok with auth: {request.state.name} ({request.state.email})')

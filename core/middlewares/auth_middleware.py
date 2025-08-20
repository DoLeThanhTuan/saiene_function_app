from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from core.configs.env import get_settings
from core.configs.logging_conf import logger
from core.exceptions.app_exception import AppException, Unauthorized, DecodeError
from core.exceptions.system_exception import SystemException
from core.utils.response import response_fail
import jwt

settings = get_settings()


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Do something for authentication here
        logger.info(">>>>>> Start auth")
        try:
            check_token(request)
            return await call_next(request)
        except AppException as e:
            return response_fail(e)
        except Exception:
            logger.exception("")
            return response_fail(SystemException())
        finally:
            logger.info(">>>>>> End auth")


def check_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer"):
        logger.warning(">>>>>> No auth header")
        raise Unauthorized()
    try:
        token = auth_header[7:]
        decode = jwt.decode(token, options={"verify_signature": False})
        request.state.email = decode["preferred_username"]
        request.state.name = decode["name"]
    except jwt.PyJWTError as e:
        logger.error(f"JWT Decode Error: {str(e)}")
        raise DecodeError()

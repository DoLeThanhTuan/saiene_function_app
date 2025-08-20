import azure.functions as func
from api.healthcheck.healthcheck_controller import app as healthcheck_app  # Import ứng dụng FastAPI của bạn

# Điểm khởi đầu của Azure Functions
app = func.FunctionApp()

# Đăng ký ứng dụng FastAPI của bạn với Azure Functions
# Đoạn mã này sẽ bắt tất cả các request đến /api/healthcheck/* và chuyển cho FastAPI
@app.route(route="healthcheck/{*route}", auth_level=func.AuthLevel.ANONYMOUS)
async def healthcheck(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """
    Điều hướng tất cả các request trong route 'healthcheck' cho ứng dụng FastAPI xử lý.
    """
    return await func.AsgiMiddleware(healthcheck_app).handle_async(req, context)

# Bạn có thể đăng ký thêm các app khác ở đây
# @app.route(route="users/{*route}", auth_level=func.AuthLevel.FUNCTION)
# async def users(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
#     return await func.AsgiMiddleware(users_app).handle_async(req, context)
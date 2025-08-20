import azure.functions as func
from api.main import app as main_app

# 2. Khởi tạo Azure Function App
app = func.FunctionApp()

# 3. Đăng ký ứng dụng FastAPI với Azure Functions
#    Route ở đây phải khớp với route prefix mà bạn định nghĩa.
@app.route(route="{*route}", auth_level=func.AuthLevel.ANONYMOUS)
async def healthcheck(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """
    Điều hướng tất cả các request trong route 'healthcheck' cho ứng dụng FastAPI.
    """
    return await func.AsgiMiddleware(main_app).handle_async(req, context)

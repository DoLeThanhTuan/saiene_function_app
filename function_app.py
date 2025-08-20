import azure.functions as func
from api.main import app as main_app

app = func.FunctionApp()

@app.route(route="{*route}", auth_level=func.AuthLevel.ANONYMOUS)
async def main_api(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(main_app).handle_async(req, context)

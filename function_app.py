import azure.functions as func
import logging

# 1. Khởi tạo một đối tượng FunctionApp. Đây là điểm khởi đầu.
app = func.FunctionApp()


# 2. Sử dụng decorator `@app.route` để định nghĩa một HTTP Trigger.
#    - route="hello": URL của API sẽ là /api/hello
#    - auth_level=func.AuthLevel.ANONYMOUS: Cho phép bất kỳ ai cũng có thể gọi mà không cần API key.
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger_hello(req: func.HttpRequest) -> func.HttpResponse:
    """
    Một hàm HTTP Trigger đơn giản.
    """
    logging.info("Python HTTP trigger function processed a request.")

    # Lấy tham số 'name' từ query string (ví dụ: /api/hello?name=World)
    name = req.params.get("name")
    if not name:
        try:
            # Nếu không có, thử lấy từ body của request (JSON)
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully."
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )

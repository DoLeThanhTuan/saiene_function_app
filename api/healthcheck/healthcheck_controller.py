from fastapi import APIRouter, Depends, Request
from core.utils.response import response_success

router = APIRouter()

@router.get("/")
def health_check_root(request: Request):
    """
    Endpoint cơ bản để kiểm tra sức khỏe.
    """
    # Middleware đã xử lý xác thực, bạn có thể truy cập thông tin user ở đây
    # Ví dụ: user_email = request.state.user.email
    return response_success("Health check is OK!")

@router.get("/details")
def health_check_details():
    """
    Endpoint trả về thông tin chi tiết hơn.
    """
    return response_success({
        "status": "Healthy",
        "services": {
            "database": "Connected",
            "cache": "Connected"
        }
    })

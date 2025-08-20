from fastapi import APIRouter, Depends, Request

router = APIRouter()

@router.get("/")
def health_check_root(request: Request):
    """
    Endpoint cơ bản để kiểm tra sức khỏe.
    """
    # Middleware đã xử lý xác thực, bạn có thể truy cập thông tin user ở đây
    # Ví dụ: user_email = request.state.user.email
    return "Health check is OK!"

@router.get("/details")
def health_check_details():
    """
    Endpoint trả về thông tin chi tiết hơn.
    """
    return {
        "status": "Healthy",
        "services": {
            "database": "Connected",
            "cache": "Connected"
        }
    }

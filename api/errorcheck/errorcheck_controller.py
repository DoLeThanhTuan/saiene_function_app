from fastapi import APIRouter


router = APIRouter()

@router.get("/conflict")
def health_check_error_test():
    """
    Endpoint này cố tình gây ra lỗi để kiểm tra exception handler.
    """
    # Exception này sẽ được bắt bởi app_exception_handler mà bạn đã cấu hình
    return "Error"

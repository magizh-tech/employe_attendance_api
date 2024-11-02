from fastapi import APIRouter

from .attendance import router as attendance_router
from .employee import router as employee_router
from .leave_management import router as leave_management_router
from .auth import router as auth_router
from .breaks import router as breaks_router

# Create a main router instance
router = APIRouter()

# Include each router
router.include_router(attendance_router, prefix="/attendance")
router.include_router(employee_router, prefix="/employee")
router.include_router(leave_management_router, prefix="/leave_management")
router.include_router(auth_router, prefix="/auth")
router.include_router(breaks_router, prefix="/breaks")

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from modules.api.controller import login_controller, login_check_controller
from modules.api.models import Phone


router = APIRouter()

@router.post(path="/login/")
async def login(phone: Phone) -> JSONResponse:
    qr_url = await login_controller(phone.phone_number)
    return JSONResponse(content={"qr_link_url": qr_url})

@router.get(path="/check/login")
async def check_login(phone: str) -> JSONResponse:
    return JSONResponse(content={"status": login_check_controller(phone)})

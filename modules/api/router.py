from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from modules.api.controller import get_messages_controller, login_controller, login_check_controller, send_message_controller
from modules.api.models import MessageGetModel, MessageSendModel, Phone


router = APIRouter()

@router.post(path="/login/", response_class=JSONResponse)
async def login(phone: Phone) -> JSONResponse:
    qr_url = await login_controller(phone.phone_number)
    return JSONResponse(content={"qr_link_url": qr_url}, status_code=status.HTTP_202_ACCEPTED)

@router.get(path="/check/login", response_class=JSONResponse)
async def check_login(phone: str) -> JSONResponse:
    return JSONResponse(content={"status": (await login_check_controller(phone)).value}, status_code=status.HTTP_200_OK)

@router.get(path="/messages", response_model=list[MessageGetModel])
async def get_messages(phone: str, uname: str) -> JSONResponse:
    messages = await get_messages_controller(phone, uname)
    return JSONResponse(content=messages, status_code=status.HTTP_200_OK)

@router.post(path="/messages")
async def send_messages(message: MessageSendModel) -> JSONResponse:
    result = await send_message_controller(message.from_phone, message.username, message.message_text)
    return JSONResponse(content={"status": result if not result else "ok"})

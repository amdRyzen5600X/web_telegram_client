import os
from telethon import TelegramClient

from config import API_ID, API_HASH
from modules import database
from modules.api.exceptions import ConnectionAlreadyExsist
from modules.api.models import CheckResult
from modules.telethon.qr_login import login


async def login_controller(phone_number: str) -> str:
    session_path = await database.PhoneSessionDB.get_phone_session_pair(phone_number)
    if session_path is not None:
        print(session_path)
        raise ConnectionAlreadyExsist(phone_number)
    await database.PhoneSessionDB.create_phone_session_pair(phone_number)
    client = TelegramClient(session=phone_number, api_id=API_ID, api_hash=API_HASH)
    return await login(client)

async def login_check_controller(phone_number: str) -> CheckResult:
    session = await database.PhoneSessionDB.get_phone_session_pair(phone_number)
    if session is None:
        return CheckResult.ERROR
    elif os.path.isfile(f"../../{session}"):
        return CheckResult.LOGINED

    return CheckResult.WAITING
    

import asyncio
import os
from telethon import TelegramClient, errors

from config import API_ID, API_HASH
from modules import database
from modules.api.exceptions import ConnectionAlreadyExsist
from modules.api.models import CheckResult, MessageGetModel
from modules.telethon import login, get_messages, send_message


async def login_task_handler(task: asyncio.Task, phone: str):
    try:
        await task
    except asyncio.TimeoutError:
        await database.PhoneSessionDB.del_phone_session_pair(phone)

async def login_controller(phone_number: str) -> str:
    session_path = await database.PhoneSessionDB.get_phone_session_pair(phone_number)
    if session_path is not None:
        print(session_path)
        raise ConnectionAlreadyExsist(phone_number)
    await database.PhoneSessionDB.create_phone_session_pair(phone_number)
    client = TelegramClient(session=phone_number, api_id=API_ID, api_hash=API_HASH)
    qr_login = await login(client)
    asyncio.create_task(login_task_handler(asyncio.create_task(qr_login.wait()), phone_number))

    return qr_login.url

async def login_check_controller(phone_number: str) -> CheckResult:
    session = await database.PhoneSessionDB.get_phone_session_pair(phone_number)
    if session is None:
        return CheckResult.ERROR
    elif os.path.isfile(f"../../{session}"):
        return CheckResult.LOGINED

    return CheckResult.WAITING
    
async def get_messages_controller(phone_number: str, uname: str) -> list[MessageGetModel]:
    client = TelegramClient(session=phone_number, api_id=API_ID, api_hash=API_HASH)
    result = await get_messages(client, uname)
    return list(map(lambda member: MessageGetModel(message_text=member[0].message, is_self=member[1], username=uname), result))

async def send_message_controller(phone_number: str, uname: str, message: str) -> None | str:
    client = TelegramClient(session=phone_number, api_id=API_ID, api_hash=API_HASH)
    try:
        await send_message(client, message, uname)
    except errors.RPCError as ex:
        return str(ex)

    

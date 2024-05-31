from telethon import TelegramClient
from telethon.tl.types import Message


async def login(client: TelegramClient) -> str:
    await client.connect()
    qr_login = await client.qr_login()
    return qr_login.url

async def get_messages(client: TelegramClient, uname: str) -> list[tuple[Message, bool]]:
    result = []
    self_messages = []
    await client.connect()
    async for message in client.iter_messages(uname, limit=50, from_user="me"):
        self_messages.append(message)

    async for message in client.iter_messages(uname, limit=50):
        result.append((message, message in self_messages))

    return result


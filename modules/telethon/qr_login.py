from telethon import TelegramClient


async def login(client: TelegramClient) -> str:
    await client.connect()
    qr_login = await client.qr_login()
    return qr_login.url

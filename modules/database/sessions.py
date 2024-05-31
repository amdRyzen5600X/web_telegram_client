from redis.asyncio.client import Redis


class PhoneSessionDB:
    redis: Redis

    @classmethod
    async def connect(cls, dsn):
        cls.redis = await Redis.from_url(dsn)

    @classmethod
    async def create_phone_session_pair(cls, phone_number: str) -> None:
        await cls.redis.set(phone_number, f"{phone_number}.session")

    @classmethod
    async def get_phone_session_pair(cls, phone_number: str) -> str | None:
        res = await cls.redis.get(phone_number)
        return str(res) if res else None

    @classmethod
    async def close(cls):
        await cls.redis.aclose()


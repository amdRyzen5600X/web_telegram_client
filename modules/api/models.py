from enum import Enum
from pydantic import BaseModel


class Phone(BaseModel):
    phone_number: str

class MessageModel(BaseModel):
    message_text: str
    from_phone: str
    username: str

class CheckResult(Enum):
    WAITING = "wainitg_qr_login"
    LOGINED = "logined"
    ERROR = "error"

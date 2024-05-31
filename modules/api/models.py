from enum import Enum
from pydantic import BaseModel


class Phone(BaseModel):
    phone_number: str

class MessageModel(BaseModel):
    message_text: str
    is_self: bool
    username: str

class CheckResult(Enum):
    WAITING = "wainitg_qr_login"
    LOGINED = "logined"
    ERROR = "error"

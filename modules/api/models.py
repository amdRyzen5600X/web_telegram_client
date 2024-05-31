from pydantic import BaseModel


class Phone(BaseModel):
    phone_number: str

class MessageModel(BaseModel):
    message_text: str
    from_phone: str
    username: str

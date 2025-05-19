from pydantic import BaseModel

class login_respose(BaseModel):
    username: str
    password: str

class chatbot_respose(BaseModel):
    chat: str
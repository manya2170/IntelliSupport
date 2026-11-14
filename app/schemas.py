
from pydantic import BaseModel, Field, EmailStr


class TicketCreate(BaseModel):
    customer_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    message: str = Field(min_length=5, max_length=2000)


class TicketResponse(BaseModel):
    id: int
    customer_name: str
    email: EmailStr
    message: str
    status: str

    class Config:
        from_attributes = True


class ChatRequest(BaseModel):
    message: str = Field(min_length=2, max_length=2000)

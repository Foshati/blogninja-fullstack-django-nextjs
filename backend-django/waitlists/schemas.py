import datetime
from ninja import Schema
from pydantic import EmailStr



class WaitlistCreateSchema(Schema):
    # Create -> Data
    email: EmailStr


class WaitlistListSchema(Schema):
    # List -> Data
    id:int
    email:EmailStr


class WaitlistDetailSchema(Schema):
    # Get -> Data
    email: EmailStr
    create:datetime


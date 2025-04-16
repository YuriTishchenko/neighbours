from typing import Optional, List
from pydantic import BaseModel, Field, validator, root_validator
from pydantic_extra_types.phone_numbers import PhoneNumber

class UserBase(BaseModel):
    name: Optional[str] = Field(None, example='Yuri')
    surname: Optional[str] = Field(None, example='Yurievich')
    telegram_username: Optional[str] = Field(None, example='MyNickname')
    phone: Optional[PhoneNumber] = Field(None, example='+79117777777')
    @root_validator(skip_on_failure=True)
    def at_least_one_required(cls, values):
        if not(values.get('name') or values.get('surname') or values.get('telegram_username')):
            raise ValueError(
                'Хотя бы одно из полей должно быть Имя, Фамилия или телегам ник должно быть заполнено.'
            )

class UserCreate(UserBase):
    flats: List[int] = Field(..., example=[1, 2])

class UserUpdate(UserBase):
    name: Optional[str] = Field(None, example='Yuri')
    surname: Optional[str] = Field(None, example='Yurievich')
    telegram_username: Optional[str] = Field(None, example='MyNickname')
    phone: Optional[PhoneNumber] = Field(None, example='+79117777777')
    flats: Optional[List[int]] = Field(None, example=[1, 2])

class UserDB(UserBase):
    id: int
    class Config:
        orm_mode = True
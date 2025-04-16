from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str

class RoleDB(RoleBase):
    id: int

    class Config:
        orm_mode = True

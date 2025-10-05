from pydantic import BaseModel

class Body(BaseModel):
    serie: list[int]
    
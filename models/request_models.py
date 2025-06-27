from pydantic import BaseModel

class SumaRequest(BaseModel):
    a: float
    b: float

class MultiRequest(BaseModel):
    a: float
    b: float

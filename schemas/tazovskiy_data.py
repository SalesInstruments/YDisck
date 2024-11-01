from pydantic import BaseModel

class Tazovskiy(BaseModel):
    ID: int 
    SCALEID: int
    NAME: str
    ADDITIONALNAME: str

class TazovskiyData(BaseModel):
    N: int 
    T: str
    V: int


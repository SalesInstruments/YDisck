from pydantic import BaseModel

class RequestData(BaseModel):
    table_name: str
    start_row: str
    end_row: str
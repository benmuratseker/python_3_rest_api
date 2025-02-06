import datetime
import decimal

from pydantic import BaseModel

#with schema we can filter fields from dbModel that we want to return from fastapi operation
class Event(BaseModel):
    id: int
    #product_code: str
    date: datetime.date
    price: decimal.Decimal
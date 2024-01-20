from datetime import datetime, date
from pydantic import BaseModel, Field
from fastapi import FastAPI, Query
import uvicorn
from typing import Optional

app = FastAPI()


# schema
class ResponceBooks(BaseModel):
    location: str
    date_from: date
    date_to: date
    stars: int
    spa: bool

class BookingPost(BaseModel):
    room_id: int
    date_from: date
    date_to: date

@app.get("/hotels/{location}", response_model=list[ResponceBooks])
def get_hotels(
        location: str,  # Информация в строке запроса
        date_from: date,  # query параметры `/?date_form=...&date_to=...`
        date_to: date,
        stars: Optional[int] = Query(le=5, ge=1, default=None),  # Опциональный параметр, по умолчанию None
        spa: Optional[bool] = None  # Опциональный параметр, по умолчанию None
):
    return [{
        "location": location,
        "date_from": date_from,
        "date_to": date_to,
        "stars": stars,
        "spa": spa
    }]

@app.post('/bookings/{loca}')
def add_booking(booking: BookingPost,
                loca):
    return loca



if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

from pydantic import BaseModel, validator, Field, RootModel
from typing import Literal, List
from datetime import date

class BookingDates(BaseModel):
    checkin: date
    checkout: date

class BookingData(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str

class Booking(BaseModel):
    bookingid: int

class BookingList(RootModel[List[Booking]]):
    pass

class PostBookingAnswer(BaseModel):
    bookingid: int
    booking: BookingData




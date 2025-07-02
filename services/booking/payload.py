from services.booking.models.booking_models import BookingDates
from datetime import date
from typing import Dict


class PayLoad:

    @staticmethod
    def post_booking(firstname: str, lastname: str, totalprice: int, depositpaid: bool, bookingdates: dict, additionalneeds: str):
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'totalprice': totalprice,
            'depositpaid': depositpaid,
            'bookingdates': {
                'checkin': bookingdates['checkin'],
                'checkout': bookingdates['checkout']
            },
            'additionalneeds': additionalneeds
        }
        return data


    @staticmethod
    def put_booking(firstname: str, lastname: str, totalprice: int, depositpaid: bool, bookingdates: BookingDates, additionalneeds: str):
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'totalprice': totalprice,
            'depositpaid': depositpaid,
            'bookingdates': {
                bookingdates.checkin,
                bookingdates.checkout
            },
            'additionalneeds': additionalneeds
        }
        return data


    @staticmethod
    def patch_booking(kwargs: list):
        data = {}
        for field in kwargs:
            data[field.key] = field.value

        return data

from services.booking.endpoints import Endpoints as ep
from services.booking.payload import PayLoad as pl
import requests


class BookingApi:


    @staticmethod
    def get_bookings():
        response = requests.get(
            url=ep.get(),
        )
        return response


    @staticmethod
    def get_booking(booking_id: int = ''):
        response = requests.get(
            url=ep.get(booking_id)
        )
        return response


    @staticmethod
    def post_booking(**kwargs):
        response = requests.post(
            url=ep.post(),
            json=pl.post_booking(**kwargs)
        )
        return response


    @staticmethod
    def put_booking(**kwargs):
        response = requests.put(
            url=ep.post(),
            json=pl.put_booking(**kwargs)
        )
        return response


    @staticmethod
    def patch_booking(**kwargs):
        response = requests.patch(
            url=ep.post(),
            json=pl.patch_booking(**kwargs)
        )
        return response


    @staticmethod
    def delete_booking(booking_id: int):
        response = requests.delete(
            url=ep.delete(booking_id)
        )
        return response
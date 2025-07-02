from basetest import BaseTest
from services.generate_text import GenerateText as GT
from services.generate_date import GenerateDate as GD
from services.booking.payload import PayLoad as pl
import pytest
import random


class TestBookingApi(BaseTest):


    def test_get_bookings_positive(self, validate_response):
        """
        Тест отправляет GET запрос на получение списка всех бронирований.
        Проводит валидацию ответа
        """
        response = self.booking.get_bookings()
        assert response.status_code == 200, response.json()
        validator = validate_response.validate(response.json(), 'booking_get_bookings')
        assert validator


    @pytest.mark.parametrize('booking_id', [ 561 ])
    def test_get_booking_positive(self, validate_response, booking_id):
        """
        Тест отправляет GET запрос на получение информации конкретного бронирования.
        Проводит валидацию ответа
        """
        response = self.booking.get_booking(booking_id)
        assert response.status_code == 200, response.json()
        print(response.json())
        validator = validate_response.validate(response.json(), 'booking_get_booking')
        assert validator


    @pytest.mark.negative
    @pytest.mark.parametrize('booking_id', [
        GT.generate_char(random.randint(1,50)),
        random.randint(10000,100000),
    ])
    def test_get_booking_negative(self, validate_response, booking_id):
        """
        Тест отправляет GET запрос на получение информации конкретного бронирования с неверным booking id.
        """
        response = self.booking.get_booking(booking_id)
        assert response.status_code == 404, response.json()


    @pytest.mark.parametrize('data', [
        pl.post_booking(
        firstname=GT.generate_char(26),
        lastname=GT.generate_char(26),
        totalprice=random.randint(1,1000),
        depositpaid=True,
        bookingdates={
            'checkin': GD.generate_date_from_today(random.randint(1,30)),
            'checkout': GD.generate_date_from_today(random.randint(1,30))
    },
        additionalneeds=GT.generate_char(26)
    ) ])
    def test_post_booking_positive(self, validate_response, data):
        """
        Тест отправляет POST запрос на создание бронирования и проводит валидацию ответа
        """
        response = self.booking.post_booking(**data)
        assert response.status_code == 200, response.json()
        booking_id = response.json()['bookingid']
        print(f'bookingid: {booking_id}')
        validator = validate_response.validate(response.json(), 'booking_post_answer')
        assert validator

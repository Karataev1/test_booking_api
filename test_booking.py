from basetest import BaseTest
from services.generate_text import GenerateText as GT
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


    @pytest.mark.parametrize('booking_id', [ 1 ])
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

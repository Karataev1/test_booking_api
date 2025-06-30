from services.auth.auth_api import AuthApi
from services.booking.booking_api import BookingApi


class BaseTest:

    def setup_method(self):

        self.auth = AuthApi()
        self.booking = BookingApi()
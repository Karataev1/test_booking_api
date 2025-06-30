import allure

main_url = 'https://restful-booker.herokuapp.com'

class Endpoints:


    @staticmethod
    def get(booking_id:int = ''):
        url = f'{main_url}/booking/{booking_id}'
        return url


    @staticmethod
    def post():
        url = f'{main_url}/booking/'
        return url


    @staticmethod
    def put(booking_id: int):
        url = f'{main_url}/booking/{booking_id}'
        return url


    @staticmethod
    def path(booking_id: int):
        url = f'{main_url}/booking/{booking_id}'
        return url


    @staticmethod
    def delete(booking_id: int):
        url = f'{main_url}/booking/{booking_id}'
        return url
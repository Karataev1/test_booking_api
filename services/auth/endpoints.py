import allure

main_url = 'https://restful-booker.herokuapp.com'

class Endpoints:

    @staticmethod
    def post():
        url = f'{main_url}/auth'
        return url
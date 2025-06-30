

class PayLoad:

    @staticmethod
    def post(username: str, password: str):
        data = {
            'username': username,
            'password': password
        }
        return data

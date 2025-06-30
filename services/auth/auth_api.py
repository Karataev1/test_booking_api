from services.auth.payload import PayLoad as pl
from services.auth.endpoints import Endpoints as ep

import requests


class AuthApi:


    @staticmethod
    def create_new_token_auth(**kwargs):
        response = requests.post(
            url=ep.post(),
            json=pl.post(**kwargs)
        )
        return response
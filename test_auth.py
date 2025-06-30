from basetest import BaseTest
from services.auth.payload import PayLoad as pl
from services.generate_text import GenerateText as GT
import random
import pytest



class TestAuthApi(BaseTest):


    @pytest.mark.parametrize('data', [
        pl.post(username='admin', password='password123')
    ])
    def test_create_new_token_auth_positive(self, data, validate_response):
        """
        Тест отправляет POST запрос на создание токена аутентификации
        и проводит валидацию ответа
        """
        response = self.auth.create_new_token_auth(**data)
        assert response.status_code == 200, response.json()
        validator = validate_response.validate(response.json(),'auth_post_token_answer')
        assert validator


    @pytest.mark.negative
    @pytest.mark.parametrize('data',[
        # Тест кейс с неверными двумя полями
        pl.post(username=GT.generate_char(random.randint(1,100)),
                password=GT.generate_char(random.randint(1,100))),
        # Тест кейс с неверным полем password
        pl.post(username='admin',
                password=GT.generate_char(random.randint(1, 100))),
        # Тест кейс с неверным полем username
        pl.post(username=GT.generate_char(random.randint(1, 100)),
                password='password123')
    ])
    def test_create_new_token_auth_negative(self, data, validate_response):
        """
        Тест отправляет POST запрос на создание токена аутентификации
        с неверными полями username и password. Проводит валидацию ответа
        """
        response = self.auth.create_new_token_auth(**data)
        assert response.status_code == 200, response.json()
        validator = validate_response.validate(response.json(),'auth_post_token_answer_negative')
        assert validator

from services.validation import ResponseValidator
from services.auth.auth_api import AuthApi
import pytest


@pytest.fixture()
def validate_response():
    return ResponseValidator()


@pytest.fixture()
def auth_token():
    return AuthApi.create_new_token_auth().json()

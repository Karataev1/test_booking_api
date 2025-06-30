from pydantic import BaseModel, validator, Field
from typing import Literal


class TokenModel(BaseModel):
    username: str
    password: str


class AnswerCreateTokenPositive(BaseModel):
    token: str


class AnswerCreateTokenNegative(BaseModel):
    reason: Literal['Bad credentials']
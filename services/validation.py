from services.auth.models.auth_models import TokenModel,AnswerCreateTokenPositive,AnswerCreateTokenNegative
from services.booking.models.booking_models import BookingList, BookingData, PostBookingAnswer
from pydantic import ValidationError


class ResponseValidator:
    def __init__(self):
        self.validators = {
            'auth_post_token_answer': lambda response_json: AnswerCreateTokenPositive(**response_json),
            'auth_post_token_answer_negative': lambda response_json: AnswerCreateTokenNegative(**response_json),
            'booking_get_bookings': lambda response_json: BookingList(response_json),
            'booking_get_booking': lambda response_json: BookingData(**response_json),
            'booking_post_answer': lambda response_json: PostBookingAnswer(**response_json)
        }

    def validate(self, response_json, type_of_validation: str):
        validator = self.validators.get(type_of_validation)

        try:
            return validator(response_json)
        except ValidationError as e:
            raise ValueError(f"Ошибка валидации: {e}") from e
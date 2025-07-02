from datetime import datetime, timedelta
import random


class GenerateDate:


    @staticmethod
    def generate_date_from_today(day: int):
        """
        Метод генерирует будущую дату на N дней вперед
        :param day:
        :return: future_date
        """
        today = datetime.today()
        future_date = today + timedelta(days=day)
        return str(future_date.date())
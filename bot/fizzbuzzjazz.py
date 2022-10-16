import datetime

from dateutil.parser import isoparse


class FizzBuzzJazz:
    def get_fizzbuzzjazz(self, event: dict) -> str:
        """
        Take AWS Eventbridge event JSON and return `FizzBuzzJazz` value.

        :param event: AWS Eventbridge event
        :return: FizzBuzzJazz value
        """
        # Extract date from event
        date = isoparse(event["time"]).date()

        # Calculate day number
        current_year = date.year
        year_start = datetime.date(year=current_year, month=1, day=1)
        day_number = (date - year_start).days + 1

        # Calculate FBJ value
        fbj = ""
        fbj_values = [(3, "fizz"), (5, "buzz"), (7, "jazz")]
        for denominator, fbj_value in fbj_values:
            if day_number % denominator == 0:
                fbj += fbj_value
        return fbj if fbj else str(day_number)

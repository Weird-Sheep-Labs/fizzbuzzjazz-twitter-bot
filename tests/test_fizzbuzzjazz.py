import datetime
from unittest import TestCase

from bot.fizzbuzzjazz import FizzBuzzJazz


class TestFizzBuzzJazz(TestCase):
    def setUp(self):
        super().setUp()
        self.test_matrix = [
            ("2022-01-01T12:00:00Z", "1"),
            ("2022-01-03T12:00:00Z", "fizz"),
            ("2022-01-05T12:00:00Z", "buzz"),
            ("2022-01-07T12:00:00Z", "jazz"),
            ("2022-01-15T12:00:00Z", "fizzbuzz"),
            ("2022-02-11T12:00:00Z", "fizzjazz"),
            ("2022-03-11T12:00:00Z", "buzzjazz"),
            ("2022-07-29T12:00:00Z", "fizzbuzzjazz"),
            ("2022-09-24T12:00:00Z", "fizz"),
            ("2022-12-31T12:00:00Z", "buzz"),
            # 2024 is a leap year
            ("2024-01-01T12:00:00Z", "1"),
            ("2024-01-03T12:00:00Z", "fizz"),
            ("2024-01-05T12:00:00Z", "buzz"),
            ("2024-01-07T12:00:00Z", "jazz"),
            ("2024-01-15T12:00:00Z", "fizzbuzz"),
            ("2024-02-11T12:00:00Z", "fizzjazz"),
            ("2024-03-10T12:00:00Z", "buzzjazz"),
            ("2024-03-11T12:00:00Z", "71"),
            ("2024-07-28T12:00:00Z", "fizzbuzzjazz"),
            ("2024-07-29T12:00:00Z", "211"),
            ("2024-09-23T12:00:00Z", "fizz"),
            ("2024-09-24T12:00:00Z", "268"),
            ("2024-12-30T12:00:00Z", "buzz"),
            ("2024-12-31T12:00:00Z", "fizz"),
        ]

    def test_get_fizzbuzzjazz(self):
        for i, (iso_date, fbj) in enumerate(self.test_matrix):
            with self.subTest(i=i):
                event = {"time": iso_date}
                assert FizzBuzzJazz().get_fizzbuzzjazz(event) == fbj

import datetime
from enum import Enum


class InterviewResult(Enum):
    RECRUITED = "recruited"
    DENIED = "denied"
    CALL_LATER = "call later"


class Interview:
    interviews_conducted = 0

    @staticmethod
    def print_amount_of_conducted_interviews():
        print(f"Interviews conducted:{Interview.interviews_conducted}")

    def __init__(self, topic = "Data Science Engineer position offer", location = "Lviv",
                 date = datetime.datetime.now() + datetime.timedelta(days = 1),
                 duration = datetime.timedelta(hours = 1), interviewer_name = "Max Dmytryshyn",
                 result = InterviewResult.CALL_LATER):
        self.topic = topic
        self.location = location
        self.date = date
        self.duration = duration
        self.interviewer_name = interviewer_name
        self.result = result
        Interview.interviews_conducted += 1

    def __str__(self):
        return f"Interview topic: {self.topic} \n" \
               f"Interview location: {self.location} \n" \
               f"Interview date: {self.date:%d.%m.%Y %H:%M} \n" \
               f"Interview duration: {self.duration} \n" \
               f"Interviewer name: {self.interviewer_name} \n" \
               f"Interview result: {self.result.value}"

    def __del__(self):
        print(f"Interview from", str(self.date)[:16], "deleted")

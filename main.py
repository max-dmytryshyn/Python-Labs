import interview
import datetime
if __name__ == '__main__':
    first_interview = interview.Interview()
    second_interview = interview.Interview("Junior C++ Developer offer", "Sheptytskykh Street, 26, Lviv",
                                           datetime.datetime(2021, 3, 10, 17))
    third_interview = interview.Interview("Senior Java Developer offer", "Sadova Street, 2D, Lviv",
                                          datetime.datetime(2021, 4, 4, 18, 30),
                                          datetime.timedelta(hours = 1, minutes= 30), "Andriy Tyslyak",
                                          interview.InterviewResult.RECRUITED)
    print("_______Interview 1_______")
    print(first_interview)
    print("_______Interview 2_______")
    print(second_interview)
    print("_______Interview 3_______")
    print(third_interview)
    print("-------------------------")
    interview.Interview.print_amount_of_conducted_interviews()




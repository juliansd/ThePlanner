
"""
Homework Sort

What do we have to consider from the course_homework objects? What are grading
exactly? We are grading each course by importance and in turn grading the
homework for each by importance as well as taking into
considering the due date of course.


Variables we have to consider:

Relevance (Major(M), Minor(m), General Elective(ge))
    Major - 0.55
    Minor - 0.25
    General Elective - 0.2

Credits
    8 credits - 0.9
    6 credits - 0.7
    4 credits - 0.6
    3 & 2 credits - 0.4

Type of Homework
    Paper
    Group Project
    Web Assign
    Weekly Assignment - 0.7
    Midterm Study - 1
    Quiz Study
    Final Study
    Presentation

Due Date
    Scales with how many days are left until due starting at 7


Algorithm:

The function 'I' scales with respect to days until due date 'd',
call it I(d).  Relevance 'r', credits the course has 'c', and type of the
homework 't' are all constants.

    I(D) = rct / d

Accumulates to total score of 4

"""
import pickle


class HomeworkSort():
    def homework_sort(course_object):

    homework_sort(pickle.load(open("user_data.p", "rb")))

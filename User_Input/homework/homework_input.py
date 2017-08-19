
def transform(metadata):
    """Transform input from user about homework."""
    homework = {}

    course = str(input("Which course is the assignment for: "))
    kind = str(input("What kind of homework assignment is this: "))
    due_date = str(input("When is the assignment due: "))
    hours_to_finish = float(input("How many hours will it take to complete: "))

    homework["course"] = course
    homework["kind"] = kind
    homework["due_date"] = due_date
    homework["hours_to_finish"] = hours_to_finish

    return homework

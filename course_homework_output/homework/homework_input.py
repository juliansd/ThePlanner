
def transform(metadata):
    """Transform input from user about homework."""
    homework = {}

    verification = input(
        "Do you have homework for this class you would like to add? ")

    if verification == "yes" or verification == "y":

        course = str(input("Which course is the assignment for: "))
        title = str(input("Title of assignment: "))
        kind = str(input("What kind of homework assignment is this: "))
        due_date = str(input("When is the assignment due: "))
        hours_to_finish = float(
            input("How many hours will it take to complete: "))

        homework["title"] = title
        homework["kind"] = kind
        homework["due_date"] = due_date
        homework["hours_to_finish"] = hours_to_finish

    else:
        pass

    return homework

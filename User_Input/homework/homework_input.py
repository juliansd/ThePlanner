def transform(kind, due_date, hours_to_finish):
    homework = {}

    kind = str(input("What kind of homework assignment is this: "))
    due_date = str(input("When is the assignment due: "))
    hours_to_finish = float(input("How many hours will it take to complete: "))

    homework["kind"] = kind
    homework["due_date"] = due_date
    homework["hours_to_finish"] = hours_to_finish

    return homework

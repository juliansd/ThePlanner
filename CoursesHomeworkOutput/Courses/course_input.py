
def transform(metadata):
    """Transform user input into a class object."""
    retval = []
    course_object = {}

    course = str(input("Course name: "))
    course_object["title"] = course

    credits = int(input("Course credits: "))
    course_object["credits"] = credits

    importance = str(input(
        "Where are course credits allocated to: "))
    course_object["importance"] = importance

    hours_per_week = float(input("Hours of course per week: "))
    course_object["hours_per_week"] = hours_per_week

    course_object["homework"] = []

    retval.append(course_object)
    return(retval)

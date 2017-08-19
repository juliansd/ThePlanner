def transform(course, credits, importance, hours_per_week):
    # num_of_courses = int(input("Number of courses this semester: "))
    retval = []
    course_object = {}
    course = str(input("Course name: "))
    course_object["course"] = course
    credits = int(input("Course credits: "))
    course_object["credits"] = credits
    importance = str(input(
        "Where are course credits allocated to: "))
    course_object["importance"] = importance
    hours_per_week = float(input("Hours of course per week: "))
    course_object["hours_per_week"] = hours_per_week
    retval.append(course_object)
    return retval

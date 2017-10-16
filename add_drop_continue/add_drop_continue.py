"""Imports pickle class for data storage and streaming."""
import pickle


class AddDropContinue:
    """Class for adding, dropping, and showing user's planner."""

    def add_course():
        """Add course to planner and stores in pickle file."""
        course_object = {}

        title = input("What is the title of the course: ")
        course_object["title"] = title

        try:
            credits = int(input("How many credits is the course: "))
            course_object["credits"] = credits
        except ValueError as e:
            raise e
            print("Please enter an integer for your course credits. ")

        try:
            hours_per_week = float(input(
                "How many hours per week is the course: "))
            course_object["hours_per_week"] = hours_per_week
        except ValueError as e:
            raise e
            print(
                "Please enter a floating point value for the hours per week you \
                attend this course")

        pickle.dump(course_object, open("user_data.p", "wb"))

    # def drop_course():

    # def continue_to_planner():


def main():
    """Main method, runs initial input."""
    print("\n Welcome to your planner! What would you like to do? \n")
    add_drop_continue = input(
        "You can `add` (a), `drop` (d) , or `continue` (c) to your planner: ")
    if add_drop_continue == 'add' or add_drop_continue == 'a':
        AddDropContinue.add_course()
    # elif add_drop_continue == 'drop' or add_drop_continue == 'd':
    #     # drop_course()
    # elif add_drop_continue == 'continue' or add_drop_continue == 'c':
    #     # continue_to_planner()
    else:
        raise ValueError("Please input 'add', 'drop', or 'continue' ")
main()

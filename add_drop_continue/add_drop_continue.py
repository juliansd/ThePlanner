"""Imports pickle class for data storage and streaming."""
import pickle


class AddDropContinue:
    """Class for adding, dropping, and showing user's planner."""

    course_list = []

    def add_course(self):
        """Add course to planner and stores in pickle file."""
        course_object = {}

        title = input("What is the title of the course: ")
        course_object["title"] = title

        importance = input(
            "Is this for your major(M), minor(m), or a general elective(ge): ")
        course_object["importance"] = importance

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
        AddDropContinue.course_list.append(course_object)

        # Stores course_object as a binary file to a pickle file
        pickle.dump(AddDropContinue.course_list, open(
            "user_data.p", "wb"))


def main():
    """Main method, runs initial input."""
    user = AddDropContinue()
    flag = False
    print("\n Welcome to your planner! What would you like to do? \n")
    while not flag:
        add_drop_continue = input(
            "You can `add`(a), `drop`(d) , or `continue`(c) to your planner: ")
        if add_drop_continue == 'add' or add_drop_continue == 'a':
            user.add_course()
        elif add_drop_continue == 'end' or add_drop_continue == 'e':
            flag = True
        else:
            raise ValueError("Please input 'add', 'drop', or 'continue' ")
main()

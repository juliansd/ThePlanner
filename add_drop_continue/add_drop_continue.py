"""Imports pickle class for data storage and streaming."""
import pickle


class AddDropContinue:
    """Class for adding, dropping, and showing user's planner."""

    course_list = []

    def command_tooltips(self):
        """A method which shows a list of commands."""
        print("")
        print("**************************************************************")
        print("List of Planner commands:\n")

        # add command tooltip
        print(
            "add(a) \t\t Prompts user to add course to their `course_list`\n")

        # drop command tooltip
        print("drop(d) \t Prompts the user to drop course from their")
        print("\t\t`course_list`\n")

        # continue command tooltip
        print("continue(c) \t Takes user to their planner\n")

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

    def drop_course(self):
        """Method for dropping courses from user_data."""
        course_list = pickle.load(open("user_data.p", "rb"))
        print("Current course list:\n")

        for course_object in course_list:
            print(course_object["title"])
        print("\n")

        course_to_drop = input("Which course would you like to drop: ")
        for course_object in course_list:
            if course_object["title"] == course_to_drop:
                course_list.remove(course_object)

        pickle.dump(course_list, open("user_data.p", "wb"))


def main():
    """Main method, runs initial input."""
    user = AddDropContinue()
    flag = False
    print("Welcome to your planner! What would you like to do? \n")
    print("You can `add`(a), `drop`(d) , or `continue`(c) to your planner. \n")
    while not flag:
        add_drop_continue = input(
            "Enter `help`(h) for a list of all commands: ")
        if add_drop_continue == 'add' or add_drop_continue == 'a':
            user.add_course()
        elif add_drop_continue == 'drop' or add_drop_continue == 'd':
            user.drop_course()
        elif add_drop_continue == 'help' or add_drop_continue == 'h':
            user.command_tooltips()
        elif add_drop_continue == 'end' or add_drop_continue == 'e':
            flag = True
        else:
            raise ValueError("Please input 'add', 'drop', or 'continue' ")
main()

"""Add Drop module."""


class AddDrop:
    """A Class for adding and dropping classes."""

    def add_drop():
        """Method which prompts the user to add or drop a course."""
        # object to be returned if user chooses to add a course.
        course_object = {}
        add_drop_continue = input(
            "Would you like add, drop, or continue to your planner: ")
        if add_drop_continue == "add":
            course_title = input("What is the title of the course: ")
            course_object["title"] = course_title

            # Raises exception if user doesn't enter an integer.
            try:
                credits = int(input("How many credits is the course: "))
                course_object["credits"] = credits
            except Exception as e:
                raise e
                print("Please enter an integer")
            try:
                hours_per_week = float(
                    input("How many hours per week is the course: "))
                course_object["hours_per_week"] = hours_per_week
            except Exception as e:
                raise e
                print("Please enter an integer or floating point value")

            course_object["homework"] = []

            return course_object

        elif add_drop_continue == "drop":
            # Searches for class to be dropped and drops it.
            print("Class is dropped.")
        elif add_drop_continue == "continue":
            # Will bring user to their planner.
            print("Here is your planner!")
        else:
            raise ValueError(
                "Invalid input. Please input 'add', drop', 'continue'")


def main():
    """Main method which runs classes methods."""
    print(AddDrop.add_drop())
main()

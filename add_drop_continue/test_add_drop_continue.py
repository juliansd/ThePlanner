"""Testing framework for dropping a class from `user_data.p`."""
import unittest
import pickle


class TestAddDropContinue(unittest.TestCase):
    """A class which allows for testing of methods."""

    def test_drop(self):
        """Testing whether if the correct course_object is removed."""
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

        expected_result = [
            {
                'title': 'intro to comp sci', 'importance': 'M', 'credits': 4,
                'hours_per_week': 2.5
            }
        ]
        self.assertEqual(course_list, expected_result)

if __name__ == '__main__':
    unittest.main()

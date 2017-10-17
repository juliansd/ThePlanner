import unittest
import pickle
from add_drop_continue import AddDropContinue


class TestDropCourse(unittest.TestCase):
    def test_drop_course(course_to_drop):
        user_data = pickle.load(open("user_data.p", "rb"))
        print(course_to_drop, "course to drop")

if __name__ == '__main__':
    unittest.main()

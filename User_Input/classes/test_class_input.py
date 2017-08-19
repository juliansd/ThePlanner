import unittest
import class_input


class TestClassInput(unittest.TestCase):
    def test_class_input(self):
        courses = ["Intro to Computer Science"]
        credits = [4]
        importance = ["major"]
        hours_per_week = [2.5]
        result = class_input.transform(
            courses, credits, importance, hours_per_week)
        expected_result = [
            {"course": "Intro to Computer Science",
                "credits": 4, "importance": "major", "hours_per_week": 2.5}]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

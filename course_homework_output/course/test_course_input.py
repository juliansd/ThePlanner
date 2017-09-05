"""Import unittest and function."""
import unittest
import course_input


class TestCourseInput(unittest.TestCase):
    """Unittest test Class."""

    def test_course_input(self):
        """Test course_input function."""
        metadata = ["Intro to Computer Science", 4, "major", 2.5]
        result = course_input.transform(metadata)
        expected_result = [
            {
                "title": "Intro to Computer Science",
                "credits": 4, "importance": "major",
                "hours_per_week": 2.5,
                "homework": []
            }
        ]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

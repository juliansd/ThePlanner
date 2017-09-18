"""Import unittest and function."""
import unittest
import homework_input


class TestHomeworkInput(unittest.TestCase):
    """Unittest class."""

    def test_homework_input(self):
        """Test homework_input function."""
        metadata = [
            "AI in the World", "paper",
            "12/19", 1.5
        ]
        results = homework_input.transform(metadata)
        expected_results = {
            "title": "AI in the World",
            "kind": "paper",
            "due_date": "12/19",
            "hours_to_finish": 1.5
        }
        self.assertEqual(results, expected_results)
if __name__ == "__main__":
    unittest.main()

import unittest
import homework_input


class TestHomeworkInput(unittest.TestCase):
    def test_homework_input(self):
        kind = "paper"
        due_date = "12/19"
        hours_to_finish = 1.5
        results = homework_input.transform(kind, due_date, hours_to_finish)
        expected_results = {
            "kind": "paper", "due_date": "12/19", "hours_to_finish": 1.5}
        self.assertEqual(results, expected_results)
if __name__ == "__main__":
    unittest.main()

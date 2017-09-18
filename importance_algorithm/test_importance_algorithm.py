"""Import unittest and function."""
import unittest
import importance_algorithm


class TestImportanceAlgorithm(unittest.TestCase):
    """Unittest class."""

    def test_importance_algorithm(self):
        metadata = """
            [{'title': 'Intro to Computer Science', 'credits': 4,
            'importance': 'major', 'hours_per_week': 2.5,
            'homework': {'title': 'AI in the World', 'kind': 'paper',
            'due_date': '12/19', 'hours_to_finish': 1.5}}]
        """
        result = importance_algorithm.calculate_score(metadata)
        expected_result

if __name__ == "__main__":
    unittest.main()

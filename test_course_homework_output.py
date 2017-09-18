
import unittest
import course_homework_output


class TestCourseHomeworkOutput(unittest.TestCase):
    def test_course_homework_output(self):
        first_input = ["Intro to Computer Science", 4, "major", 2.5]
        course_metadata = course_homework_output.course.course_input.transform(
            first_input)
        print(course_metadata)

        second_input = [
            "Intro to Computer Science", "AI in the World", "paper",
            "12/19", 1.5
        ]
        homework_metadata = \
            course_homework_output.homework.homework_input.transform(
                second_input)
        print(homework_metadata)

        course_metadata[0]["homework"] = homework_metadata

        file_object = open('output_file.txt', 'r+')
        file_object.write(str(course_metadata))

        result = file_object.read()
        expected_result = """
            [
                {
                    'title': 'Intro to Computer Science', 'credits': 4, '
                    importance': 'major', 'hours_per_week': 2.5,
                    'homework': [
                        'title': 'AI in the World','kind': 'paper',
                        'due_date': '12/19','hours_to_finish': 1.5
                    ]
                }
            ]
        """

if __name__ == "__main__":
    unittest.main()

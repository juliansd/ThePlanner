import unittest
import courses
import homework
import writetofile

class TestCoursesHomeworkOutput(unittest.TestCase):
    def test_courses_homework_output(self):
        metadata = {}
        step1 = courses.course_input.transform(metadata)
        step2 = homework.homework_input.transform(step1)
        step3 = writetofile.write_to_file.output_to_file(step2)

        file_object = open('output_file.txt', 'r')

        result = file_object.read()
        expected_result = []

if __name__ == "__main__":
    unittest.main()

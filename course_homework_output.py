"""This file runs the main method for course_homework_output.

We import modules from subdirectories of course_homework_output which allow us
to grab user input on their courses and homework and then write the data to a
file as a list of dictionaries.
"""
import coursehomeworkoutput.course.course_input
import coursehomeworkoutput.homework.homework_input
import coursehomeworkoutput.write_to_file.write


def final_output(metadata):
    """
    Output a list of dictionaries with data on classes and homework.

    This method takes metadata as an argument which is a list of dictionaries
    containing data on the user's courses and homework returns data which is
    written to a file on the user's courses and homework assignments.
    """
    output_1 = coursehomeworkoutput.course.course_input.transform(metadata)
    output_2 = coursehomeworkoutput.homework.homework_input.transform(output_1)
    retval = coursehomeworkoutput.writeotofile.write_to_file.write_file(
        output_2)

    return retval

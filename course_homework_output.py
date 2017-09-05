
import coursehomeworkoutput.course.course_input
import coursehomeworkoutput.homework.homework_input
import coursehomeworkoutput.write_to_file.write


def final_output(metadata):

    output_1 = coursehomeworkoutput.course.course_input.transform(metadata)
    output_2 = coursehomeworkoutput.homework.homework_input.transform(output_1)
    retval = coursehomeworkoutput.writeotofile.write_to_file.write_file(
        output_2)

    return retval


def output_to_file(metadata):
    file_object = open("output_file.txt", "w")
    file_object.write(metadata)
    file_object.close()
output_to_file(
    str(
        [
            {
                "title": "Intro to Computer Science",
                "credits": 4,
                "importance": "major",
                "hours_per_week": 2.5,
                "homework": []
            }
        ]
    )
)

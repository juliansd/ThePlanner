
"""
    Category calculations out of a score of 4.

    -   Whether if it's for a major, minor, or general elective
        - major = 0.75
        - minor = 0.5
        - general elective = 0.25
    -   What kind of assignment is due
        - kinds include:
            final study (FS) = 0.8
            midterm study (MS) = 0.8
            test study (TS) = 0.7
            group project (GP) = 0.7
            paper (P) = 0.5
            programming exercises (PE) = 0.5
            web assign (WA) = 0.5
            weekly math homework (WMH) = 0.5
            quiz study (QS) = 0.5
            reading (R) = 0.4
            personal project (PP) = 0.3
    -   When an assignment is due
        - For every day until the due date (unless specified otherwise like the
            User would like to work on the assignment 3 days a week) the score
            goes up by +0.05.
    -   How long the user thinks it will take them to complete the assignment
        - The algorithm will take the inputed hours from the user, and divide
            By 5.  For examlple if the assignment will take 3 hours to
            Complete, time_to_complete will be scored at 0.6
"""

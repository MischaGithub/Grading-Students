#Grading Student

#Creatinga function to calculate the 3 marks and then getting a average
def take_mark(mark1, mark2, mark3):
    """

    >>> take_mark(80, 40, 75)
    65.0

    """

    average = (mark1 + mark2 + mark3) / 3

    return average

#Creating a function to take the avearge mark and the determining
#if its a pass or fail

def average_mark(average):

    if average >= 50:
        mark = "passed"

        return mark

    else:
        mark = "failed"

        return mark



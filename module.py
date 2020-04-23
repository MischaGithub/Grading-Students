
#Creating the function to add all the marks and then dividing it by the amount of marks
def marks(mk1, mk2, mk3):
    """
    >>> marks(25, 15, 60)
    100
    """

    return (mk1+mk2+mk3)//3


#Creating a if statement to determine the average mark
def average_mark(average):
#If the mark is more than or equal to 50 the student passed and returns the mark
    if average >= 50:
        mark = "passed"

        return mark
#Else if the mark is less than 50 the student fails
    else:
        mark = "failed"

        return mark

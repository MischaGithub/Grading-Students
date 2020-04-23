#display the marks

mark_1 = float(input("Please enter mark 1: \n"))
mark_2 = float(input("Please enter mark 2: \n"))
mark_3 = float(input("Please enter mark 3: \n"))

import marks

final_mark = int(marks.take_mark(mark_1, mark_2, mark_3))
print("The Final average mark is", final_mark, "%")

final_average = marks.average_mark(final_mark)
print("The Student:", final_average)






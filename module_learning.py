#Importing from module to get the expected results
import module

#Having the user input the 3 marks
mark1 = int(input("Enter first mark: \n"))
mark2 = int(input("Enter second mark: \n"))
mark3 = int(input("Enter third mark: \n"))

#Performing the results of the marks enter by the user
int_average = module.marks(mark1, mark2, mark3)
print("The average mark is:", int_average, "%")

#Also diplay the average for those marks entered by the user and giving a average
final_average = module.average_mark(int_average)
print("The Student has:", final_average)
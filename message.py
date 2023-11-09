names =  input("Enter names separated by commas: ").title().split(",")
assignments =  input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grade separated by commas: ").split(",")
potential = [int(grade) + 2 * int(assignment) for grade, assignment in zip(grades, assignments)]

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
# decided to create a dictionary that will have the names as key and the other variables as values
student_dict = {}
for name, assignment, grade, pot in zip(names, assignments, grades, potential):
    student_dict[name] = (assignment, grade, pot)

#we need to print a message after every loop
for name, (assignment, grade, pot) in student_dict.items():
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n".format(name, assignment, grade, pot)
    print(message)

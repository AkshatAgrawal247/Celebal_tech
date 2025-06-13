n = int(input("Enter number of students: "))

student_marks = {}

for i in range(n):
    data = input("Enter name and marks: ").split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

query_name = input("Enter student name to get average: ")

marks_list = student_marks[query_name]
average = sum(marks_list) / len(marks_list)

print("Average marks: {:.2f}".format(average))

students = []

no_of_student = int(input("Please enter the number of students you want to enter:> "))

i = 0
while i < no_of_student:
    name = input("Please enter name:> ")
    marks = int(input("Please enter marks:> "))
    roll = int(input("Please enter roll:> "))
    student = {
        "name": name,
        "marks": marks,
        "roll": roll
    }
    students.append(student)
    i += 1
print("NAME,    marks,    roll")
for x in students:
    print(x["name"], x["marks"], x["roll"], sep="      ")
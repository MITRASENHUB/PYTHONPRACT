# input: name of the student, roll no., marks in PCMBE.
# Output : total marks, %, Passing marks 33, if failed in any one subject then considered fail

name=input("Please enter your name :> ")
rollno=input("Please enter your roll no. :>")
maths=int(input("Please enter your marks Maths:>"))
physics=int(input("Please enter your marks Physics:>"))
chemistry=int(input("Please enter your marks Chemistry :>"))
biology=int(input("Please enter your marks Biology:>"))
english=int(input("Please enter your marks English:>"))
total_marks=maths+physics+chemistry+biology+english
percentage=total_marks/5    
print("total Marks :> ",total_marks)
print("Percentage", percentage)

if maths > 33 or physics > 33 or chemistry > 33 or biology > 33 or english > 33:
    print("Pass")
else:
    print("Fail")    
        
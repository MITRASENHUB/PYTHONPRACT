print("Please confirm if the student is pass or fail")
physics=int(input("please enter the marks of Physics :)"))
chemistry=int(input("please enter the marks of Chemistry :)"))
biology=int(input("please enter the marks of Biology :)"))
if physics+chemistry+biology < 60:
    print("Fail - Better Luck next Time")
else:
    print("Pass - Best Wishes")
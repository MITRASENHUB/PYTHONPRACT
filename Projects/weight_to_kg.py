print("hello monika")
weight=int(input('Please enter your weight : >  '))
unit= input('(l)bs or (k)g :   ')
if unit.upper() == "l" :
    converted=weight*0.45
    print(f"you are {converted} kilos")
else:
    converted=weight//0.45
    print(f"you are {converted} pounds")
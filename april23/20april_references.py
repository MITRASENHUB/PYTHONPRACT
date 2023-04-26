a = [1,2,3 ,4 ,5]
print(id(a))
print(a) 
b=a
b.append(7)
b.append(1)
a[1]="APPLE"
print(id(b))
b[1]="MIT"
a[1]="APPLE"
print(a)
print(b)
# how to find address . just write - print("x", id(x))

c=[6,6,8,9,5,0]
d=c
d.append(9)
print(c)
print("C", id(c))
print(d)
print("D", id(d))

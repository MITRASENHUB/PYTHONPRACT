i=1
num=int(input())
factors=0
while i <= num :
    if num % i == 0:
        factors = factors + 1

    i+=1

if factors == 2:
    print("Prime")
else:
    print("Not a prime")
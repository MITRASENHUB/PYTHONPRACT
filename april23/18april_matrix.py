A = [
    [3, 5, 7, 8],
    [2, 1, 9, 3]
]

i=0
rows=2
columns=4
print("MATRIX A")
while i < rows:
    j=0
    while j < columns:
        print(A[i][j], end=" ")
        j +=1
    print()
    i += 1


B = [
    [1, 2, 3, 4],
    [8, 7, 6, 5]
]
print()
print("MATRIX B")
i=0
while i < rows:
    j=0
    while j < columns:
        print(B[i][j], end=" ")
        j +=1
    print()
    i += 1
i = 0
print()
print("A + B")
while i < rows:
    j=0
    while j < columns:
        print(A[i][j] + B[i][j], end=" ")
        j +=1
    print()
    i += 1

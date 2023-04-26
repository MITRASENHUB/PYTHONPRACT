def printMartrix(matrix):
    for a in matrix:
        for b in a:
            print(b, sep=" ", end=" ")
        print()
    print()

def add(matrix_a, matrix_b):
    C = []
    i=0
    while i < len(matrix_a):
        j = 0
        while j < len(matrix_a[i]):
            try:
                C[i].append(matrix_a[i][j] + matrix_b[i][j])
            except Exception as e:
                C.append([matrix_a[i][j] + matrix_b[i][j]])
            j += 1
        i += 1
    printMartrix(C)


def multiply(matrix_a, matrix_b):
    print(matrix_a, matrix_b)



A = [
    [1, 2 ,3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

printMartrix(A)
printMartrix(B)

add(A, B)
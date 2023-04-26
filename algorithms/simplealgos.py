def linear_search(array, x):
    for item in array:
       if item == x:
           return True
    return False

def simple_sort(array):
    i = 0
    j = 0
    while j < len(array) - 1:
        i = 0
        while i < len(array) -1:
            if array[i] > array[i + 1]:
                c = array[i + 1]
                array[i + 1] = array[i]
                array[i] = c
            i += 1
        j += 1

a = [5,1,3,4,10, 0, -1]

ret = linear_search(a, 90) 
print(ret)

simple_sort(a)
print(a)
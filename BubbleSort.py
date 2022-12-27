A = [5,3,8,9,6,2]
n = len(A)
print("Original Array : " , A)
def BubbleSort(A):
    for val in range(n-1, 0, -1):
        for var in range(0, val):
            if A[var] > A[var+1]:
                temp = A[var]
                A[var] = A[var+1]
                A[var+1] = temp
    return A

print("Sorted Array  :  ", BubbleSort(A))

# i and j are swapped from the example in sort/insertion_sort.py.
# This is so the code follows the pseudocode in CLRS.
#
# n = length of array

def insertion_sort(A):                   # COST     TIMES
    for j in range(2, len(A)):           # c1       n
        key = A[j]                       # c2       n - 1 

        i = j - 1                        # c4       n - 1
        while i > 0 and A[i] > key:      # c5       Σ (j=2,n) of tj   
            A[i+1] = A[i]                # c6       Σ (j=2,n) of (tj - 1)   
            i = i - 1                    # c7       Σ (j=2,n) of (tj - 1)  
        A[i+1] = key                     # c8       n - 1

    return A


def main():
    # Python arrays are zero-based. I'm ignoring the first element,
    # so the indices are aligned with the pseudocode in CLRS.
    list = [None, 99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    insertion_sort(list)
    print(list)

    list = [None, 3, 9, 2, 1]
    insertion_sort(list)
    print(list)

main()

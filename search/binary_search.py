import math

def binarySearch(array, target):
    if not len(array):
        return -1

    left = 0
    right = len(array)

    while (left + 1 < right):
        # The video has two forward slashes which is floor division. 
        # It only needs one, as I'm rounding up with ceil after division occurs.
        mid = math.ceil((right + left) / 2)

        if array[mid] == target:
            return mid
        elif array[mid] < target: 
            left = mid 
        else:
            right = mid

    if array[left] == target:
        return left 

    return -1


def main():
    array = [1,4,5,7,9,12,15,18,19,22,23,25,29,30,33,35,40,41,50]
    print(f'Index of 1: {binarySearch(array, 1)}')
    print(f'Index of 9: {binarySearch(array, 9)}')
    print(f'Index of 22: {binarySearch(array, 22)}')
    print(f'Index of 30: {binarySearch(array, 30)}')
    print(f'Index of 50: {binarySearch(array, 50)}')

    array = []
    print(f'Index of 100: {binarySearch(array, 100)}')

    array = [1]
    print(f'Index of 1: {binarySearch(array, 50)}')

    array = [8, 9]
    print(f'Index of 1: {binarySearch(array, 8)}')

main()

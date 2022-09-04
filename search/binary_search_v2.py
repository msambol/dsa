import math

def binarySearch_v2(array, target):
    if not len(array):
        return -1

    left = 0
    right = len(array) - 1

    while (left <= right):
        mid = math.ceil((right + left) / 2)

        if array[mid] == target:
            return mid
        elif array[mid] < target: 
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    array = [1,4,5,7,9,12,15,18,19,22,23,25,29,30,33,35,40,41,50]
    print(f'Index of 1: {binarySearch_v2(array, 1)}')
    print(f'Index of 9: {binarySearch_v2(array, 9)}')
    print(f'Index of 22: {binarySearch_v2(array, 22)}')
    print(f'Index of 30: {binarySearch_v2(array, 30)}')
    print(f'Index of 50: {binarySearch_v2(array, 50)}')

    array = []
    print(f'Index of 100: {binarySearch_v2(array, 100)}')

    array = [1]
    print(f'Index of 1: {binarySearch_v2(array, 50)}')

    array = [8, 9]
    print(f'Index of 1: {binarySearch_v2(array, 8)}')

main()

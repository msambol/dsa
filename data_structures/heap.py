from math import floor


def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def parent(i):
    return floor(i/2)


def max_heapify(a, i):
    l = 2*i
    r = 2*i + 1

    largest = i 

    if l < len(a) and a[l] > a[i]:
        largest = l
    
    if r < len(a) and a[r] > a[largest]:
        largest = r 
    
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)


def build_max_heap(a):
    for i in range(5, 0, -1):
        max_heapify(a, i)


def main():
    # root is at index 1
    # it can be at index zero but see here: https://www.quora.com/Why-do-indexes-for-heaps-start-at-1
    # and: https://stackoverflow.com/questions/22900388/why-in-a-heap-implemented-by-array-the-index-0-is-left-unused

    a = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    build_max_heap(a)

    # print heap starting with the root at index 1
    print(f'Heap: {a[1:]}')


main()

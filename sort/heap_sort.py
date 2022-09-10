def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def parent(i):
    return i//2

def max_heapify(a, heap_size, i):
    l = left(i)
    r = right(i)

    largest = i 

    if l < heap_size and a[l] > a[i]:
        largest = l
    
    if r < heap_size and a[r] > a[largest]:
        largest = r 
    
    if largest != i:
        # swap elements
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)


def build_max_heap(a):
    heap_size = len(a)

    for i in range(heap_size//2, 0, -1):
        max_heapify(a, heap_size, i)


def heap_sort(a):
    build_max_heap(a)

    for i in range(len(a)-1, 1, -1):
        # swap elements
        a[i], a[1] = a[1], a[i]

        # after the swap the last element is now sorted, but the new root may break the max-heap condition
        # fix it by calling max-heapify with a smaller heap size (sorted elements are out of the picture)
        max_heapify(a, i, 1)


def main():
    # root is at index 1
    # it can be at index zero but see here: https://www.quora.com/Why-do-indexes-for-heaps-start-at-1
    # and: https://stackoverflow.com/questions/22900388/why-in-a-heap-implemented-by-array-the-index-0-is-left-unused

    a = [None, 99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    heap_sort(a)
    print(a[1:])

    a = [None, 3, 9, 2, 1]
    heap_sort(a)
    print(a[1:])

main()
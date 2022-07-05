def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def parent(i):
    return i//2


def max_heapify(a, heap_size, i):
    l = 2*i
    r = 2*i + 1

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

def main():
    a = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    build_max_heap(a)

    print(f'Heap: {a[1:]}')


main()

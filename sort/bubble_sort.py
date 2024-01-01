def bubble_sort(list):
    n = len(list)

    for i in range(n-1):
        for j in range(n-1):
            if list[j] > list[j+1]: 
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    return list


def main():
    list = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    bubble_sort(list)
    print(list)

    list = [3, 9, 2, 1]
    bubble_sort(list)
    print(list)


main()

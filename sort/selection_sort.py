def selection_sort(list):
    n = len(list)

    for i in range(n-1): 
        min = i

        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j

        if min != i:
            temp = list[i]
            list[i] = list[min]
            list[min] = temp

    return list


def main():
    list = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    selection_sort(list)
    print(list)

    list = [3, 9, 2, 1]
    selection_sort(list)
    print(list)


main()

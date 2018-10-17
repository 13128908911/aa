# coding: utf8
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def select_sort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if array[j] < array[min]:
                min = j
        array[min], array[i] = array[i], array[min]
    return array


def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        if array[i] > array[i - 1]:
            temp = array[i]
            index = i
            for j in range(i - 1, -1, -1):
                if array[j] < temp:
                    array[j + 1] = array[j]
                    index = j
                else:
                    break
            array[index] = temp
    return array


if __name__ == '__main__':
    li = [12, 4, 1, 53, 12, 112, 95, 2, 78, 20, 30, 10, 60, 8, 6, 5, 75, 85, 112]
    # arr = bubble_sort(li)
    # arr = select_sort(li)
    arr = insert_sort(li)
    print(arr)

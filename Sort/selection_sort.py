import random

def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest_found = find_smallest(arr, i+1, len(arr)-1)
        if arr[smallest_found] < arr[i]:
            swap(arr, i, smallest_found)

    print(arr)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def find_smallest(arr, start, end):
    temp = arr[start]
    index = -1

    for i in range(start, end +1):

        if arr[i] < temp:
            temp = arr[i]
            index = i

    if index == -1:
        return start
    else:
        return index

if __name__ == "__main__":
    arr = [random.randint(1,10) for i in range(11)]
    print(arr)
    selection_sort(arr)
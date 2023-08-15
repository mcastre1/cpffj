import random

def selection_sort(arr):
    return

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def find_smallest(arr, start, end):
    temp = arr[start]

    for i in range(start, end):
        if arr[i] < temp:
            temp = arr[i]

    return temp

if __name__ == "__main__":
    arr = [random.randint(1,10) for i in range(11)]
    print(arr)
    selection_sort(arr)
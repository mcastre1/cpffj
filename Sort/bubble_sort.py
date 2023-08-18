import random


def bubble(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i]<arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]

def bblSort(arr):
    for i in range(len(arr)-1):
        bubble(arr)


if __name__ == "__main__":
    arr = [random.randint(1,10) for i in range(10)]
    print(arr)

    bblSort(arr)

    print(arr)
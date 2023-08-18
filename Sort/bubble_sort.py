import random


def bubble(arr):
    j = 0
    while j < len(arr) - 1:
        if arr[j] > arr[j + 1]:
            arr[j], arr[j+1] = arr[j + 1], arr[j]
        j += 1
        

def bblSort(arr):
    i = 0
    while i < len(arr)-1:
        bubble(arr)
        i += 1

if __name__ == "__main__":
    arr = [random.randint(1,10) for i in range(10)]
    print(arr)

    bblSort(arr)

    print(arr)
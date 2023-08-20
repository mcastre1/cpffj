import random

def insertion_sort(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            for j in range(i,-1,-1):
                if arr[j + 1] < arr[j]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]


if __name__ == "__main__":
    arr = [random.randint(1,10) for i in range(10)]
    print(arr)
    insertion_sort(arr)
    print(arr)
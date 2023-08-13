# Sort given array of n length
# Iterate through each element and place at beginning.
def simple_sort(arr, n):
    for i in range(n):

        j = i+1
        while j <= n - 1:
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)
                continue
            j += 1

    return


if __name__ == "__main__":
    import random

    # Create and populate array with n random integers.
    n = 10
    arr = [random.randint(1,100) for i in range(n)]

    print(arr)

    simple_sort(arr, n)

    print(arr)
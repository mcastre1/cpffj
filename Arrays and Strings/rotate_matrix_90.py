def rotate_90(matrix, n):
    temp = [[0]*n for i in range(n)]

    temp_j = 0

    for i in range(n):
        for j in range(n - 1, -1, -1):
            temp[i][temp_j] = matrix[j][i]
            temp_j += 1
        temp_j = 0

    print(temp)


if __name__ == "__main__":
    matrix = [[1,1,1],
              [2,7,6],
              [3,3,3]]
    rotate_90(matrix, 3)
# Write an algorithm such as if the element in a M x N matrix is 0
# its entire row and column are turned into 0

def zero_matrix(matrix):
    temp_js = []
    temp_is = []

    for j in range(len(matrix)):
        if not j in temp_js:
            for i in range(len(matrix[j])):
                if not i in temp_is:
                    if matrix[j][i] == 0:
                        temp_is.append(i)
                        temp_js.append(j)

                        for y in range(len(matrix[j])):
                            matrix[j][y] = 0

                        for x in range(len(matrix)):
                            matrix[x][i] = 0

    return matrix

if __name__ == "__main__":
    matrix = [[1,0,2,0],
              [2,3,0,1],
              [3,5,1,12]]
    
    print(zero_matrix(matrix))
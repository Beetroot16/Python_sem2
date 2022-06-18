matrix1 = [[0 for i in range(3)] for j in range(3)]
matrix2 = [[0 for i in range(3)] for j in range(3)]
final_matrix = [[0 for i in range(3)] for j in range(3)]

def input_mat(matrix,rows):
    for i in range(int(rows)):
        matrix[i] = list(map(int,input().split()))
    print(matrix)

def multipy(matrix1,matrix2):
    for j in range(3):
        for k in range(3):
            sum = 0
            for l in range(3):
                sum = sum + matrix1[j][l]*matrix2[l][k]
            final_matrix[j][k] = sum
    print(final_matrix)
    
input_mat(matrix1,3)
input_mat(matrix2,3)
multipy(matrix1,matrix2)
        



"""
Реализуйте функцию snail_path(), которая принимает на вход матрицу и возвращает 
список элементов матрицы по порядку следования от левого верхнего элемента по часовой
стрелке к внутреннему. Движение по матрице напоминает улитку
"""


def snail_path(matrix):

    if not len(matrix):
        return []

    output = []
    
    # 0 - right, 1 - down, 2 - left, 3 - up
    direction = 0
    
    # track rows and columns we have passed
    hor_stop, vert_stop = len(matrix[0]), len(matrix)
    hor_start = 0
    vert_start = 0 
   
    # track row and col to iter through it 
    last_row = 0
    last_col = 0

    while hor_start < hor_stop and vert_start < vert_stop:
        if direction == 0:
            for i in range(hor_start, hor_stop):
                output.append(matrix[last_row][i])
                last_col = i
            
            vert_start += 1

        if direction == 1:
            for i in range(vert_start, vert_stop):
                output.append(matrix[i][last_col])
                last_row = i
            

            hor_stop -= 1

        if direction == 2:
            for i in range(hor_stop - 1, hor_start - 1, -1):
                output.append(matrix[last_row][i])
                last_col = i
            
            vert_stop -= 1

        if direction == 3:
            for i in range(vert_stop - 1, vert_start - 1, -1):
                output.append(matrix[i][last_col])
                last_row = i
            
            hor_start += 1

        
        direction = (direction + 1) % 4

    return output




print(snail_path([
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],
   [13, 14, 15, 16],
   [17, 18, 19, 20]
]))

print(snail_path([[1,2],[3,4]]))
print(snail_path([[1,2,3]]))


# this solution was coped from hexlet

def rotate(matrix):
    """
    Counter-clockwise rotation
    """
    return list(reversed(list(zip(*matrix))))

def snail_path_2(matrix):
    path = []

    def trace(submatrix):
        if not submatrix:
            return 
        path.extend(submatrix[0])
        trace(rotate(submatrix[1:]))

    trace(matrix)
    return path


print(snail_path_2([
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],
   [13, 14, 15, 16],
   [17, 18, 19, 20]
]))

print(snail_path_2([[1,2],[3,4]]))
print(snail_path_2([[1,2,3]]))

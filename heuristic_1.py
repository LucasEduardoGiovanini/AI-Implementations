import math

# heuristic_1 : return (right_side - left_side).
#               Se a matriz for par, retorna a diferenca entre a soma dos pilares da
#               primeira metade e a soma dos pilares da segunda metade.

#               Se a matriz for ímpar, encontra o pilar do meio, e o ignora, para
#               encontrar a diferença entre a soma dos pilares da direita e a
#               soma dos pilares da esquerda.


#-----------------------------------------------------------------------------------------------------------------------------------------------
def sumColumns(matrix, From, To):           # Returns sum of columns "From" until "To"
    total = 0
    for column in range(From,To+1):
        for row in range(len(matrix)):
            total += matrix[row][column]
    return total

#-----------------------------------------------------------------------------------------------------------------------------------------------
def heuristic_1(hanoi_matrix):

    left_side =0
    right_side = 0

    is_odd = len(hanoi_matrix[0]) % 2 == 1
    middle = math.ceil(len(hanoi_matrix[0]) / 2) - 1

    if(is_odd):                                                                        # if odd,
        left_side = sumColumns(hanoi_matrix,0,middle-1)                                # sums left columns and ignores middle
        right_side = sumColumns(hanoi_matrix,middle+1,len(hanoi_matrix[0])-1)          # sums right columns and ignores middle

    else:                                                                              # if even,
        left_side = sumColumns(hanoi_matrix, 0, middle)                                # sums left columns
        right_side = sumColumns(hanoi_matrix, middle+1, len(hanoi_matrix[0]) - 1)      # sums right columns

    return(right_side-left_side)  # returns difference of right and left

#               0  1  2
hanoi_tower = [[0, 0, 0],
               [2, 0, 0],
               [3, 0, 1]]

print(heuristic_1(hanoi_tower))
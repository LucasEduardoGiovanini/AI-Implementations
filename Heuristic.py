import numpy as np
import math

matrix_tower_hanoi = np.array([[1,0,0],
                               [2,0,2],
                               [3,0,2]])

def calculating_matrix_length(matrix):  #essa função verifica o tamanho da matriz em colunas, para que possamos estipular quais colunas presentam esquerda e direita
    total_number_pillars=(matrix.shape[1]) #shape[1] represent columns in the tupple result

    if total_number_pillars %2 ==1: #if number of pillars  is odd (impar)
        print("pilar do meio = ",total_number_pillars/2)
        middle_pillar = math.ceil(total_number_pillars/2) #the middle pilar is defined by the rounding(math.ceil) of num of pillars/2
        return middle_pillar-1

middle_pilar = calculating_matrix_length(matrix_tower_hanoi)

tamanhos = np.shape(matrix_tower_hanoi)  # pego a quantidade de linhas e de colunas da matriz

sum_col_dir_e_col_esq = list(); #armazeno a soma total da coluna a esquerda e a soma total da colunaa direita
soma=0;
for x in range(0,tamanhos[1]): #começo varrendo as colunas, pois caso a matriz seja, por exemplo, 3x2, vai dar problema na leitura
    if (x != middle_pilar): #quer desconsiderar a soma do pilar lateral
        for y in range(0,tamanhos[0]):
            soma+=matrix_tower_hanoi[y][x] #somo a posição
        sum_col_dir_e_col_esq.append(soma)#armazeno a soma na posição da lista
        soma=0;
    else:
        pass


print(sum_col_dir_e_col_esq)


#def calculate_the_best_move(matrix, middle_pilar):









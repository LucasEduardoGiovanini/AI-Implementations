def run(start_matrix, goal_matrix):
    goal_reached = False
    state_list = [[start_matrix, True]]

    Depth_Hanoi(start_matrix, goal_matrix, state_list, goal_reached)



def Move_hanoi(matrix, list, coluna_atual, coluna_destino):   # move da coluna X para a coluna Y
    copy = [[0,0,0],[0,0,0],[0,0,0]]  # copia para trabalhar com a matriz

    for i in range(0,3):
        for j in range(0,3):
            copy[i][j] = matrix[i][j]


    continuar = True
    has_moved = False

    for i in range(0,3):
        if copy[i][coluna_atual] !=  0 and continuar:        # le a coluna atual do topo ate o fim, e pega o disco do topo
            for j in range(2,-1,-1):                          # le a coluna destino do fim ate o topo
                if(copy[j][coluna_destino] == 0 and j == 2): # se a posicao livre e a base
                    copy[j][coluna_destino] = copy[i][coluna_atual]   # destino = disco a ser movido
                    copy[i][coluna_atual] = 0                          # atual = 0
                    continuar = False                                   # para o codigo
                    has_moved = True                                        # diz que foi posivel mover
                    break;

                elif(copy[j][coluna_destino] == 0 and copy[j + 1][coluna_destino] > copy[i][coluna_atual]):  #0 se a posicao livre nao e a base, compara se o disco
                                                                                                                # abaixo e maior que o disco a ser movido
                    copy[j][coluna_destino] = copy[i][coluna_atual]  # destino = disco a ser movido
                    copy[i][coluna_atual] = 0                         # atual = 0
                    continuar = False                                  # para o codigo
                    has_moved = True                                       # diz que foi posivel mover
                    break;

    if(has_moved):                      # se houve um movimento
        for i in range(0,len(list)):
            if i>0 and list[i][0] == copy:       # confere se esse estado novo possui possibilidades nao exploradas
                return False;


        list.append([copy, True])       # se possui, o estado atual 'e confirmado
        matrix[:] = copy
        return True;

    return False;                                # se nao, o movimento nao e feito



def Depth_Hanoi(matrix, goal_matrix, state_list, goal_reached):
    restart_while = False                      # var aux para recomecar while

    while (not goal_reached):
        restart_while = False
        for i in range(0, 3):
            for j in range(0, 3):               # para tentar todos os movimentos possiveis

                if (Move_hanoi(matrix, state_list, i, j)):    # se o movimento e possivel
                    restart_while = True        # deve-se recomecar o while para tentar todos os moves possiveis para o novo estado
                    print("matriz atual:")
                    print(matrix[0])
                    print(matrix[1])
                    print(matrix[2])


                    if (matrix == goal_matrix):    # se achar o resultado, para tudo
                        goal_reached = True


                if(restart_while):    #quebra os FOR loops para recomecar o while
                    break
            if(restart_while):
                break

        if(not restart_while):     # se todos os movimentos foram tentados e nao se achou nenhum possivel
            for x in range(len(state_list) - 1, -1, -1):    # define o estado como False na lista de estados
                if state_list[x][0] == matrix:
                    state_list[x][1] = False;

            for x in range(len(state_list) - 1, -1, -1):     # e pega o ultimo estado True na lista de estado
                if state_list[x][1] == True:
                    matrix[:] = state_list[x][0]
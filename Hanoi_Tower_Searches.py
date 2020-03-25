# state_list   : uma matriz de duas colunas, onde a primeira representa a
#                matriz estado,e a segunda se ela ainda possui movimentos
#                inexplorados.

# Função Move  : Recebe um estado, e tenta mover uma peça da coluna X
#                para a coluna Y. Se não for possível, ou se X = Y,
#                retorna uma matriz idêntica a matriz recebida.

# Depth_Hanoi  : Tenta sempre o primeiro movimento possível de maneira
#                distribuída da esquerda até a direita, ordem:
#
#                pilar da esquerda para pilar do meio;
#                pilar da esquerda para pilar da direita;
#                pilar do meio para pilar da esquerda;
#                pilar do meio para pilar da direita;
#                pilar da direita para pilar da esquerda;
#                pilar da direita para pilar do meio;

# Breadth_Hanoi: Tenta todos os movimentos possíveis de um estado, e
#                depois muda o estado atual para o primeiro estado
#                encontrado que possua movimentos inexplorados, a não
#                ser que o ultimo estado encontrado seja o estado objetivo.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def was_visited(matrix,state_list):                #confere se o estado ja foi visitado
    for i in range(0, len(state_list)):
        if state_list[i][0] == matrix:
            return True
    return False


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_false(matrix,state_list):                  # define o estado como False na lista de estados
    for x in range(len(state_list) - 1, -1, -1):
        if state_list[x][0] == matrix:
            state_list[x][1] = False;


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_last_true(state_list):                     # pega o ultimo estado True na lista de estado
    for x in range(len(state_list) - 1, -1, -1):
        if state_list[x][1] == True:
            return state_list[x][0]


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_first_true(state_list):
    for x in range(0, len(state_list)):  # e pega o primeiro estado True na lista de estado
        if state_list[x][1] == True:
            return state_list[x][0]


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Move(matrix, state_list, coluna_x, coluna_y):   # tenta mover da coluna X para a coluna Y, e retorna a matriz resultado

    if coluna_x == coluna_y:   # nao e possivel mover uma peca para a posicao onde ele ja esta
        return matrix

    copy = [[0,0,0],[0,0,0],[0,0,0]]              # copia para trabalhar com a matriz

    for i in range(0,3):
        for j in range(0,3):
            copy[i][j] = matrix[i][j]

    has_moved = False

    for i in range(0,3):
        if copy[i][coluna_x] !=  0 and not has_moved:               # le a coluna atual do topo ate o fim, e pega o disco do topo
            for j in range(2,-1,-1):                                    # le a coluna destino do fim ate o topo

                if(copy[j][coluna_y] == 0 and j == 2):            # se a posicao livre for a base
                    copy[j][coluna_y] = copy[i][coluna_x]     # destino = disco a ser movido
                    copy[i][coluna_x] = 0                           # atual = 0
                    has_moved = True                                    # diz que foi posivel mover
                    break;

                elif(copy[j][coluna_y] == 0 and copy[j + 1][coluna_y] > copy[i][coluna_x]):   # se a posicao livre nao for a base, compara se o disco
                                                                                                              # abaixo e maior que o disco a ser movido
                    copy[j][coluna_y] = copy[i][coluna_x]   # destino = disco a ser movido
                    copy[i][coluna_x] = 0                         # atual = 0
                    has_moved = True                                  # diz que foi posivel mover
                    break;

    return copy;


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Depth_Hanoi(start_matrix, goal_matrix):

    goal_reached = False
    state_list = [[start_matrix[:], True]]      # adiciona a matriz inicial a lista de estados
    restart_while = False                       # var aux para recomecar while
    movimentos = 0

    while (not goal_reached):

        restart_while = False

        for i in range(0, 3):
            for j in range(0, 3):               # para tentar todos os movimentos possiveis

                attempt = Move(start_matrix, state_list, i, j)     # tenta mover

                if (attempt != start_matrix and not was_visited(attempt, state_list)):    # se o movimento for possivel, e o novo estado ja nao foi visitado

                    state_list.append([attempt[:], True])                          # adiciona o estado novo na lista
                    start_matrix[:] = attempt                                            # este passa a ser o estado atual

                    movimentos+=1
                    restart_while = True        # deve-se recomecar o while para tentar todos os moves possiveis para o novo estado
                    print("movimento ",movimentos)
                    print(start_matrix[0])
                    print(start_matrix[1])
                    print(start_matrix[2])

                    if (start_matrix == goal_matrix):        # se achar o resultado, para tudo
                        goal_reached = True

                if(restart_while):    #quebra os FOR loops para recomecar o while
                    break
            if(restart_while):
                break

        if(not restart_while):     # se todos os movimentos foram tentados e nao se achou nenhum possivel

            set_false(start_matrix, state_list)
            start_matrix = get_last_true(state_list)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Width_Hanoi(start_matrix, goal_matrix):
    goal_reached = False
    state_list = [[start_matrix[:], True]]     # adiciona a matriz inicial a lista de estados
    movimentos = 0

    while (not goal_reached):
        for i in range(0, 3):                  # tenta todos os movimentos para este estado
            if(not goal_reached):
                for j in range(0, 3):
                    attempt = Move(start_matrix, state_list, i, j)

                    if(attempt == goal_matrix):      # se o movimento chegou ao estado objetivo
                        start_matrix = attempt       # define como o estado atual
                        goal_reached = True

                    if not was_visited(attempt,state_list):    # se o estado novo gerado ja nao foi visitado
                        movimentos += 1
                        print("movimento ", movimentos)        # printa o estado na tela
                        print(attempt[0])
                        print(attempt[1])
                        print(attempt[2])
                        state_list.append([attempt[:], True])  # adiciona o estado na lista


        set_false(start_matrix, state_list)      # apos esgotar os movimentos possiveis, define este estado como False

        start_matrix = get_first_true(state_list)
import sys
import _util



class hanoi():
    def __init__(self):
        self.first_movement = {1:1,2:2,3:4} #em qual jogada cada disco fara seu movimento, 2^(peso do disco - 1)
        self.plays = {1:2 , 2:4, 3:8} #em que cada jogada o disco será mexido, 2^(peso do disco), Obs: inicia a contagem a partir do primeiro movimento
        self.plays_of_disk = {1:0 , 2:0, 3:0} #numero de jogadas feitas em cada disco
        self.game = [[1,0,0],
                     [2,0,0],
                     [3,0,0]]
        self.move = 1

    def detects_possible_movement(self,k): #verifica pra qual lado é possivel movimentar
        col = None        
        for i in self.game: #pega a coluna em que o k está
            if k in i:
                col = i.index(k)
        movements,maxCenter,maxLeft,maxRigth = [],0,0,0
        if col == 0 or col == 2: #verifica na duas estremidades o valor a ser retornado
            for i in self.game:
                if i[1] > maxCenter:
                    maxCenter = i[1]
                if i[2] > maxRigth:
                    maxRigth = i[2]
                elif i[0] > maxLeft:
                    maxLeft = i[0]
            if col == 0:
                return ['rigth'] if (maxCenter > k or maxCenter == 0) or (maxRigth > k or maxRigth == 0) else []
            else: 
                return ['left'] if (maxCenter > k or maxCenter == 0) or (maxLeft > k or maxLeft == 0) else []
        if col == 1: #verifica no pino central
            for i in self.game:
                if i[2] > maxRigth:
                    maxRigth = i[2]
                elif i[0] > maxLeft:
                    maxLeft = i[0]
            if maxLeft > k or maxLeft == 0: movements.append('left')
            if maxRigth > k or maxRigth == 0: movements.append('rigth')
            return movements
        return []

    def _d(self,k): #calcula se o movimento esperado é possivel
        '''
            se o numero de jogadas dos disco for par:
                se o valor do disco for par:
                    tem q ir pra esquerda
                se o valor do disco for impar:
                    tem q ir para direita
            se o numero de jogadas do disco for impar:
                se o valor do disco for impar:
                    tem q ir para esquerda
                se o valor do disco for par:
                    tem que ir para direita 
        ''' 

        '''
            se pode se mexer para a posição esperada:
                return 1
            se não pode se mexer para a posição esperada:
                return 3
        '''
        moviments = self.detects_possible_movement(k)        
        if self.plays_of_disk[k]%2 == 0:
            if k%2 == 0 and  "left" in moviments:
                return 1
            if k%2 != 0 and "rigth" in moviments:
                return 3
        if self.plays_of_disk[k]%2 != 0:
            if k%2 == 0 and  "rigth" in moviments:
                return 1
            if k%2 != 0 and "left" in moviments:
                return 3
        return 3

    def _t(self,k): #ve se jogada atual é a esperada
        '''
            se for a vez do disco mover:
                return 1
            se não for a disco mover:
                return 3
        '''
        if self.move > self.first_movement[k]:
            value = self.move
            while value > self.first_movement[k]: #regreção para descobrir de qual movimento eu partir e assim desobri se o valor atual de jogadas está na jogada do disco
                value = value - self.plays[k]
            return 1 if value == self.first_movement[k] else 3
        return 1 if self.move == self.first_movement[k] else 3

    def heuristic(self,k):
        return self._d(k) +  self._t(k)

    def verify_heristic(self,values): # calcula a heuristica para todas a posições possivel
        _min = sys.maxsize
        _id = None
        for i in values:
            heuristic = self.heuristic(i)   
            if  heuristic < _min:
                _min = heuristic
                _id =  i
        '''
            se a posição escolhida tiver uma valor diferente de 0 em cima e for diferente da posição da linha inicial:
                retira a chave da busca e calcul e pega outro valor menor da heuristica
            Obs:
                tem q ser recurção pois ele refaz a verificação
        '''
        line,col = self.get_pos_by_id(_id)
        if self.game[line-1][col] != 0 and line != 0:
            values.remove(_id)
            return self.verify_heristic(values)
        return [_id, _min]

    def complet(self): #verifica se o jogo chegou no final
        _list = []
        verify = [1,2,3]
        for i in self.game:
            _list.append(i[2])
        return verify == _list

    def get_pos_by_id(self,id): #pega a posicao no matriz pela chave
        for i in range(len(self.game)):
            if id in self.game[i]:
                return [i, self.game[i].index(id)]

    def get_max_in_col(self, col):#pega a coluna maxima
        _max = 0
        for i in self.game:
            if i[col] > _max:
                _max = i[col]
        return _max
        
    def get_max_in_line(self, col, value):#pega a linha maxima
        _max = 0
        for i in range(len(self.game)):
            if self.game[i][col] == 0 :
                _max = i
        return _max
    def print_game(self):#printa o jogo
        for i in self.game:
            print(i)
        print("")
    '''
        set uma posição por um valor e seta o valor da posição antiga como 0
    '''
    def sum_col(self,col):
        sum = 0
        for i in self.game:
            sum += i[col]
        return sum
    
    def choice_side(self,moviments,col,_id):
        if self.check_especial_case():
            return 2
        sum_cols = {}
        for i in range(0, len(self.game[0])):
            sum_cols[i] = game.sum_col(i)
        col_possible = {}
        if "rigth" in moviments:
            for i in sum_cols:
                if i > col and (self.get_max_in_col(i) > _id or self.get_max_in_col(i) == 0):
                    col_possible[i] = sum_cols[i]
        if "left" in moviments:
            for i in sum_cols:
                if i < col and (self.get_max_in_col(i) > _id or self.get_max_in_col(i) == 0):
                    col_possible[i] = sum_cols[i]
        
        if _util.dic_iqual(col_possible) == True: 
            _list = _util.dic_key(col_possible)
            return int(_list[len(_list)-1]) #retorna a primeira chave
        return _util.dic_minValue(col_possible)[0] #retorna a chave com maior valor
    def check_especial_case(self):
        if self.game[2][2] == 3 and self.game[1][2] == 2:
            return True
        return False
    def set_pos(self,line,col,_id,next_col):
        
        self.game[line][col] = 0
        self.game[self.get_max_in_line(next_col,_id)][next_col] = _id
    '''
    def set_pos(self, line, col, _id, sum):
        try:
            if self.get_max_in_col(col+sum) > _id or self.get_max_in_col(col+sum) == 0:
                    self.game[line][col] = 0
                    self.game[self.get_max_in_line(col+sum,_id)][col_id+sum] = _id
                    return True
            return False
        except: return False
    '''
list_open = [] #armazena todas as jogadas possiveis
list_lock = [] #armazena todas as jogodas passadas
list_values = {1,2,3}
game = hanoi() #instacia a torre
while game.complet() == False: #roda até que o objetivo tenha sido atigindo
#for i in range(8):
    list_values = {1,2,3}
    _id,_value = game.verify_heristic(list_values) #pega a chave escolhido pela heuristica
    line_id,col_id = game.get_pos_by_id(_id) #pega a posição no game pelo id    
    moviments = game.detects_possible_movement(_id) #pega o movimentos possiveis para a chave
    plays_of_disk = game.plays_of_disk[_id] #numero de jogadas dos discos 
    next_col = game.choice_side(moviments,col_id,_id) #escolhe o melhor lado
    game.set_pos(line_id,col_id,_id,next_col) #set a posição do disco q esta se movendo
    game.print_game()#printa o jogo    
    game.move += 1
    game.plays_of_disk[_id] += 1
a = int(input())
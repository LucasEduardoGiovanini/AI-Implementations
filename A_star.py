import sys
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
        if col == 0 or col == 2: #verifica na duas estremidades o valor a ser retornado
            maxCenter = 0
            for i in self.game:
                if i[1] > maxCenter:
                    maxCenter = i[1]
            if col == 0:
                return ['rigth'] if maxCenter > k or maxCenter == 0 else []
            else: 
                return ['left'] if maxCenter > k or maxCenter == 0 else []
        if col == 1: #verifica no pino central
            movements,maxLeft, maxRigth = [],0,0
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
        if self.game[self.get_line_by_id(_id)-1][self.get_col_by_id(_id)] != 0 and self.get_line_by_id(_id) != 0:
            values.remove(_id)
            return self.verify_heristic(values)
        return [_id, _min]

    def complet(self): #verifica se o jogo chegou no final
        _list = []
        verify = [1,2,3]
        for i in self.game:
            _list.append(i[2])
        return verify == _list

    def get_col_by_id(self,id): #pega a coluna pela chave
        for i in self.game:
            if id in i:
                return i.index(id)
        
    def get_line_by_id(self,id): #pega a linha pela chave
        for i in range(len(self.game)):
            if id in self.game[i]:
                return i
    def get_max_col(self, col):#pega a coluna maxima
        _max = 0
        for i in self.game:
            if i[col] > _max:
                _max = i[col]
        return _max
    def get_max_line(self, col, value):#pega a linha maxima
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
    def set_pos(self, line, col, _id, sum):
        try:
            if self.get_max_col(col+sum) > _id or self.get_max_col(col+sum) == 0:
                    self.game[line][col] = 0
                    self.game[self.get_max_line(col+sum,_id)][col_id+sum] = _id
                    return True
            return False
        except: return False
list_open = [] #armazena todas as jogadas possiveis
list_lock = [] #armazena todas as jogodas passadas
list_values = {1,2,3}
game = hanoi() #instacia a torre
#while game.complet() == False: #roda até que o objetivo tenha sido atigindo
for i in range(5):
    _id,_value = game.verify_heristic(list_values) #pega a chave escolhido pela heuristica
    col_id = game.get_col_by_id(_id) #pega a coluna da chave
    line_id = game.get_line_by_id(_id)# pega a linha da coluna
    moviments = game.detects_possible_movement(_id) #pega o movimentos possiveis para a chave
    plays_of_disk = game.plays_of_disk[_id] #numero de jogadas dos discos 
    
    if plays_of_disk%2 == 0:
        if _id%2 == 0 and  "left" in moviments:
            if(game.set_pos(line_id,col_id,_id,-1) == False): game.set_pos(line_id,col_id,_id,-2)     
        elif _id%2 != 0 and "rigth" in moviments or col_id == 0:            
            if(game.set_pos(line_id,col_id,_id,2) == False): game.set_pos(line_id,col_id,_id,1)
            
    else:
        if _id%2 == 0 and  "rigth" in moviments:
           if(game.set_pos(line_id,col_id,_id,2) == False): game.set_pos(line_id,col_id,_id,1)
        elif _id%2 != 0 and "left" in moviments:
            if(game.set_pos(line_id,col_id,_id,-1) == False): game.set_pos(line_id,col_id,_id,-2)
    print(game.plays_of_disk[_id], game.move)

    game.print_game()
    
    game.move += 1
    game.plays_of_disk[_id] += 1
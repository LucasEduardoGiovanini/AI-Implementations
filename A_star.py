import Heuristic

class hanoi():
    def __init__(self):
        self.first_movement = {1 : 1, 2:2,3 : 4} #em qual jogada cada disco fara seu movimento, 2^(peso do disco - 1)
        self.plays = {1 : 2 , 2 : 4, 3 : 8} #em que cada jogada o disco será mexido, 2^(peso do disco), Obs: inicia a contagem a partir do primeiro movimento
        self.plays_of_disk = {1 : 0 , 2 : 0, 3 : 0} #numero de jogadas feitas em cada disco
        self.game = [[1,0,0],
                     [2,0,0],
                     [3,0,0]]
        self.move = 0
    def detects_possible_movement(self,k):
        movents = []
        line = None
        col = None
        for i in range(self.game):
            if k in i:
                line = i
                col = i.index(k)
        
        return ["rigth"]

    def _d(self,k):
        movent = self.detects_possible_movement(k)
        if self.plays_of_disk[k]%2 == 0:
            if k%2 == 0 and  "left" in movent:
                return 1
            if k%2 != 0 and "rigth" in movent:
                return 3
        if self.plays_of_disk[k]%2 != 0:
            if k%2 == 0 and  "rigth" in movent:
                return 1
            if k%2 != 0 and "left" in movent:
                return 3
                
    def _t(self,k):
        if self.move > self.first_movement[k]:
            value = self.move
            while value > self.first_movement[k]:
                value = value - self.plays[k]
            return 1 if value == self.first_movement[k] else 3
        return 1 if self.move == self.first_movement[k] else 3

    def heuristic(self,k):
        return self._d(k) +  self._t(k)



list_open = [] #armazena todas as jogadas possiveis
list_lock = [] #armazena todas as jogodas passadas






import Hanoi_Tower_Searches

matriz_atual = [[1,0,0],          # estado inicial da torre de hanoi
                [2,0,0],
                [3,0,0]]

matriz_Goal = [[0,0,1],           # estado objetivo da torre de hanoi
               [0,0,2],
               [0,0,3]]


Hanoi_Tower_Searches.Depth_Hanoi(matriz_atual, matriz_Goal)
Hanoi_Tower_Searches.Width_Hanoi(matriz_atual, matriz_Goal)
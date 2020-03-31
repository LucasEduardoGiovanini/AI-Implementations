import Hanoi_Tower_Searches , Heuristics,A_star

matriz_atual = [[1,0,0],          # estado inicial da torre de hanoi
                [2,0,0],
                [3,0,0]]

matriz_Goal = [[0,0,1],           # estado objetivo da torre de hanoi
               [0,0,2],
               [0,0,3]]


print("Depth Hanoi Search ----------------")
Hanoi_Tower_Searches.Depth_Hanoi(matriz_atual, matriz_Goal)
print(" ")
print("------------------------------------------------------------------------------------------------")
print(" ")
matriz_atual = [[1,0,0],          # estado inicial da torre de hanoi
                [2,0,0],
                [3,0,0]]

matriz_Goal = [[0,0,1],           # estado objetivo da torre de hanoi
               [0,0,2],
               [0,0,3]]
Hanoi_Tower_Searches.Breadth_Hanoi(matriz_atual, matriz_Goal)
print(" ")
print("busca em largura------------------------------------------------------------------------------------------------")
print(" ")
matriz_atual = [[1,0,0],          # estado inicial da torre de hanoi
                [2,0,0],
                [3,0,0]]

matriz_Goal = [[0,0,1],           # estado objetivo da torre de hanoi
               [0,0,2],
               [0,0,3]]
Hanoi_Tower_Searches.Breadth_Hanoi(matriz_atual, matriz_Goal)
print(" ")
print(" busca gulosa------------------------------------------------------------------------------------------------")
print(" ")
matriz_atual = [[1,0,0],          # estado inicial da torre de hanoi
                [2,0,0],
                [3,0,0]]

matriz_Goal = [[0,0,1],           # estado objetivo da torre de hanoi
               [0,0,2],
               [0,0,3]]
Hanoi_Tower_Searches.Greedy_Hanoi(matriz_atual, matriz_Goal, Heuristics.heuristic_1)
print("")
print("------------------------------------------------------------------------------------------------")
print(" ")


a = int(input())
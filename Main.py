import depth_search

matriz_atual = [[1,0,0],
                [2,0,0],
                [3,0,0]]

matriz_Goal = [[0,0,1],
               [0,0,2],
               [0,0,3]]



depth_search.run(matriz_atual,matriz_Goal)


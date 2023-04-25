import random

n = int(input('digite a dimesao n da matriz'))
m = int(input('digite a dimesao m da matriz'))
matriz = []

    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(random.randint(0, 10))
            matriz.append(linha)
            print(matriz)



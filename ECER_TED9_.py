matriz_5x5 = [
    [1,2 ,3,4,5],
    [1,2 ,3,4,5],
    [1,2 ,3,4,5],
    [1,2 ,3,4,5],
    [1,2 ,3,4,5]
]

for lista in matriz_5x5:
         for item in lista:
    if (item % 2) == 0:
        print(f'Este numero e PAR {item}')
    elif item == 5:
        print(f'Este e o numero cinco - {item}')
    elif (item & 2) !=0:
        print(f' Este numero nao e cinco e e impar {item}')

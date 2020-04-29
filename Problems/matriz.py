# una matriz es un arreglo de arreglos
# en cada posicion del arreglo pongo un arreglo que serian cada columna
# y el numero de afuera son las filas

mat = [ [0] * 10 ] * 5

for i in range(0,5):
    for j in range(0,5):
        print(mat[i][j], end=" ")
    print()
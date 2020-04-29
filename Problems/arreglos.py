#cubeta
#n = int(input())

# crear arreglo tamaño 100 con cero
arr = [0]*100

# leer una cantidad indefinida de elementos en la misma linea
n = int(input())
lista = list( map( int,input().split() ) )

for i in range(0,n):
    print( lista[i] ,end=" ")



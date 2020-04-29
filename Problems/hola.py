#saber si un numero es primo o no
print("Ingresa un numero por favor:")
cont = 0
a = int(input())
for i in range(1,a):
    if a%i==0:
        cont+=1

if cont>1:
    print("No es primo")
else:
    print("Es primo")

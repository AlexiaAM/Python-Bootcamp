
def square(num):
    return num**2

mynums = [1,2,3,4,5,67,8]

#aplicar la funcion para cada uno de mis numeros en mi lista de numeros

for item in map(square,mynums):
    print(item)

#aplicar lo de arriba para convertirlo en una nueva lista

l = list(map(square,mynums))
print(l)


names = ['hola','eve','jeje']

def strings(name):
    if len(name)%2 == 0:
        return 'even'
    else:
        return name[0]

n = list(filter(strings,names))
print(n)

def check(num):
    return num%2 == 0

m = list(filter(square,mynums))
print(m)


#hacer una expresion lamda

squar = lambda num: num**2
print(squar(2))


def invertir(name):
    return name[::-1]

print(invertir('hola'))

invertir = lambda name : name[::-1]
inv = list(map(lambda name: name[::-1],names))

print(inv)
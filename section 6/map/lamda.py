
def square(num):
    result = num**2
    return result

square(4)

mynums = [1,2,3,4,5]

#pasar de una funcion normal a ponerlo como expresion lamda

def square(num): return num ** 2

square = lambda num : n**2

# en combinacion con map

print(list(map(lambda n: n**2,mynums)))
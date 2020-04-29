import random

#for i in range(1,2):
 #   print(random.randint(1,100))

import sys 

#while True:
  #  r = str(input())
   # if r == 'exit':
    #    sys.exit()

#none in other languages is equal to null

def numero(x):
    try:
        return 10/x
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    
print(numero(3))
print(numero(0))
print(numero(1))
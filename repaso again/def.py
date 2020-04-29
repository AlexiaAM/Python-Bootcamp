
# declaration of a function in python

def imprimir():
    print('hello')


# call a function without parameters

imprimir()

# function with parameters

a = 10
b = 3 

def sum(a,b):
    return a + b

# call a function with parameters

print(sum(a,b))

def dog_check (myString):
    if 'dog' in myString:
        return True
    else:
        return False

myString  = 'HEllo, its my dog'

print(dog_check(myString))

# function lower 

myString = myString.lower()

print(myString)

# function in

word = 'my'
if word in myString:
    print('yes')
else:
    print('no')


# encrip something

def pig_latin(word1):

    first_letter = word1[0]
    # check if the first letter is vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word1[1:] + first_letter + 'ay'

    return pig_word

print(pig_latin('word'))

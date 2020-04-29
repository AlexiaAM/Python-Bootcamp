
# args take a arbitrary number of elements

def myfunc(*args):
    return sum(args)


# kwargs

def fruits(**kwargs):
    if 'fruit' in kwargs:
        print('yes {}'.format(kwargs['fruit']))
    else:
        print('no')

fruits(fruit = 'apple')


#combination *args with **kwaargs

def myfuncc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfuncc(10,20,30,fuit = 'hola', food = 'eggs')

mylist = []

def my(*args):
    for item in args:
        if item % 2 == 0:
            mylist.append(item)
my(5,6,7,8)
print(mylist)

word = 'ASkjd'

print(word.upper())

def stringWeird(mystring):

    newSring = ''
    for i in range(0,len(mystring)):
        if(i %2 == 0):
            newSring = newSring + mystring[i].lower()
        else:
            newSring = newSring + mystring[i].upper()
    return newSring

print(stringWeird('hola'))
import sys

while True:
    print('hola')
    name = str(input())
    if name == 'a':
        print('bye')
        sys.exit()
    print('You typed ' + name + '.')

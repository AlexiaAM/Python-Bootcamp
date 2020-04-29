
while True:
    print('nombre?')
    name = str(input())
    if(name != 'alexia'):
        continue
    print('hola alexia, contraseña?')
    password = str(input())
    if(password == 'hola'):
        break

print('listo')
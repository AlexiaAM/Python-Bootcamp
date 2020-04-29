colores = ["rojo", "verde","azul","negro"]

while True:
    print("ingresa un color ... presiona s para salir")
    color = input()

    if color == "s":
        break

    if color in colores:
        print("yes")
    else :
        print("no")
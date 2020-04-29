n = int(input())
cont = 0

animalitos = []
con = 0
dineroDonado = 0

for i in range (0,n):
    animalitos.append( str(input()) )

while True:

    print("Bienvenido al mejor centro de adopción de la ciudad")
    print("(A)Dar en adopción   (B) adoptar animalito   (C)Donar dinero   (D)salir  (M)Mostrar animales disponibles")
    opcion = str(input())
    if opcion == "A" or opcion == "a":
        print("Que animalito quieres dar en adopción?")
        animalitos.append( str(input()) )
        print("Muchas gracias, le conseguiremos el mejor de los hogares, hasta pronto!")
    if opcion == "B" or opcion == "b":
        print("¿Como que animalito te gustaría adoptar?")
        animal = str(input())
        if animal in animalitos:
            print("Si tenemos el animal: " + animal )
            if animal == "perro":
                print("Recomendaciones:")
                print("No olvides darle de comer todos los dias")
                print("bañarlo 1 ves cada dos semanas o cada semana")
                print("y sobre todo, darle mucho pero MUCHO AMOR!!! <3")
            if animal == "gato":
                print("Recomendaciones:")
                print("Darle de comer todos los dias")
                print("Recuerda que los gatitos se bañan solito")
                print("Darle muchisimo AMOR!! <3")
            if animal == "pollo":
                print("Recomendaciones:")
                print("Darle de comer todos los dias, no olvides que son una mascota super chiquita")
                print("pero como toda mascota, tambien necesita de atenciones")
                print("llevarlo al veterinario cada que se enferme")
                print("quererlo demasiado")
            if animal == "leon":
                print("Recomendaciones:")
                print("Como es un animalito que no debe de estar con los humanos")
                print("solamente lo podrás tener los primeros meses de vida")
                print("pues, se deberá de regresar a su habitat natural en donde el bebe león")
                print("estara super feliz, por ultimo no olvides darle todo tu AMOR")
                print("mientras este contigo, muchisima suerte <3")
            animalitos.remove(animal)
            print("Desea hacer algún donativo? SI/NO")
            donativo = str(input())
            if donativo == "SI" or donativo == "si":
                print("Cuanto desea donar?")
                dinero = int(input())
                dineroDonado+=dinero
                print("Muchas gracias por su ayuda!!!")
            else:
                print("Muchas gracias por adoptar un animalito de nuestro refugio!!")
        else:
            for animal in animalitos:
                cont+=1

            if cont!=0:
                print("Lo siento, ya no tenemos el animalito: " + animal + " pero tenemos estos disponibles ")
                for animal in animalitos:
                    print(animal)
                print("desea adoptar alguno ? SI/NO")
                answer = str(input())
                if answer == "SI" or answer == "si":
                    print("QUe animalito desea adoptar?")
                    animalA = str(input())
                    if animalA in animalitos:
                        print("Usted a adoptado: " + animalA)
                        animalitos.remove(animalA)
                if answer == "NO" or answer == "no":
                    print("Hasta luego... <3")
                    break
            else:
                print("lo siento ya no tenemos animalitos disponibles, vuelva pronto")
                break
    if opcion == "C" or opcion == "c":
        print("Cuanto dinero quiere donar?")
        dinero = int(input())
        dineroDonado+=dinero
        print("Muchas gracias por donar, que tenga un bonito día")
        print("Dinero recaudado total: " + str(dineroDonado))
    if opcion == "D" or opcion == "d":
        print("Adios, vuelva pronto")
        break
    if opcion == "M" or opcion == "m":
        print("Animales disponibles en este momento: ")
        for animal in animalitos:
            print(animal)

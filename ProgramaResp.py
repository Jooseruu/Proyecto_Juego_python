import random
import time #Necesitamos las siguientes librerias random para escoger un personaje y time para tener un cronometro y poder crear la ilusión de que la IA piensa
def juego(): 
    Personajes = [["Michael Jackson",  50, 175, "Hombre", "no", "negro"], #Nuestra lista de personajes
                ["Albert Einstein", 76, 160, "Hombre", "gafas", "blanco"],
                ["Nicki Nicole", 22, 145, "Mujer", "sombrero/gorro", "negro"],
                ["Princesa Diana", 36, 170, "Mujer", "pendientes", "rubio"],
                ["Steve Jobs", 56, 168, "Hombre", "gafas", "negro"],
                ["Cristiano Ronaldo", 37, 187, "Hombre", "no", "negro"],
                ["Bad Bunny",  28, 180, "Hombre", "pendientes", "negro"],
                ["Ronnie Coleman", 58, 180, "Hombre", "no", "calvo"],
                ["Reina Letizia", 50, 170, "Mujer", "sombrero/gorro", "castaño"],
                ["Aitana", 23, 160, "Mujer","pendientes", "negro"],
                ["Dwayne Johnson", 50, 196, "Hombre", "no", "calvo"],
                ["Vin Diesel", 55, 182, "Hombre", "no", "calvo"],
                ["Lionel Messi",  35, 169, "Hombre", "no",  "negro"],
                ["Leonardo DiCaprio", 48, 183, "Hombre", "no", "rubio"],
                ["Shakira", 45, 157, "Mujer", "pendientes", "rubio"]]

    print("***********")
    print("|Cargando........|")
    print("***********")

    time.sleep(3)
    
    
    nombre_jugador=input("¿Cuál es tu nombre? " ) #Aquí el jugador introducirá su nombre
    print("Comenzamos a jugar", nombre_jugador, ", buena suerte <3." )

    Personaje= random.choice(Personajes) #Aquí utilizamos random.choice para que escoja uno aleatorio y le indicamos a que posición de la lista corresponden las características de los personajes
    nombre= Personaje[0]
    edad= Personaje[1]
    altura= Personaje[2]
    genero= Personaje[3]
    accesorios= Personaje[4]
    Colordepelo= Personaje[5]

    Número_intentos=0 #Creamos un contador de intentos y generamos el cronometro
    comienzo_tiempo = time.perf_counter()
    
    while True:

        adivina_edad=int(input("¿Qué edad piensas que tiene? ")) #Aquí creamos estas variables que mediante "if" nos dicen si vamos bien o no
        time.sleep(2)
        if adivina_edad==edad:
            print("Sí, correcto!")
        else:
            if edad<adivina_edad: #nos dan pistas en los parametros mas dificiles de acertar
                print("Ala!, no es tan viejo mi personaje")
            else:
                print("Es de una edad mas avanzada que la que me has propuesto")

        adivina_altura= int(input("¿Qué altura tiene mi personaje en cm? "))
        time.sleep(2)

        if adivina_altura==altura:
            print("Sí, correcto!")
        else:
            if altura<adivina_altura:
                print("Es más bajito el personaje escogido por mi ;)")

            else: 
                print("Es más alto mi personaje")

        adivina_genero= input("¿Qué genero es? ")
        adivina_genero= adivina_genero.title() #Aquí lo pasamos a title para que salga igual que en nuestros parametros de personajes
        time.sleep(2)
        if adivina_genero==genero:
            print("Claro que sí!", nombre_jugador)
        else:
            print("No, es", genero)

        adivina_accesorios= input("¿Que accesorios tiene si es que los tiene? ")
        adivina_accesorios=adivina_accesorios.lower() #Lo mismo aquí para que salga igual que en nuestros parametros
        time.sleep(2)

        if adivina_accesorios==accesorios:
            print("Sí, correcto como siempre!")
        else:
            print("No, te has equivocado", nombre_jugador)

        adivina_Colordepelo= input("¿Qué Color de pelo tiene? ")
        adivina_Colordepelo=adivina_Colordepelo.lower()
        time.sleep(2)
        if adivina_Colordepelo==Colordepelo:
            print("Sí, correctísimo!")
        else:
            print("No, te has equivocado, más suerte la proxima", nombre_jugador)

        adivina= input("¿Quién piensas que es? ")
        adivina= adivina.title()
        time.sleep(2)
        if adivina==nombre:
            final_tiempo = time.perf_counter() #Justo aqí paramos el cronometro y hacemos la resta para que nos quede el tiempo
            durante_tiempo = final_tiempo - comienzo_tiempo
            print("Felicidades has acertado!!!")
            time.sleep(2)
            print(" ") #Priteamos el contador y el tiempo de juego
            print("----Estadísticas----")
            print(" ")
            time.sleep(1)
            print("El número de intentos extras realizado para adivinar el personaje ha sido de",Número_intentos)
            print("Tiempo de juego: {:.2f} segundos.".format(durante_tiempo)) 
            break
        else:
            Número_intentos += 1 #En caso de no acertar sumaremos 1 a los intentos
            Resultado= input("No!!!,¿Desea volver a intentarlo? seguirá siendo el mismo personaje(s/n)  ") #Mediante un while podemos volver a intentarlo
            if Resultado =="n":
                print(" ")
                print("Más suerte la próxima, se trataba de: " + nombre)
                final_tiempo = time.perf_counter()
                durante_tiempo = final_tiempo - comienzo_tiempo
                time.sleep(2)
                print(" ")
                print("----Estadísticas----")
                print(" ")
                time.sleep(1)
                print("El número de intentos realizado ha sido de",Número_intentos)
                print("Tiempo de juego: {:.2f} segundos.".format(durante_tiempo))
                break
juego()

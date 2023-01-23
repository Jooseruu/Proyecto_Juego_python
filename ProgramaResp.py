import random
import time
Personajes = [["Michael Jackson",  50, 175, "Hombre", "no", "negro"],
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

print("*******************************")
print("|Cargando........|")
print("*******************************")

time.sleep(3)
 
 
nombre_jugador=input("¿Cuál es tu nombre? " )
print("Comenzamos a jugar", nombre_jugador, ", buena suerte <3." )

Personaje= random.choice(Personajes)
nombre= Personaje[0]
edad= Personaje[1]
altura= Personaje[2]
genero= Personaje[3]
accesorios= Personaje[4]
Colordepelo= Personaje[5]

Número_intentos=0
comienzo_tiempo = time.perf_counter()
while True:

 adivina_edad=int(input("¿Qué edad piensas que tiene? "))
 time.sleep(2)
 if adivina_edad==edad:
    print("Sí, correcto!")
 else:
    if edad<adivina_edad:
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
 adivina_genero= adivina_genero.title()
 time.sleep(2)
 if adivina_genero==genero:
    print("Claro que sí!", nombre_jugador)
 else:
    print("No, es", genero)

 adivina_accesorios= input("¿Que accesorios tiene si es que los tiene? ")
 adivina_accesorios=adivina_accesorios.lower()
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
    final_tiempo = time.perf_counter()
    durante_tiempo = final_tiempo - comienzo_tiempo
    print("Felicidades has acertado!!!")
    time.sleep(2)
    print(" ")
    print("El número de intentos extras realizado para adivinar el personaje ha sido de",Número_intentos)
    print("Tiempo de juego: {:.2f} segundos.".format(durante_tiempo))
    break
 else:
    Número_intentos += 1
    Resultado= input("No!!!,¿Desea volver a intentarlo? seguirá siendo el mismo personaje(s/n)  ")
    if Resultado =="n":
     print(" ")
     print("Más suerte la próxima, se trataba de: " + nombre)
     final_tiempo = time.perf_counter()
     durante_tiempo = final_tiempo - comienzo_tiempo
     time.sleep(2)
     print("El número de intentos realizado ha sido de",Número_intentos)
     print("Tiempo de juego: {:.2f} segundos.".format(durante_tiempo))
     break

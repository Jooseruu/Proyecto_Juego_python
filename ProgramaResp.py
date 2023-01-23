import random
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
              ["Dwayne Douglas Johnson", 50, 196, "Hombre", "no", "calvo"],
              ["Vin Diesel", 55, 182, "Hombre", "no", "calvo"],
              ["Lionel Messi",  35, 169, "Hombre", "no",  "negro"],
              ["Leonardo DiCaprio", 48, 183, "Hombre", "no", "rubio"],
              ["Shakira", 45, 157, "Mujer", "pendientes", "rubio"]]

print("-------------------------------")
print("Bienvenido a Quien es Quien!")
print("-------------------------------")
 
 
nombre_jugador=input("¿Cual es tu nombre?" )
print("Vamos a empezar a jugar", nombre_jugador, ", buena suerte <3." )

Personaje= ["Vin Diesel", 55, 182, "Hombre", "no", "calvo"]
Personaje= random.choice(Personajes)
nombre= Personaje[0]
edad= Personaje[1]
altura= Personaje[2]
genero= Personaje[3]
accesorios= Personaje[4]
Colordepelo= Personaje[5]

print("El nombre es:", nombre)
print("La edad es:", edad)
print("La altura en cm es:", altura)
print("Es:", genero)
print("Usa algun accesorio:", accesorios)
print("Su pelo es:", Colordepelo)

adivina_edad=int(input("¿Que edad piensas que tiene?"))
if adivina_edad==edad:
    print("Sí, correcto!")
else:
    if edad<adivina_edad:
        print("Ala!, no es tan viejo mi personaje")
    else:
        print("Es de una edad mas avanzada que la que me has propuesto")

adivina_altura= int(input("¿Que altura tiene en cm?"))
if adivina_altura==altura:
    print("Sí, correcto!")
else:
    if altura<adivina_altura:
        print("Es mas bajito el personaje escogido por mi ;)")

    else: 
        print("Es más alto mi personaje")

adivina_genero= input("¿Que genero es?")
adivina_genero= adivina_genero.title()
if adivina_genero==genero:
    print("Claro que sí!", nombre_jugador)
else:
    print("No, es", genero)

adivina_accesorios= input("¿Que accesorios tiene si es que los tiene?")
adivina_accesorios=adivina_accesorios.lower()
if adivina_accesorios==accesorios:
    print("Sí, correcto como siempre!")
else:
    print("No, te has equivocado", nombre_jugador)

adivina_Colordepelo= input("¿Que Color de pelo tiene?")
adivina_Colordepelo=adivina_Colordepelo.lower()
if adivina_Colordepelo==Colordepelo:
    print("Sí, correctísimo!")
else:
    print("No, te has equivocado, más suerte la proxima", nombre_jugador)

adivina= input("¿Quien piensas que es? ")
adivina= adivina.title()
if adivina==nombre:
    print("Felicidades has acertado!!!")
else:
    print("Más suerte la próxima, se trataba de:" + nombre)

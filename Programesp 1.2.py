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
print("Su pelo es:", nombre)




print("La altura en cm es:", altura)
print("Es:", genero)
print("Usa algun accesorio:", accesorios)
print("Su pelo es:", nombre)
print("Su pelo es:", Colordepelo)

adivina_edad= input("¿Que edad piensas que tiene?")
if adivina_edad==edad:
    print("Sí, correcto!")
else:
    print("No, no tiene esa edad")

adivina= input("¿Quien piensas que es? ")
adivina= adivina.title()
if adivina==nombre:
    print("Felicidades has acertado!!!")
else:
    print("Más suerte la próxima, se trataba de:" + nombre)
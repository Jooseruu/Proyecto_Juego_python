import random
import time
def juego():
    Characters = [
        ["Michael Jackson",  50, 175, "Male", "none", "black"],
        ["Albert Einstein", 76, 160, "Male", "glasses", "white"],
        ["Nicki Nicole", 22, 145, "Female", "hat", "black"],
        ["Princesa Diana", 36, 170, "Female", "earrings", "blond"],
        ["Steve Jobs", 56, 168, "Male", "glasses", "black"],
        ["Cristiano Ronaldo", 37, 187, "Male", "none", "black"],
        ["Bad Bunny",  28, 180, "Male", "earrings", "black"],
        ["Ronnie Coleman", 58, 180, "Male", "none", "bald"],
        ["Reina Letizia", 50, 170, "Female", "hat", "brown"],
        ["Aitana", 23, 160, "Female","earrings", "black"],
        ["Dwayne Johnson", 50, 196, "Male", "none", "bald"],
        ["Vin Diesel", 55, 182, "Male", "none", "bald"],
        ["Lionel Messi",  35, 169, "Male", "none",  "black"],
        ["Leonardo DiCaprio", 48, 183, "Male", "none", "blond"],
        ["Shakira", 45, 157, "Female", "earrings", "blond"]]

    print("*******************************")
    print("|Loading........|")
    print("*******************************")

    time.sleep(3)
    
    
    nombre_jugador=input("What is your name? " )
    print("Let's play", nombre_jugador,", Good luck have fun <3." )

    Personaje= random.choice(Characters)
    nombre= Personaje[0]
    edad= Personaje[1]
    altura= Personaje[2]
    genero= Personaje[3]
    accesorios= Personaje[4]
    Colordepelo= Personaje[5]

    Número_intentos=0
    comienzo_tiempo = time.perf_counter()
    
    while True:

        adivina_edad=int(input("How old do you think is? "))
        time.sleep(2)
        if adivina_edad==edad:
            print("Yes, OMG!")
        else:
            if edad<adivina_edad:
                print("Noo!, my character is not that old.")
            else:
                print("He/She is of a more advanced age than you have said.")

        adivina_altura= int(input("How tall you think is my character in cm? "))
        time.sleep(2)

        if adivina_altura==altura:
            print("It's correct!")
        else:
            if altura<adivina_altura:
                print("The character chosen by me is shorter ;)")

            else: 
                print("The character I'm thinking of is taller. ")

        adivina_genero= input("What gender do you think it is? ")
        adivina_genero= adivina_genero.title()
        time.sleep(2)
        if adivina_genero==genero:
            print("Of course",nombre_jugador,"!")
        else:
            print("Noup, he/she is",genero)

        adivina_accesorios= input("What accessories does it have, if any? ")
        adivina_accesorios=adivina_accesorios.lower()
        time.sleep(2)

        if adivina_accesorios==accesorios:
            print("Yes, good answer!")
        else:
            print("Nice try but not correct", nombre_jugador)

        adivina_Colordepelo= input("What color hair does the character have? ")
        adivina_Colordepelo=adivina_Colordepelo.lower()
        time.sleep(2)
        if adivina_Colordepelo==Colordepelo:
            print("Correct, you almost got it!")
        else:
            print("Oupss, you're wrong", nombre_jugador)

        adivina= input("Who do you think it is? ")
        adivina= adivina.title()
        time.sleep(2)
        if adivina==nombre:
            final_tiempo = time.perf_counter()
            durante_tiempo = final_tiempo - comienzo_tiempo
            print("Congratulations you guessed it!!!")
            time.sleep(2)
            print(" ")
            print("----Scoreboard----")
            print(" ")
            time.sleep(1)
            print("The number of extra attempts to guess the character has been ",Número_intentos)
            print("Game time: {:.2f} seconds.".format(durante_tiempo))
            break
        else:
            Número_intentos += 1
            Resultado= input("Oh no, you have failed!!!, Do you want to try again? It will still be the same character that I'm thinking (Y/n)  ")
            if Resultado =="n":
                print(" ")
                print("More luck next time, my character was " + nombre)
                final_tiempo = time.perf_counter()
                durante_tiempo = final_tiempo - comienzo_tiempo
                time.sleep(2)
                print(" ")
                print("----Scoreboard----")
                print(" ")
                time.sleep(1)
                print("The number of extra attempts to guess the character has been",Número_intentos)
                print("Game time: {:.2f} seconds.".format(durante_tiempo))
                break
juego()
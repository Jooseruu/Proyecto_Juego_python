import random 
import time
def menu():

    def idioma():      #definimos el menu de seleccion de idioma como una funcion y lo decoramos
        print("************************************************")
        print("*     Bienvenido al juego ¿Quién es Quién?     *")
        print("*            Selecciona el idioma              *")
        print("*----------------------------------------------*")
        print("*  Para jugar en español (España) introduce 1  *")
        print("*                                              *")
        print("*  Para jugar en inglés (English) introduce 2  *")
        print("************************************************")
        idiomasele= input("Selecciona el idioma en el que quieres jugar: ")  
        return idiomasele  #la funcion retornará el idioma que eliga el usuario

    while True:   #creamos un bucle para mostrar un menú u otro
        idiomasele=idioma()
        if idiomasele=="1":
            print(" ")
            print("Has elegido jugar en Español")
            print(" ")
            def esp():
                def menuprincipalesp():
                    print("*******************************************")
                    print("*   Bienvenido al juego ¿Quién es Quién?  *")
                    print("*-----------------------------------------*")
                    print("*        Introduce 1 para Jugar           *")
                    print("*                                         *")
                    print("*  Introduce 2 para ver las Instrucciones *")
                    print("*                                         *")
                    print("*        Introduce 3 para Salir           *")
                    print("*******************************************")
                    opcion = input("Seleccione una opción: ")
                    return opcion   #la función devuelve el valor de la opcion que de el usuario

                def jugar():      
                # código para iniciar el juego
                    #Necesitamos las siguientes librerias random para escoger un personaje y time para tener un cronometro y poder crear la ilusión de que la IA piensa
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
                    
                while True:
                    opcion = menuprincipalesp()
                    if opcion == "1": #si elige 1 se iniciara el juego
                        jugar()  
                        break
                    elif opcion == "2": #si elige 2 se mostrarán las instrucciones y volverá a salir el menú principal.
                        print("-------------------Instrucciones del juego-------------------\nEl juego consiste en adivinar el personaje que está pensando la IA (Inteligencia Artifical) mediante preguntas.\nLas preguntas te las irá diciendo la IA y tú responderás, en el caso de los accesorios necesitas saber que hay 3:\npendientes, sombrero/gorro, gafas o ninguno (no).\nLa dificultad del juego trata en adivinarlo en el menor tiempo posible e intentar no hacer muchos fallos.\nAl final de la partida se mostrarán las estadísticas con el tiempo de juego y el número de intentos totales.\nPara empezar a jugar debes introducir un nombre de ususario y a continuación el programa elegirá un personaje al azar.\nEs necesario descargarse un archivo jpg ubicado en el github para poder ver los personajes y sus características, ¡Buena Suerte!.\n-------------------------------------------------------------")
                    elif opcion == "3": #si elige 3 se saldra del juego
                        print("Has salido del programa.")
                        break
                    else:
                        print("Opción no válida. Por favor seleccione una opción válida...")
                        print(" ")
            esp()
            break

        elif idiomasele=="2":
            print(" ")
            print("You have chosen to play in English")
            print(" ")
            def eng():
                def menuprincipaleng():
                    print("*******************************************")
                    print("*     Welcome to the game Guess Who?      *")
                    print("*-----------------------------------------*")
                    print("*            Enter 1 to Start             *")
                    print("*                                         *")
                    print("*      Enter 2 to view instructions       *")
                    print("*                                         *")
                    print("*        Enter 3 to exit the game         *")
                    print("*******************************************")
                    option = input("Choose an option: ")
                    return option   #la función devuelve el valor de la opcion que de el usuario

                def play():      
                # código para iniciar el juego
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
                while True:
                    option = menuprincipaleng()
                    if option == "1": #si elige 1 se iniciara el juego
                        play()  
                        break
                    elif option == "2": #si elige 2 se mostrarán las instrucciones y volverá a salir el menú principal.
                        print("-------------------Game instructions--------------------\nThe game consists of guessing the character that the AI (Artificial Intelligence) is thinking through questions.\nThe questions will be told by the AI and you will answer, in the case of accessories you need to know that there are 3:\nearrings, hat , glasses or none.\nThe difficulty of the game is about guessing it in the shortest time possible and trying not to make too many mistakes.\nAt the end of the game the statistics will be shown with the playing time and the number of total attempts.\nTo start playing you must enter a username and then the program will choose a random character.\nYou need to download a jpg file located on github to see the characters and their characteristics, Good Luck!.\n-------------------------------------------------------------")
                    elif option == "3": #si elige 3 se saldrá del programa.
                        print("You have exited the program.")
                        break
                    else:  #si pone un caracter no valido le avisará
                        print("Invalid option. Please select a valid option.")
                        print(" ")
            eng()
            break

        else:    #si no pone una opcion valida avisará
            print(" ")
            print("No has introducido una opción válida, vuelve a intentarlo...")

menu()       
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
                    print("Iniciando juego...")
                    
                while True:
                    opcion = menuprincipalesp()
                    if opcion == "1": #si elige 1 se iniciara el juego
                        jugar()  
                        break
                    elif opcion == "2": #si elige 2 se mostrarán las instrucciones y volverá a salir el menú principal.
                        print("-------------------Instrucciones del juego-------------------\nEl juego consiste en adivinar el personaje que esta pensando la IA (Inteligencia Artifical) mediante preguntas.\nLas respuestas de las preguntas solo serán de si o no y no se darán más pistas. \nLa dificultad del juego trata en adivinarlo en el menor tiempo posible y no tener más de tres fallos.\nPara ello debes introducir un nombre de ususario y a continuación el programa elegirá un personaje al azar.\nEs necesario descargarse un archivo png ubicado en el github para poder ver los personajes y sus características, ¡Buena Suerte!.\n-------------------------------------------------------------")
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
                    print("Starting game...")
                            
                while True:
                    option = menuprincipaleng()
                    if option == "1": #si elige 1 se iniciara el juego
                        play()  
                        break
                    elif option == "2": #si elige 2 se mostrarán las instrucciones y volverá a salir el menú principal.
                        print("-------------------Game instructions--------------------\nThe game consists of guessing the character that The AI (Artificial Intelligence) through questions.\nThe answers to the questions will only be yes or no and no further clues will be given. \nThe difficulty of the game is about guessing it in the shortest time possible and not having more than three mistakes.\nTo do this you must enter a username and then the program will choose a character at random.\nIt is necessary to download a png file located in the github to see the characters and their characteristics, Good Luck!.\n---------------------------------------------------------------")
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
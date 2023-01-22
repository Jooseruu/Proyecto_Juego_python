def esp():
    def menuprincipalesp():
        print("Bienvenido al juego ¿Quién es Quién?")
        print("Introduce 1 para Jugar")
        print("Introduce 2 para ver las Instrucciones")
        print("Introduce 3 para Salir")
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
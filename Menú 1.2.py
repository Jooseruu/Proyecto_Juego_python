def eng():
    def menuprincipaleng():
            print("Welcome to the game Who's Who?")
            print("Enter 1 to play")
            print("Enter 2 to see instructions")
            print("Enter 3 to exit the game")
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
        else:
            print("Invalid option. Please select a valid option.")
            print(" ")
eng()
def menuprincipal():
    print("Bienvenido al juego ¿Quién es Quién?")
    print("Introduce 1 para Jugar")
    print("Introduce 2 para ver las Instrucciones")
    print("Introduce 3 para Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def jugar():
    print("Para empezar a jugar debes de elegir el modo de juego que quieres.\nEscribe 1 para jugar contra la IA \nEscribe 2 para jugar con otro jugador ")
    Modo_de_Juego=int(input())
    if Modo_de_Juego==1:
        print("Has elegido jugar contra la IA. ¡Buena Suerte!")
    elif Modo_de_Juego==2:
        print("Has elegido jugar contra otra persona. ¡Buena suerte a los dos!")
    else:
        print("Has introducido un modo no válido para jugar, inténtalo de nuevo:")
        Modo_de_Juego=int(input())
        
    # código para iniciar el juego
    print("Iniciando juego...")
    

def instrucciones():
    # código para mostrar las instrucciones
    print("Instrucciones del juego...")

while True:
    opcion = menuprincipal()
    if opcion == "1":
        jugar()
        break
    elif opcion == "2":
        instrucciones()
        break
    elif opcion == "3":
        print("Has salido del programa.")
        break
    else:
        print("Opción no válida. Por favor seleccione una opción válida.")
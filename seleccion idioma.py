def selector():
    def idioma():
        print("Para jugar en español (España) introduce 1\nPara jugar en inglés (English) introduce 2")
        idiomasele= input("Selecciona el idioma en el que quieres jugar: ")
        return idiomasele

    while True:
        idiomasele=idioma()
        if idiomasele=="1":
            print(" ")
            print("Has elegido jugar en Español")
            break
        elif idiomasele=="2":
            print(" ")
            print("You have chosen to play in English")
            break
        else:
            print(" ")
            print("No has introducido una opción válida, vuelve a intentarlo...")
selector()


        
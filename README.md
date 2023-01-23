# GUESS WHO?
Primer proyecto python del módulo DAW. Autores: Rubén Arjona y Alejandro Roca

## Objetivos
Lo más importante de este proyecto, es aplicar los conocimientos adquiridos durante todo este curso sobre el lenguaje Python, para poder realizar de la mejor manera un juego.

## El juego
El juego que hemos escogido ha sido el Guess Who? o ¿Quién es quién? Lo hemos escogido porque haciendo un estudio de lo que tendríamos que tener en cuenta, nos pareció un juego relativamente sencillo de realizar, adecuado para nuestro nivel de Python.

### Estructura del juego
La estructura del juego se compone de 3 fases: Comprender el juego, Diseñar el Juego, Codificar y Revisar.

### Primera fase
En la primera fase buscaremos información sobre el juego, necesitamos saber jugar para saber programarlo, necesitamos conocer sus normas y sus formas de jugar y en base a esto desarrollaremos un pseudocódigo para lograr tener una primera idea de cómo debería diseñarse.


### Segunda fase
Aquí se implementa la información anterior, debemos desarrollar un pseudocódigo para Python ya que es el lenguaje de programación que usaremos, a partir de esto podremos conocer las funciones de nuestro programa inicial.


### Tercera fase
En esta fase codificaremos el juego se hará un fichero main donde se plasmará el juego al completo con este escrito y un jpg con las fichas
necesarias para el juego, gracias a las herramientas git podremos trabajar en distintas ramas al mismo tiempo sin necesidad de coordinarnos
excesivamente, podremos realizar adecuadamente un control de versiones entre otras funcionalidades. Durante la revisión nos dedicaremos a poner a
prueba el juego probando sus funcionalidades y provocando errores con tal de mejorar nuestro programa.



# Documento del juego

El juego consiste en adivinar el personaje que está pensando la IA (Inteligencia Artificial) mediante preguntas. Las preguntas te las irá diciendo la IA y tú responderás, en el caso de los accesorios necesitas saber que hay 3:pendientes, sombrero/gorro, gafas o ninguno (no).

La dificultad del juego trata en adivinarlo en el menor tiempo posible e intentar no cometer muchos fallos. Al final de la partida se mostrarán las estadísticas con el tiempo de juego y el número de intentos totales.

Para empezar a jugar debes introducir un nombre de usuario y a continuación el programa elegirá un personaje al azar. Es necesario descargarse un archivo jpg ubicado en el github para poder ver los personajes y sus características.


# Documento Diseño Inicial

Hay una función que te imprime un menú, tendrás que escoger entre el inglés o el español y a partir de ahí se genera un menú con 3 opciones 
1-Jugar 
2-Instrucciones
3-Salir







# Documento de codificación y desarrollo
## División
Hemos dividido el juego en 3 partes:
1-Menú
 1.1-Interfaz: Se define como menú esto es más lo visual(nos permite escoger idioma)
 ~~~
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
~~~

2-Personajes: Funciona mediante posiciones, es necesario para jugar
~~~
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
~~~

3-Juego 
3.1-Estructura: Funciona en gran parte mediante estructuras "if"
~~~
     if adivina_altura==altura:
                                print("Sí, correcto!")
                            else:
                                 if altura<adivina_altura:
                                 print("Es más bajito el personaje escogido por mi ;)")

                                else: 
                                    print("Es más alto mi personaje")
~~~
3.2-Contadores y Timers: Usados para poder visualizar los intentos y el tiempo
~~~
     Número_intentos=0 #Creamos un contador de intentos y generamos el cronometro
     comienzo_tiempo = time.perf_counter()
     durante_tiempo = final_tiempo - comienzo_tiempo
~~~
     

# Documento de test de errores
### Fallo:
~~~
Coge mal los valores y los da como incorrectos
~~~
### Solución:
.lower hace que se corresponda con las mayusculas de nuestra lista
~~~
adivina_Colordepelo= input("¿Qué Color de pelo tiene? ")
                            adivina_Colordepelo=adivina_Colordepelo.lower()
                            time.sleep(2)
                            if adivina_Colordepelo==Colordepelo:
                                print("Sí, correctísimo!")
                            else:
                                print("No, te has equivocado, más suerte la proxima", nombre_jugador)
~~~

### Fallo:
~~~
No printea correctamente el tiempo
~~~
### Solución:
Utilizamos .format para solucionarlo
~~~
print("Tiempo de juego: {:.2f} segundos.".format(durante_tiempo))
~~~


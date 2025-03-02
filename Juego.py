# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

"""Inicializa las variables y estructuras de datos necesarias para el juego.

    Esta función configura el juego piedra, papel o tijera, inicializando el modo de juego,
    el histórico de juegos y las estadísticas de los jugadores y la computadora.

    Variables:
        modo_juego (int): 0 indica que el juego no ha comenzado.
        historico_juegos (list): Lista para almacenar el resultado de cada juego.
        estadisticas (dict): Diccionario para almacenar las estadísticas de cada jugador
                             y la computadora, incluyendo juegos ganados, perdidos y empatados.

    Módulos:
        random: Se utiliza para generar elecciones aleatorias para la computadora.
        getpass: Se utiliza para ocultar la entrada del jugador en ciertos modos de juego.
    """


import random   # Se utiliza para generar elecciones aleatorias para la computadora.
import getpass  # Importa el módulo getpass para ocultar la entrada

modo_juego = 0

# Variables para almacenar el histórico y las estadísticas del juego
historico_juegos = []
estadisticas = {
    "jugador1": {"ganadas": 0, "perdidas": 0, "empatadas": 0},
    "jugador2": {"ganadas": 0, "perdidas": 0, "empatadas": 0},
    "computadora": {"ganadas": 0, "perdidas": 0, "empatadas": 0},
}


def manejar_opcion(opcion):

    """Maneja la opción seleccionada por el usuario en el menú principal.

    Esta función recibe la opción elegida por el usuario y ejecuta la acción
    correspondiente.  Las opciones disponibles son:

    1. Página de inicio: Muestra un mensaje indicando la página de inicio.
    2. Configuración del juego: Muestra un mensaje indicando la configuración del juego.
    3. Perfil de usuario: Muestra un mensaje indicando el perfil de usuario.
    4. Iniciar juego: Inicia el juego, reinicia las estadísticas y el histórico,
                      y muestra el menú de modos de juego.
    5. Histórico y estadísticas: Muestra el histórico y las estadísticas de juego.
    6. Hasta luego: Finaliza el programa.

    Cualquier otra opción se considera inválida y se muestra un mensaje de error.

    Args:
        opcion (int): El número de la opción seleccionada por el usuario.

    Returns:
        bool: True si la opción es válida y no es la de salida (opción 6), False si la opción es inválida.
              Si la opción es la de salida (6), también retorna True, pero el programa principal debería terminar.

    Variables globales utilizadas:
        historico_juegos (list): Lista que almacena el histórico de los juegos. Se reinicia al iniciar un nuevo juego.
        estadisticas (dict): Diccionario que almacena las estadísticas de los jugadores y la computadora. Se reinicia al iniciar un nuevo juego.

    Funciones llamadas:
        mostrar_menu_modos_juego(): Muestra el menú para seleccionar el modo de juego.
        mostrar_historico_estadisticas(): Muestra el histórico y las estadísticas del juego.   
    """
    
    if opcion == 1:
        print("¡Página de inicio!")

    elif opcion == 2:
        print("¡Configuración del juego!")

    elif opcion == 3:
        print("¡Perfil de usuario!")

    elif opcion == 4:
        print("¡Iniciar juego!")
        historico_juegos.clear()
        estadisticas.update({
            "jugador1": {"ganadas": 0, "perdidas": 0, "empatadas": 0},
            "jugador2": {"ganadas": 0, "perdidas": 0, "empatadas": 0},
            "computadora": {"ganadas": 0, "perdidas": 0, "empatadas": 0},
        })
        
        mostrar_menu_modos_juego()  # Muestra el menú de modos de juego
        return True

    elif opcion == 5:
        print("¡Histórico y estadísticas!")
        mostrar_historico_estadisticas()  # Llamar a la función para mostrar el histórico y las estadísticas
        return True

    elif opcion == 6:
        print("¡Hasta luego!")
        return True

    else:
        print("Opción inválida. Por favor, elige una opción del menú.")

    return False

def mostrar_menu_modos_juego():
    
    """Muestra el menú de modos de juego y maneja la selección del usuario.

    Esta función presenta al usuario las opciones de modos de juego disponibles:
    1. Usuario vs Computadora
    2. Multijugador (Usuario vs Usuario)
    3. Regresar al menú principal

    El usuario debe ingresar el número correspondiente al modo de juego deseado.
    Se manejan errores de entrada (valores no numéricos y opciones inválidas)
    y se vuelve a pedir la entrada hasta que sea válida.

    Variables globales utilizadas:
        modo_juego (int): Almacena el modo de juego seleccionado por el usuario.
                          Se modifica dentro de esta función.

    Funciones llamadas:
        mostrar_reglas_usuario_vs_computadora(): Muestra las reglas del modo Usuario vs Computadora.
        jugar_usuario_vs_computadora(): Inicia el juego en modo Usuario vs Computadora.
        mostrar_reglas_multijugador(): Muestra las reglas del modo Multijugador.
        jugar_multijugador(): Inicia el juego en modo Multijugador.
        main(): Regresa al menú principal del juego. 
    """
    
    global modo_juego
    print("\n--- Modos de juego ---")
    print("1. Usuario vs Computadora")
    print("2. Multijugador (Usuario vs Usuario)")
    print("3. Regresar al menú principal")

    while True:
        try:
            modo_juego = int(input("Ingresa el número del modo de juego: "))
            if modo_juego in [1, 2, 3]:
                break
            else:
                print("Opción inválida. Por favor, elige 1,2 o 3.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

    if modo_juego == 1:
        mostrar_reglas_usuario_vs_computadora()
        jugar_usuario_vs_computadora()
    elif modo_juego == 2:
        mostrar_reglas_multijugador()
        jugar_multijugador()
    elif modo_juego == 3:  # Regresar al menú principal
        main()    
        

def mostrar_reglas_usuario_vs_computadora():
    
    """Muestra las reglas del juego Piedra, Papel o Tijera en la modalidad Usuario vs Computadora.

    Esta función imprime en la consola las reglas generales del juego, así como las reglas
    específicas para la modalidad Usuario vs Computadora.

    Reglas Generales:
        - La piedra aplasta la tijera (la piedra gana).
        - La tijera corta el papel (la tijera gana).
        - El papel envuelve la piedra (el papel gana).
        - Si ambos jugadores eligen la misma opción, es un empate.

    Reglas modalidad Usuario vs Computadora:
        - El usuario elige una de las tres opciones (piedra, papel o tijera).
        - La computadora elige aleatoriamente una de las tres opciones.
        - Se comparan las elecciones y se determina el resultado según las reglas generales.
    """
    
    print("Bienvenido al juego de piedra, papel o tijera modalidad usuario vs computadora.")
    print("Reglas Generales:")
    print("·\tLa piedra aplasta la tijera (la piedra gana).")
    print("·\tLa tijera corta el papel (la tijera gana).")
    print("·\tEl papel envuelve la piedra (el papel gana).")
    print("·\tSi ambos jugadores eligen la misma opción, es un empate.")
    print("Reglas modalidad Usuario vs Computadora:")
    print("·\tEl usuario elige una de las tres opciones (piedra, papel o tijera).")
    print("·\tLa computadora elige aleatoriamente una de las tres opciones.")
    print("·\tSe comparan las elecciones y se determina el resultado según las reglas generales.")

def mostrar_reglas_multijugador():
    
    """Muestra las reglas del juego Piedra, Papel o Tijera en la modalidad Multijugador (Usuario vs Usuario).

    Esta función imprime en la consola las reglas generales del juego, así como las reglas
    específicas para la modalidad Multijugador (Usuario vs Usuario).

    Reglas Generales:
        - La piedra aplasta la tijera (la piedra gana).
        - La tijera corta el papel (la tijera gana).
        - El papel envuelve la piedra (el papel gana).
        - Si ambos jugadores eligen la misma opción, es un empate.

    Reglas modalidad Multijugador (Usuario vs Usuario):
        - Dos jugadores se enfrentan.
        - Ambos jugadores eligen simultáneamente una de las tres opciones (piedra, papel o tijera).
        - Se comparan las elecciones y se determina el resultado según las reglas generales.
    """
    
    print("Bienvenido al juego de piedra, papel o tijera modalidad multijugador")
    print("Reglas Generales:")
    print("·\tLa piedra aplasta la tijera (la piedra gana).")
    print("·\tLa tijera corta el papel (la tijera gana).")
    print("·\tEl papel envuelve la piedra (el papel gana).")
    print("·\tSi ambos jugadores eligen la misma opción, es un empate.")
    print("Reglas modalidad Multijugador Usuario vs Usuario:")
    print("·\tDos jugadores se enfrentan.")
    print("·\tAmbos jugadores eligen simultáneamente una de las tres opciones (piedra, papel o tijera).")
    print("·\tSe comparan las elecciones y se determina el resultado según las reglas generales.")



def jugar_usuario_vs_computadora():
    
    """Implementa el juego Piedra, Papel o Tijera en la modalidad Usuario vs Computadora.

    Esta función permite al usuario jugar contra la computadora.  El usuario puede elegir
    jugar un número definido de partidas o jugar libremente hasta que decida no seguir jugando.
    Se registran las estadísticas de cada partida y se muestra un resumen al final.

    Flujo del juego:
        1.  El usuario ingresa su nombre.
        2.  Se pregunta si desea definir un número de partidas.
        3.  Si el usuario define un número de partidas, se valida la entrada.
        4.  Comienza el bucle principal del juego.
        5.  Dentro del bucle, se juega cada partida:
            a.  La computadora elige su opción aleatoriamente.
            b.  El usuario elige su opción (se valida la entrada).
            c.  Se muestran las opciones de ambos jugadores.
            d.  Se determina el ganador según las reglas del juego.
            e.  Se actualizan las estadísticas.
            f.  Se añade la información de la partida al histórico.
        6.  Si se definió un número de partidas, se pregunta si quiere volver a jugar con el mismo número de partidas.
        7.  Si no se definió un número de partidas, se pregunta si quiere jugar otra partida.
        8.  Si el usuario no quiere seguir jugando, se muestran las estadísticas y el histórico, y se regresa al menú principal.

    Variables globales utilizadas:
        estadisticas (dict):  Diccionario que almacena las estadísticas del juego. Se modifica dentro de esta función.
        historico_juegos (list): Lista que almacena el histórico de las partidas jugadas. Se modifica dentro de esta función.
        main (function): Función que representa el menú principal del juego. Se llama al finalizar la partida.
        mostrar_historico_estadisticas (function): Función que muestra el histórico y las estadísticas. Se llama al finalizar la partida.
        random (module): Módulo utilizado para la elección aleatoria de la computadora.

    """
    
    nombre_jugador = input("Ingresa tu nombre: ")

    # Preguntar si desea definir número de partidas
    while True:
        definir_partidas = input("¿Desea definir un número de partidas a jugar? (si/no): ").lower()
        if definir_partidas in ["si", "no"]:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    if definir_partidas == "si":
        while True:
            try:
                num_partidas = int(input("Ingrese el número de partidas a jugar: "))
                if num_partidas > 0:
                    break
                else:
                    print("Número de partidas inválido. Debe ser mayor que cero.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
        num_partidas_inicial = num_partidas  # Guarda el número inicial de partidas
    else:
        num_partidas = None

    while True:  # Bucle principal para controlar si se juega de nuevo
        partidas_jugadas = 0
        opciones = ["piedra", "papel", "tijera"]

        # Bucle para jugar partidas (modalidad libre o definida)
        while (num_partidas is None or partidas_jugadas < num_partidas):
            computadora_opcion = random.choice(opciones)

            jugador_opcion = ""
            while jugador_opcion not in opciones:
                jugador_opcion = input("Elige piedra, papel o tijera: ").lower()
                if jugador_opcion not in opciones:
                    print("Opción no válida. Inténtalo de nuevo.")

            print(f"{nombre_jugador} eligió: {jugador_opcion}")  # Muestra la opción del jugador
            print(f"La computadora eligió: {computadora_opcion} ")

            if jugador_opcion == computadora_opcion:
                print("¡Empate!")
                resultado = "empate"
                estadisticas["jugador1"]["empatadas"] += 1
                estadisticas["computadora"]["empatadas"] += 1

            elif (jugador_opcion == "piedra" and computadora_opcion == "tijera") or \
                (jugador_opcion == "papel" and computadora_opcion == "piedra") or \
                (jugador_opcion == "tijera" and computadora_opcion == "papel"):
                print(f"¡{nombre_jugador} gana!")
                resultado = "ganado"
                estadisticas["jugador1"]["ganadas"] += 1
                estadisticas["computadora"]["perdidas"] += 1

            else:
                print("¡Perdiste!")
                resultado = "perdido"
                estadisticas["jugador1"]["perdidas"] += 1
                estadisticas["computadora"]["ganadas"] += 1

            historico_juegos.append({
                "jugador1": nombre_jugador,
                "jugador2": "Computadora",
                "jugador1_opcion": jugador_opcion,
                "jugador2_opcion": computadora_opcion,
                "resultado": resultado
            })

            partidas_jugadas += 1

            # Preguntar si jugar de nuevo (solo en modo libre)
            if num_partidas is None:
                while True:
                    jugar_de_nuevo = input("¿Quieres jugar otra partida? (si/no): ").lower()
                    if jugar_de_nuevo in ["si", "no"]:
                        break
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")

                if jugar_de_nuevo == "no":
                        print("¡Gracias por jugar! ¡Hasta la próxima!")
                        mostrar_historico_estadisticas()  # Mostrar histórico y estadísticas
                        return  # Salir de la función
                
        # Preguntar si jugar de nuevo (solo si se definió número de partidas)
        if definir_partidas == "si":
            while True:
                jugar_de_nuevo = input("¿Quieres jugar otra vez con la misma cantidad de partidas? (si/no): ").lower()
                if jugar_de_nuevo in ["si", "no"]:
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")

            if jugar_de_nuevo == "si":
                num_partidas = num_partidas_inicial  # Restablecer el número de partidas
                partidas_jugadas = 0  # Reiniciar el contador de partidas
                continue  # Volver al inicio del bucle while True principal
            else:
                print("¡Gracias por jugar! ¡Hasta la próxima!")
                mostrar_historico_estadisticas()  # Mostrar histórico y estadísticas
                return  # Salir de la función
         
def jugar_multijugador():
    
    """Implementa el juego Piedra, Papel o Tijera en la modalidad Multijugador (Usuario vs Usuario).

    Esta función permite que dos jugadores se enfrenten en el juego. Los jugadores pueden
    elegir jugar un número definido de partidas o jugar libremente hasta que decidan no seguir jugando.
    Las opciones de cada jugador se ocultan usando `getpass` para mayor privacidad.
    Se registran las estadísticas de cada partida y se muestra un resumen al final.

    Flujo del juego:
        1.  Los jugadores ingresan sus nombres.
        2.  Se pregunta al Jugador 1 (jugador principal) si desea definir un número de partidas.
        3.  Si se define un número de partidas, se valida la entrada.
        4.  Comienza el bucle principal del juego.
        5.  Dentro del bucle, se juega cada partida:
            a.  Ambos jugadores eligen su opción (se oculta la entrada con `getpass`, y se valida la entrada).
            b.  Se muestran las opciones de ambos jugadores.
            c.  Se determina el ganador según las reglas del juego.
            d.  Se actualizan las estadísticas.
            e.  Se añade la información de la partida al histórico.
        6.  Si se definió un número de partidas, se pregunta al Jugador 1 (jugador principal) si quiere volver a jugar con el mismo número de partidas.
        7.  Si no se definió un número de partidas, se pregunta al Jugador 1 (jugador principal) si quiere jugar otra partida.
        8.  Si el Jugador 1 (jugador principal) no quiere seguir jugando, se muestran las estadísticas y el histórico, y se regresa al menú principal.

    Variables globales utilizadas:
        estadisticas (dict):  Diccionario que almacena las estadísticas del juego. Se modifica dentro de esta función.
        historico_juegos (list): Lista que almacena el histórico de las partidas jugadas. Se modifica dentro de esta función.
        main (function): Función que representa el menú principal del juego. Se llama al finalizar la partida.
        mostrar_historico_estadisticas (function): Función que muestra el histórico y las estadísticas. Se llama al finalizar la partida.
        getpass (module): Módulo utilizado para ocultar la entrada de los jugadores.

    """
    
    nombre_jugador1 = input("Ingresa el nombre del Jugador 1: ")
    nombre_jugador2 = input("Ingresa el nombre del Jugador 2: ")

    # Preguntar si desea definir número de partidas
    while True:
        definir_partidas = input(f"{nombre_jugador1}, ¿Desean definir un número de partidas a jugar? (si/no): ").lower()
        if definir_partidas in ["si", "no"]:
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    if definir_partidas == "si": 
        while True:
            try:
                num_partidas = int(input("Ingrese el número de partidas a jugar: "))
                if num_partidas > 0:
                    break
                else:
                    print("Número de partidas inválido. Debe ser mayor que cero.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
        num_partidas_inicial = num_partidas  # Guarda el número inicial de partidas
    else:
        num_partidas = None

    while True:  # Bucle principal para controlar si se juega de nuevo
        partidas_jugadas = 0
        opciones = ["piedra", "papel", "tijera"]

        # Bucle para jugar partidas (modalidad libre o definida)
        while (num_partidas is None or partidas_jugadas < num_partidas):
            # Obtener opciones de ambos jugadores
            jugador1_opcion = ""
            while jugador1_opcion not in opciones:
                jugador1_opcion = jugador1_opcion = getpass.getpass(prompt=f"{nombre_jugador1}, elige piedra, papel o tijera (no se mostrará): ").lower()
                if jugador1_opcion not in opciones:
                    print("Opción no válida. Inténtalo de nuevo.")

            jugador2_opcion = ""
            while jugador2_opcion not in opciones:
                jugador2_opcion = getpass.getpass(prompt=f"{nombre_jugador2}, elige piedra, papel o tijera (no se mostrará): ").lower()
                if jugador2_opcion not in opciones:
                    print("Opción no válida. Inténtalo de nuevo.")

            print(f"{nombre_jugador1} eligió: {jugador1_opcion}")  # Muestra la opción del jugador 1
            print(f"{nombre_jugador2} eligió: {jugador2_opcion}")  # Muestra la opción del jugador 2

            # Determinar el resultado
            if jugador1_opcion == jugador2_opcion:
                print("¡Empate!")
                resultado = "empate"
                estadisticas["jugador1"]["empatadas"] += 1
                estadisticas["jugador2"]["empatadas"] += 1

            elif (jugador1_opcion == "piedra" and jugador2_opcion == "tijera") or \
                (jugador1_opcion == "papel" and jugador2_opcion == "piedra") or \
                (jugador1_opcion == "tijera" and jugador2_opcion == "papel"):
                print(f"¡{nombre_jugador1} gana!")
                resultado = "ganado"
                estadisticas["jugador1"]["ganadas"] += 1
                estadisticas["jugador2"]["perdidas"] += 1

            else:
                print(f"¡{nombre_jugador2} gana!")
                resultado = "perdido"
                estadisticas["jugador1"]["perdidas"] += 1
                estadisticas["jugador2"]["ganadas"] += 1

            historico_juegos.append({
                "jugador1": nombre_jugador1,
                "jugador2": nombre_jugador2,
                "jugador1_opcion": jugador1_opcion,
                "jugador2_opcion": jugador2_opcion,
                "resultado": resultado
            })

            partidas_jugadas += 1

            # Preguntar si jugar de nuevo (solo en modo libre)
            if num_partidas is None:
                while True:
                    jugar_de_nuevo = input(f"{nombre_jugador1}, ¿Quieren jugar otra partida? (si/no): ").lower()
                    if jugar_de_nuevo in ["si", "no"]:
                        break
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")

                if jugar_de_nuevo == "no":
                        print("¡Gracias por jugar! ¡Hasta la próxima!")
                        mostrar_historico_estadisticas()  # Mostrar histórico y estadísticas
                        return  # Salir de la función
                  
        # Preguntar si jugar de nuevo (solo si se definió número de partidas)
        if definir_partidas == "si":
            while True:
                jugar_de_nuevo = input(f"{nombre_jugador1}, ¿Quieren jugar otra vez con la misma cantidad de partidas? (si/no): ").lower()
                if jugar_de_nuevo in ["si", "no"]:
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")

            if jugar_de_nuevo == "si":
                num_partidas = num_partidas_inicial  # Restablecer el número de partidas
                partidas_jugadas = 0  # Reiniciar el contador de partidas
                continue  # Volver al inicio del bucle while True principal
            else:
                print("¡Gracias por jugar! ¡Hasta la próxima!")
                mostrar_historico_estadisticas()  # Mostrar histórico y estadísticas
                return  # Salir de la función        
        
def mostrar_historico_estadisticas():
    
    """Muestra el histórico de juegos y las estadísticas del juego Piedra, Papel o Tijera.

   Esta función imprime en la consola el histórico de las partidas jugadas, mostrando
   los nombres de los jugadores, sus elecciones y el resultado de cada partida.
   También muestra las estadísticas generales del juego, incluyendo el total de partidas
   jugadas y las estadísticas individuales de cada jugador (ganadas, perdidas y empatadas).

   Si no hay juegos registrados en el histórico, se muestra un mensaje indicando que no
   hay estadísticas recientes.

   Variables globales utilizadas:
       historico_juegos (list): Lista que contiene diccionarios, donde cada diccionario representa una partida y contiene información sobre losjugadores, sus opciones y el resultado.
       estadisticas (dict): Diccionario que contiene las estadísticas de cada jugador. Las claves del diccionario son los nombres de los jugadores y los valores son diccionarios con las estadísticas (ganadas, perdidas, empatadas).
       modo_juego (int): Variable que indica el modo de juego (1 para Usuario vs Computadora, 2 para Multijugador). Se usa para mostrar las estadísticas correspondientes a cada modo.
       main (function): Función que representa el menú principal del juego. Se llama automáticamente al final de esta función para regresar al menú.
   """
    
    if not historico_juegos:
        print("No hay estadisticas recientes")
    else:
        print("\n--- Histórico de juegos ---")
        for juego in historico_juegos:
            print(f"{juego['jugador1']} vs {juego['jugador2']}: {juego['jugador1_opcion']} vs {juego['jugador2_opcion']} - Resultado: {juego['resultado']}")

        print("\n--- Estadísticas del juego ---")
        print(f"Total de partidas jugadas: {len(historico_juegos)}")
        print("Estadísticas por jugador:")
        
        global modo_juego
        
        if modo_juego == 1:
             print(f"  jugador1: Ganadas: {estadisticas['jugador1']['ganadas']}, Perdidas: {estadisticas['jugador1']['perdidas']}, Empatadas: {estadisticas['jugador1']['empatadas']}")
             print(f"  computadora: Ganadas: {estadisticas['computadora']['ganadas']}, Perdidas: {estadisticas['computadora']['perdidas']}, Empatadas: {estadisticas['computadora']['empatadas']}")
        elif modo_juego == 2:
             print(f"  jugador1: Ganadas: {estadisticas['jugador1']['ganadas']}, Perdidas: {estadisticas['jugador1']['perdidas']}, Empatadas: {estadisticas['jugador1']['empatadas']}")
             print(f"  jugador2: Ganadas: {estadisticas['jugador2']['ganadas']}, Perdidas: {estadisticas['jugador2']['perdidas']}, Empatadas: {estadisticas['jugador2']['empatadas']}")
        
          
    main()  # Regresar al menú principal automáticamente 
    
def main():
    """Función principal que ejecuta el bucle del menú de la aplicación Piedra, Papel o Tijera.

   Esta función presenta un menú interactivo al usuario con las siguientes opciones:

   1. Home: Muestra un mensaje de bienvenida.
   2. Configuración: Muestra un mensaje de configuración.
   3. Perfil de usuario: Muestra un mensaje de perfil de usuario.
   4. Iniciar juego: Inicia el juego, permitiendo al usuario seleccionar el modo de juego.
   5. Histórico y estadísticas: Muestra el histórico de partidas y las estadísticas del juego.
   6. Salir del juego: Finaliza la ejecución del programa.

   El programa solicita al usuario que ingrese el número de la opción deseada. Se manejan
   errores de entrada en caso de que el usuario ingrese un valor no numérico. La función
   `manejar_opcion()` es la encargada de procesar la opción elegida por el usuario.

   El bucle continúa hasta que el usuario selecciona la opción 6 (Salir del juego).

   Variables:
       salir (bool): Variable que controla la terminación del bucle. Se inicializa en `False`
                     y se establece en `True` cuando el usuario elige la opción de salir.
       opcion (int): Variable que almacena el número de la opción ingresada por el usuario.

   Funciones llamadas:
       manejar_opcion(opcion): Función que procesa la opción elegida por el usuario.
   """
    
    salir = False
    while not salir:
        print("\n--- Menú de la aplicación ---")
        print("1. Home")
        print("2. Configuración")
        print("3. Perfil de usuario")
        print("4. Iniciar juego")
        print("5. Histórico y estadísticas")
        print("6. Salir del juego")
        try:
            
            opcion = int(input("Ingresa el número de la opción: "))
            salir = manejar_opcion(opcion)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

if __name__ == "__main__":
    main()
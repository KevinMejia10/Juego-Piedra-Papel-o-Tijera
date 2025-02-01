# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:30:10 2025

@author: kevin
"""

import random

# Muestra el menú de la aplicación
print("\n--- Menú de la aplicación ---")
print("1. Home")
print("2. Configuración")
print("3. Perfil de usuario")
print("4. Iniciar juego")
print("5. Salir del juego")

def manejar_opcion(opcion):
# El usuario ingresa el número para acceder a la opción

    if opcion == 1:
        print("¡Página de inicio!")

    elif opcion == 2:
        print("¡Configuración del juego!")

    elif opcion == 3:
        print("¡Perfil de usuario!")

    elif opcion == 4:
        print("¡Empieza el juego!")
        mostrar_instrucciones()  # Muestra las reglas del juego
        jugar()
        return True

    elif opcion == 5:
        print("¡Hasta luego!")
        return True

    else:
        print("Opción inválida. Por favor, elige una opción del menú.")

    return False

def mostrar_instrucciones():

    #Muestra las reglas del juego

    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("Reglas:")
    print("Piedra le gana tijera.")
    print("Tijera le gana a papel.")
    print("Papel le gana a piedra.")
    print("¡Buena suerte!")
    print("Comencemos")

def jugar():
    """Función que ejecuta el juego de Piedra, Papel o Tijera."""

    while True:
        opciones = ["piedra", "papel", "tijera"]
        computadora_opcion = random.choice(opciones)

        while True:
            jugador_opcion = input("Elige piedra, papel o tijera: ").lower()
            if jugador_opcion in opciones:
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

        print(f"La computadora eligió: {computadora_opcion}")

        if jugador_opcion == computadora_opcion:
            print("¡Empate!")
        elif (jugador_opcion == "piedra" and computadora_opcion == "tijera") or \
                (jugador_opcion == "papel" and computadora_opcion == "piedra") or \
                (jugador_opcion == "tijera" and computadora_opcion == "papel"):
            print("¡Ganaste!")
        else:
            print("¡La computadora ganó!")

        # Preguntar si jugar de nuevo
        while True:
            jugar_de_nuevo = input("¿Quieres jugar otra vez? (si/no): ").lower()
            if jugar_de_nuevo in ["si", "no"]:
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

        if jugar_de_nuevo == "no":
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break


def main():
    """Función principal que ejecuta el juego."""

    salir = False
    while not salir:
        try:
            opcion = int(input("Ingresa el número de la opción: "))
            salir = manejar_opcion(opcion)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

if __name__ == "__main__":
    main()





# Descripción del juego Piedra, Papel o Tijera.

Piedra, papel o tijera es un juego de manos en el que participan dos personas. Cada jugador elige una de tres opciones: piedra, papel o tijera. El objetivo es vencer al oponente seleccionando la opción que gana, según las siguientes reglas:

* La piedra aplasta la tijera.
* La tijera corta el papel.
* El papel envuelve la piedra.

## Ambiente IDE de desarrollo.
Spyder version 6.0.3 (Standalone)

## Lenguaje de programacion.
Python versión 3.11.10 64 bit | Qt 5.15.8 | PyQt5 5.15.9

## Librerias utilizadas.
* **Random:** Esta librería se utiliza para generar números aleatorios. En el juego, se usa random.choice(opciones) para que la computadora elija una opción al azar (piedra, papel o tijera). 
* La librería random es una librería estándar de Python, lo que significa que ya viene incluida en la instalación de Python. Por lo tanto, no se necesita instalarla por separado.
* La versión de la librería random que se utiliza en el codigo es la version de Python 3.11.10 64 bit | Qt 5.15.8 | PyQt5 5.15.9
* **Get Pass:**  Esta libreria se utiliza en el modo de juego multijugador para que no se muestre en pantalla la opción (piedra, papel o tijera) selecionada por cada jugador.

* **Nota Importante: La libreria Get Pass no es compatible con la consola QtConsole de Spyder ¿Cómo solucionarlo? Ejecutar el archivo .py en otra terminal, por ejemplo, la terminal de Visual Studio Code.**  

## Como se juega.

### Modo de Juego: Usuario vs Computadora. 
1. Inicio del juego: Cuando se inicia el juego, el usuario accede al menú (Home, Configuración, Perfil de Usuario, Historial y Estadísticas, Iniciar Juego, Salir del Juego) de la aplicación.
2. Si el usuario selecciona "Iniciar Juego" la aplicación consultara el modo de juego que desea jugar, Usuario vs Computadora o Multijugador: Usuario vs Usuario.
3. Si selecciona el modo de juego Usuario vs Computadora.
4. Se muestran las reglas generales del juego y en específico para la modalidad elegida. 
   - Piedra gana a tijera.
   - Tijera gana a papel.
   - Papel gana a piedra.
5. Ingresa nombre del jugador
6. El usuario decide la modalidad de juego, por número partidas definidas o número de partidas libres.
7. Iniciar la partida.
8. El usuario elige la opción: piedra, papel o tijera.
9. La computadora elegira su opción al azar.
10. La computadora realiza la lógica del juego o algoritmo del juego para determinar el resultado. 
11. Se mostrará el resultado de la partida (Empate, Ganaste, Perdiste).
12. Se consulta al usuario si desea seguir jugando, si su respuesta es SI, se juega una nueva partida bajo la misma modalidad, si su respuesta es NO, se muestra un registro histórico y estadística de la partida
13. Finalmente el usuario decide si quiere regresar al menu de la aplicación o salir del juego. 

### Modo de Juego: Multijugador Usuario vs Usuario. 

1. Inicio del juego: Cuando se inicia el juego, el usuario accede al menú (Home, Configuracion, Perfil de Usuario, Historial y Estadísticas, Iniciar Juego, Salir del Juego) de la aplicación.
2. Si el usuario selecciona "Iniciar Juego" la aplicación consultará el modo de juego que desea jugar, Usuario vs Computadora o Multijugador: Usuario vs Usuario.
3. Si selecciona el modo de juego Multijugador: Usuario vs Usuario.
4. Se muestran las reglas generales del juego y en específico para la modalidad elegida.
   - Piedra gana a tijera.
   - Tijera gana a papel.
   - Papel gana a piedra.
5. Ingresa nombre del jugador 1 (jugador principal)
6. Ingresa nombre del jugador 2
7. El usuario principal decide la modalidad de juego, por número partidas definidas o número de partidas libres.
8. Iniciar la partida.
9. El usuario jugador 1 elige la opción: piedra, papel o tijera.
10. El usuario jugador 2 elige la opción: piedra, papel o tijera.
11. La computadora realiza la lógica del juego o algoritmo del juego para determinar el resultado. 
12. Se mostrara el resultado de la partida (Empate, Ganaste, Perdiste).
13. Se consulta al usuario principal si desea seguir jugando, si su respuesta es SI, se juega una nueva partida bajo la misma modalidad, si su respuesta es NO, se muestra un registro histórico y estadística de la partida
14. Finalmente el usuario principal decide si quiere regresar al menú de la aplicación o salir del juego. 

## Instrucciones de instalación. 

Para ejecutar el juego, sigue estos pasos:

1. Clona este repositorio: git clone https://github.com/KevinMejia10/Juego-Piedra-Papel-o-Tijera.git
2. Descarga y abre el archivo "Juego.py" con Python.  
3. Sigue las instrucciones en pantalla para jugar.

## Estructura del repositorio. 

Diagramas de Funcionalidad y Arquitectura. 

  * Diagrama de flujo del Juego.
  * Diagrama de flujo lógica del juego (Usuario vs Computadora).
  * Diagrama de flujo lógica del juego (Multijugador:  Jugador 1 vs Jugador 2).
  * Diagrama de caso de uso (Usuario vs Computadora).
  * Diagrama de caso de uso ((Multijugador:  Jugador 1 vs Jugador 2).
  * Diagrama de Arquitectura de la aplicación.

Archivo .py que tiene el código del juego.

Archivo ReadMe. 



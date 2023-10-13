<div align="center">
    <img src="https://github.com/rconnolly2/Juego_Sudoku_Backtracking/blob/main/img/logo.png?raw=true">
    <h2>Sudoku Solver: ¡Juega a Sudoku o deja a tu ordenador solucionarlo por ti!<h2/>
<div/>

<div>
    <a href="https://github.com/rconnolly2/Juego_Sudoku_Backtracking/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-informational">
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-v3.8-informational">
    </a>
<div/>

<p align="center">
	<img src="http://ForTheBadge.com/images/badges/made-with-python.svg">
</p>
<img alt="GitHub last commit (by committer)" src="https://img.shields.io/github/last-commit/rconnolly2/Juego_Sudoku_Backtracking">

# Sudoku Solver

¿Estás preparado para poner tus habilidades lógicas en práctica? ¡Con este juego de Sudoku, podrás jugar y si te quedas atascado, el juego te ayudará!

El Sudoku es un rompecabezas lógico y numérico que se juega en un tablero cuadrado dividido en nueve subcuadros más pequeños. El objetivo principal del juego es llenar el tablero con números del 1 al 9 de manera que cada fila, columna y región de 3x3 contenga todos los números del 1 al 9 sin repetir ninguno.

## Reglas
Debes llenar el tablero con los números que faltan (del 1 al 9) de manera que no haya repeticiones de ningún número en ninguna fila, columna o región de 3x3. Elige un número del 1 al 9 que aún no se encuentre en esa fila, columna o región específica.

Con la ayuda de Sudoku Solver, no necesitas invertir horas resolviendo acertijos de Sudoku manualmente. Nuestro eficiente algoritmo puede resolver prácticamente cualquier puzle de Sudoku en cuestión de segundos, permitiéndote avanzar rápidamente hacia desafíos más complejos. Además, nuestra función de visualización te muestra cómo opera el algoritmo de retroceso, brindándote la oportunidad de comprender la lógica detrás de cada solución.

## Características del juego

- Puede generar sudokus nuevos y aleatorios.
- Visualización en tiempo real de cómo funciona el algoritmo de "backtracking" para solucionar el Sudoku.
- Interfaz de usuario fácil de usar (GUI).
- Puedes eliminar cuadros específicos.

## Cómo utilizar

Para poder utilizar Sudoku Solver, simplemente descarga el repositorio y ejecuta `start_game.py` en la carpeta `src`. Aparecerá un tablero de Sudoku, y si deseas otro, simplemente pulsa el botón "Generar nuevo Sudoku". Puedes hacer clic en cualquier recuadro e introducir un número del 1 al 9, tienes un total de 3 intentos.

![jugando sudoku](https://github.com/rconnolly2/Algoritmo_Punto_Medio_Circunferencias/blob/master/algo.gif?raw=true)

Si te quedas atascado, puedes dejar que el programa lo resuelva por ti utilizando la recursividad y el "backtracking". Tienes dos opciones: "Resolver Sudoku Rápido" y "Resolver Sudoku".

![resolver sudoku rápido](https://github.com/rconnolly2/Algoritmo_Punto_Medio_Circunferencias/blob/master/algo.gif?raw=true)

## Entradas

| Teclas               | Acciones                             |
|----------------------|-------------------------------------|
| `Clic izquierdo ratón` | Selecciona el cuadro a editar.      |
| `Teclas del 1-9`     | Números válidos para el juego Sudoku. |

## Instalación

- Clona este repositorio:
```
git clone https://github.com/rconnolly2/Juego_Sudoku_Backtracking.git
```

**O también**

- Descarga el ZIP del repositorio y descomprímelo.
- Cambia a la carpeta o ábrela.
- Ejecuta `setup_windows.py` o `.bat`.
```
python setup_windows.py
```
**O también**
```
.\setup_windows.bat
```
- Ahora tienes un entorno virtual que puedes activar en la carpeta `Scripts\activate.bat`.
- Para iniciar el juego, ve a la carpeta `src`:
```
python start_game.py
```

## Conclusión

Si disfrutas de los desafíos que plantea el Sudoku, Sudoku Solver se presenta como la herramienta ideal para resolverlos de manera rápida y sencilla. Gracias a su potente algoritmo y su interfaz intuitiva, te encontrarás resolviendo acertijos en un abrir y cerrar de ojos. Además, el Sudoku es una excelente forma de ejercitar tu mente y mejorar tus habilidades cognitivas, lo que lo convierte en un juego entretenido y estimulante para personas de todas las edades. Entonces, ¿por qué esperar más? ¡Descarga Sudoku Solver hoy mismo y comienza a disfrutar del desafío!


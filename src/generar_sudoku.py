from random import randint
import copy

class GenerarSudoku:
    def __init__(self):
        pass
    
    @staticmethod
    def generar_sudoku(sudoku_base: list):
        '''
        Esta función lo que va hacer es generar un sudoku a base de otro, podríamos haber creado un sudoku utilizando también recursividad 
        y backtracking pero para simplificar mas lo vamos hacer asi: cojo la tabla en la que nos vamos a basar y cambiamos aleatoriamente
        las filas y columnas MIENTRAS sean de la misma matriz de 3x3 esto dará la ilusión de otra tabla https://en.wikipedia.org/wiki/Combinatorics

        sudoku_base => la tabla que nos basamos
        '''
        copia_tabla_param = copy.deepcopy(sudoku_base)

        # swap entre 2 columnas aleatorias:
        colum_1 = [0, 3, 6]
        colum_2 = randint(1, 2)
        for columna in range(len(sudoku_base)):
            if columna in colum_1: # Si la primera columna empieza por index 0, 3, 9 hacer un swap de columnas random
                copy_columna1 = copia_tabla_param[columna]
                copy_columna2 = copia_tabla_param[columna+colum_2]
                copia_tabla_param[columna] = copy_columna2
                copia_tabla_param[columna+colum_2] = copy_columna1

            for fila in range(len(sudoku_base)):
                if fila in colum_1: # Si la primera fila empieza por index 0, 3, 9 hacer un swap de filas random
                    copy_columna1 = copia_tabla_param[columna][fila]
                    copy_columna2 = copia_tabla_param[columna][fila+colum_2]
                    copia_tabla_param[columna][fila] = copy_columna2
                    copia_tabla_param[columna][fila+colum_2] = copy_columna1

        return copia_tabla_param # Devolvemos la nueva tabla generada

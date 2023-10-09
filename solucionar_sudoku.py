class SolucionarSudoku:

    def __init__(self):
        pass
    
    @staticmethod
    def encontrar_cuadrado_vacio(tabla):
        '''
        Devuelve el primer numero que es vacio => (0)
        '''

        for i in range(len(tabla)):
            for j in range(len(tabla[i])):
                if tabla[i][j] == 0:
                    return (i, j) # devuelve posición file y columna vacía
                

    @staticmethod
    def es_numero_valido(tabla, num, posición):
        '''
        Esta función devuelve un booleano si poniendo este numero es valido en las reglas de sudoku
        '''
        # Compruebo filas - horizontal
        for i_fila in range(len(tabla[0])): # iterar sobre todas las columnas => 9
            if tabla[posición[0]][i_fila] == num and i_fila != posición[1]: # compruebo si el numero que introduzco ya existe en filas y que no es el mismo numero que estoy poniendo (mismo x)
                return False
        
        # Compruebo columnas - vertical
        for i_columna in range(len(tabla[0])): # iterar sobre todas las filas => 9
            if tabla[i_columna][posición[1]] == num and i_columna != posición[0]:
                return False
            
        # Comprobar 9 matrices de 9 números son únicos
        num_matriz_horizontal = posición[1] // 3 # lo divido entre 3 para saber si esta en matriz 0, 1, 2
        num_matriz_vertical = posición[0] // 3
        # Horizontal primero de la matriz
        for i_x_matriz in range(posición[1], posición[1]+3):
            if tabla[posición[0]][i_x_matriz] == num and i_x_matriz != posición[1]: # lo mismo que arriba pero en la matriz de 3x3 números para ver si se repiten
                return False
        # Ahora vertical matriz
        for i_y_matriz in range(posición[0], posición[0]+3):
            if tabla[i_y_matriz][posición[1]] == num and i_x_matriz != posición[0]:
                return False
            
        # Si pasas todas estas condiciones es => True
        return True
    

    def resolver_sudoku(tabla):
        '''
        Resolver sudoku con recursividad y backtracking
        https://en.wikipedia.org/wiki/Backtracking
        '''
        numero = 1
        pos_vacía = SolucionarSudoku.encontrar_cuadrado_vacio(tabla)

        if (pos_vacía == None):
            return True # Ya hemos resuelto el sudoku porque no hay cuadrados vacíos
        else:
            fila, columna = pos_vacía

        for iter in range(1, 10): # iterador del 1 al 10 (no empieza por 0)
            
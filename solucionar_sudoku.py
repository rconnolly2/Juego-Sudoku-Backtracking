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
        
        #Compruebo columnas - vertical
        

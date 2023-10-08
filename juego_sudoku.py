import tkinter as tk

class Sudoku:

    tabla = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]



    TAMAÑO_VENTANA_INICIAL = (400, 400)


    def dibujar_tabla(self):
        alto = -1 # Porque empiezo por -1 y no 0, fácil porque frame.grid() row y column empiezan por 0
        ancho = -1
        for i in range(len(self.tabla)):
            alto += 1
            for j in range(len(self.tabla[i])):
                ancho += 1
                str_numero = tk.StringVar(value=str(self.tabla[alto][ancho]))
                # Cuadrados con texto utilizando (Label)
                cuadrado = tk.Label(self.ventana, bg="green" if alto % 2 == 0 else "red", textvariable=str_numero)
                cuadrado.grid(row=ancho, column=alto, sticky="nsew") # sticky=> quiero se peguen arriba, abajo, derecha y izquierda
                self.lista_cuadrados[alto][ancho][0] = cuadrado # añado label cuadrado a mi lista de cuadrados
                self.lista_cuadrados[alto][ancho][1] = str_numero

                # Texto utilizando (labels)

            ancho = -1 # reseteo iterador ancho

        print("Dimensiones tabla: " + str(alto) + " " + str(ancho))

        # Configurar cuadrados fila & columnas para que se puedan escalar
        for num_columna_fila in range(len(self.tabla)):
            self.ventana.grid_columnconfigure(num_columna_fila, weight=1) # weight es cuando se puede escalar 
            self.ventana.grid_rowconfigure(num_columna_fila, weight=1)    # en relación cono los otros 1 > 0 el menu no queremos que se escale :)
                                                                          # también las filas

    def __init__(self, nombre_ventana: str):
        # Inicio tkinter con nombre de ventana:
        self.ventana = tk.Tk()
        self.ventana.title(nombre_ventana)
        # Empieza con este tamaño ventana
        self.ventana.minsize(width=self.TAMAÑO_VENTANA_INICIAL[0], height=self.TAMAÑO_VENTANA_INICIAL[1])
        # Listas para los cuadrados
        tamaño_filas_columnas = len(self.tabla)
        self.lista_cuadrados = [[[None, None] for columnas in range(tamaño_filas_columnas)] for filas in range(tamaño_filas_columnas)]
   
    def run_sudoku(self):
        self.lista_cuadrados[0][2][1].set("hola")
        self.ventana.mainloop()





if __name__ == "__main__":
    mi_sudoku = Sudoku("Sudoku Juego")
    mi_sudoku.dibujar_tabla()
    mi_sudoku.run_sudoku()
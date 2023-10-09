import tkinter as tk
from solucionar_sudoku import SolucionarSudoku

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


    ANCHO_MENU = 100
    TAMAÑO_VENTANA_INICIAL = (400+ANCHO_MENU, 400)


    def dibujar_tabla(self):
        alto = -1 # Porque empiezo por -1 y no 0, fácil porque frame.grid() row y column empiezan por 0
        ancho = -1
        for i in range(len(self.tabla)):
            alto += 1
            for j in range(len(self.tabla[i])):
                ancho += 1
                str_numero = tk.StringVar(value=str(self.tabla[alto][ancho]))

                # Cuadrados con texto utilizando (Label)
                cuadrado = tk.Label(self.ventana, bg="green" if alto % 2 == 0 else "red", textvariable=str_numero, borderwidth=1, relief="solid")
                cuadrado.grid(row=alto, column=ancho, sticky="nsew") # sticky=> quiero se peguen arriba, abajo, derecha y izquierda
                self.lista_cuadrados[alto][ancho][0] = cuadrado # añado label cuadrado a mi lista de cuadrados
                self.lista_cuadrados[alto][ancho][1] = str_numero

                # Texto utilizando (labels)

            ancho = -1 # reseteo iterador ancho

        # Configurar cuadrados fila & columnas para que se puedan escalar
        for num_columna_fila in range(len(self.tabla)):
            self.ventana.grid_columnconfigure(num_columna_fila, weight=1) # weight es cuando se puede escalar 
            self.ventana.grid_rowconfigure(num_columna_fila, weight=1)    # en relación con los otros 1 > 0 el menu no queremos que se escale :)
                                                                          # también las filas

    def dibujar_menu(self):
        # Esto seria como el "div" del menu
        div_menu = tk.Frame(self.ventana, bg="#F3F3F3", width=self.ANCHO_MENU, height=self.TAMAÑO_VENTANA_INICIAL[1])
        # Configuro para que no sea escalable y este después de los cuadrados horizontalmente
        div_menu.grid(row=0, column=9, rowspan=9, sticky="nw")
        self.ventana.grid_columnconfigure(len(self.tabla), weight=0) # weight 0 porque en referencia con los cuadrados queremos que escale la mitad que ellos

        # Añado el titulo del menu al div menu
        titulo_menu = tk.Label(div_menu, text="Menu Sudoku:")
        titulo_menu.pack(pady=20)
        # Botones para generar nuevo sudoku,borrar cuadrado y resolver sudoku
        b_nuevo_sudoku = tk.Button(div_menu, fg="white", bg="#0067C0", text="Nuevo\nSudoku", border=1)
        b_borrar_cuadrado = tk.Button(div_menu, fg="white", bg="#0067C0", text="Borrar cuadrado\nseleccionado")
        b_resolver_sudoku = tk.Button(div_menu, fg="white", bg="#0067C0", text="Resolver\nSudoku")
        br = tk.Label(div_menu, text="", height=12, bg="#F3F3F3") # espacio vació para que se vea mas fondo
        b_nuevo_sudoku.pack()
        b_borrar_cuadrado.pack(pady=20)
        b_resolver_sudoku.pack()
        br.pack()

    def __init__(self, nombre_ventana: str):
        # Inicio tkinter con nombre de ventana:
        self.ventana = tk.Tk()
        self.ventana.title(nombre_ventana)
        # Empieza con este tamaño MÍNIMO! ventana
        self.ventana.minsize(width=self.TAMAÑO_VENTANA_INICIAL[0], height=self.TAMAÑO_VENTANA_INICIAL[1])
        # Listas para los cuadrados
        tamaño_filas_columnas = len(self.tabla)
        # Creo una lista para guardar el obj StringVar y label de los cuadrado, creo la lista con un "list comprehension":
        self.lista_cuadrados = [[[None, None] for columnas in range(tamaño_filas_columnas)] for filas in range(tamaño_filas_columnas)]

    def run_sudoku(self):
        self.lista_cuadrados[0][2][1].set("hola")
        print(self.tabla)
        SolucionarSudoku.resolver_sudoku(self.tabla)
        print(self.tabla)
        self.ventana.mainloop()

    



if __name__ == "__main__":
    mi_sudoku = Sudoku("Sudoku Juego")
    mi_sudoku.dibujar_tabla()
    mi_sudoku.dibujar_menu()
    mi_sudoku.run_sudoku()

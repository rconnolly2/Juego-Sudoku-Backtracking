import tkinter as tk
from solucionar_sudoku import SolucionarSudoku
import threading
import time
import copy
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
    tabla_solucionado = copy.deepcopy(tabla) # Hago un deep copia primero (porque es una lista de listas)


    ANCHO_MENU = 100
    TAMAÑO_VENTANA_INICIAL = (400+ANCHO_MENU, 400)


    def dibujar_tabla(self):
        '''
        Esta función se encarga de dibujar la tabla recorriendo la lista de la tabla 
        '''
        alto = -1 # Porque empiezo por -1 y no 0, fácil porque frame.grid() row y column empiezan por 0
        ancho = -1
        for i in range(len(self.tabla)):
            alto += 1
            for j in range(len(self.tabla[i])):
                ancho += 1
                str_numero = tk.StringVar(value=(str(self.tabla[alto][ancho]) if (self.tabla[alto][ancho]) != 0 else "")) # poner numero de lista si no es 0 si lo es poner ""

                # Cuadrados con texto utilizando (Label)
                cuadrado = tk.Label(self.ventana, bg="darksalmon" if alto % 2 == 0 else "lightsalmon", textvariable=str_numero, borderwidth=1, relief="solid")
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

    def display_resultado_sudoku(self, tabla: list):
        '''
        Esta función va a actualizar la tabla entera cogiendo una lista (como un movimiento valido)
        la diferencia que esta función ya imprime la tabla resulta, enseñándolo de cuadrado a cuadrado
        lo cual sera mas rápido que el otro método.

        tabla => la lista que se va a imprimir en pantalla
        '''

        for i in range(len(tabla)):
            for j in range((len(tabla))):
                self.lista_cuadrados[i][j][0].configure(bg="green" if self.tabla[i][j] == 0 else "lightsalmon") # cambio color del label a "green" el movimiento valido 
                self.lista_cuadrados[i][j][1].set(str(tabla[i][j])) # ponemos el numero correcto al label
                time.sleep(0.1) # duermo 100 milisegundos entre imprimir cuadrados


    def dibujar_menu(self):
        # Creo hilo (resolver sudoku) sin ejecutar para luego:
        hilo_1 = threading.Thread(target=SolucionarSudoku.resolver_sudoku, args=(self.tabla, self.lista_cuadrados))
        # Segundo hilo para enseñar resultado mas rápido:
        hilo_2 = threading.Thread(target=self.display_resultado_sudoku, args=[self.tabla_solucionado])
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

        # ejecuto hilo resolver sudoku con backtracking (asi podemos resolver el sudoku mientras estamos en bucle principal)
        b_resolver_sudoku = tk.Button(div_menu, fg="white", bg="#0067C0", text="Resolver\nSudoku", command=lambda: hilo_1.start())
        # resolver sudoku rapido con tabla ya resulta antes:
        b_resolver_sudoku_rápido = tk.Button(div_menu, fg="white", bg="#0067C0", text="Resolver\nSudoku rápido", command=hilo_2.start)
    
        br = tk.Label(div_menu, text="", height=12, bg="#F3F3F3") # espacio vació para que se vea mas fondo
        b_nuevo_sudoku.pack()
        b_borrar_cuadrado.pack(pady=20)
        b_resolver_sudoku.pack()
        b_resolver_sudoku_rápido.pack()
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
    
    @staticmethod
    def imprimir_movimiento_valido(numero, pos_movimiento, lista_frames):
        if numero != 0:
            lista_frames[pos_movimiento[0]][pos_movimiento[1]][0].configure(bg="blue") # cambio color frame
            lista_frames[pos_movimiento[0]][pos_movimiento[1]][1].set(str(numero)) # cambio numero
        else:
            raise ValueError("Error: el numero que me as dado es 0!")

    def imprimir_movimiento_invalido(numero):
        pass

    def run_sudoku(self):
        
        # Resuelvo el sudoku en una copia de la tabla antes para agilizar porque el bucle de tkinter tarda mucho:
        SolucionarSudoku.resolver_sudoku(self.tabla_solucionado)
        #self.actualizar_tabla(self.tabla_solucionado)
        # Primer hilo resolver sudoku con backtracking (asi podemos resolver el sudoku mientras estamos)
        # Ejecutando el bucle principal de tkinter
        hilo_1 = threading.Thread(target=SolucionarSudoku.resolver_sudoku, args=(self.tabla, self.lista_cuadrados))
        # Arrancamos hilo 1 y después bucle principal de tkinter
        #hilo_1.start()
        self.ventana.mainloop()
        

    



if __name__ == "__main__":
    mi_sudoku = Sudoku("Sudoku Juego")
    mi_sudoku.dibujar_tabla()
    mi_sudoku.dibujar_menu()
    mi_sudoku.run_sudoku()

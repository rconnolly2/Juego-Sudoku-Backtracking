import tkinter as tk
from tkinter import messagebox
import threading
import time
import copy

from solucionar_sudoku import SolucionarSudoku
from generar_sudoku import GenerarSudoku

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

    VIDAS_JUEGO = 3
    ANCHO_MENU = 100
    TAMAÑO_VENTANA_INICIAL = (500+ANCHO_MENU, 400)

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
        # StringVar del texto del menu (label):
        self.string_var_menu = tk.StringVar(value="Menu Sudoku\nVidas: " + str(self.VIDAS_JUEGO))
        # booleano si se ha hecho click en un cuadrado para aceptar keystrokes
        self.click_label = False
        # fila y columna seleccionada:
        self.fila_colum_seleccionado = None, None
        
    def run_sudoku(self):
        
        # Resuelvo el sudoku en una copia de la tabla antes para agilizar porque el bucle de tkinter tarda mucho:
        SolucionarSudoku.resolver_sudoku(self.tabla_solucionado)
        self.asignar_click_labels()
        # Asignar keystrokes a todo el programa en caso de números del 1 al 9
        self.ventana.bind("<Key>", self.input_usuario)
        # Asingo evento en caso de que usuario de cerrar ventana:
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        # Ejecutando el bucle principal de tkinter
        self.ventana.mainloop()

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

    def display_resultado_sudoku(self):
        '''
        Esta función va a actualizar la tabla entera cogiendo una lista (la tabla resulta al iniciar el programa en => run)
        la diferencia que esta función ya imprime la tabla resulta, enseñándolo de cuadrado a cuadrado
        lo cual sera mas rápido que el otro método por problemas con tkinter y su bucle que es muy lento.
        '''

        for i in range(len(self.tabla)):
            for j in range((len(self.tabla))):
                self.lista_cuadrados[i][j][0].configure(bg="green" if self.tabla[i][j] == 0 else "lightsalmon") # cambio color del label a "green" el movimiento valido 
                self.lista_cuadrados[i][j][1].set(str(self.tabla_solucionado[i][j])) # ponemos el numero correcto al label
                time.sleep(0.1) # duermo 100 milisegundos entre imprimir cuadrados
    
    def actualizar_tabla_sudoku(self):
        '''
        Esta función va a actualizar la tabla entera, normalmente esto se utilizara por ejemplo si
        hay una tabla nueva cogiendo los nuevos valores en self.tabla (sin resolver)
        '''

        for i in range(len(self.tabla)):
            for j in range((len(self.tabla))):
                # Si el valor nuevo es un cero ponemos un string vació (""):
                self.lista_cuadrados[i][j][1].set(str(self.tabla[i][j]) if self.tabla[i][j] != 0 else "") # ponemos el numero nuevo de tabla (sin solucionar) al label
                # Ahora aspecto del label: color, borde etc ...
                self.lista_cuadrados[i][j][0].configure(bg="darksalmon" if i % 2 == 0 else "lightsalmon", border=1)

    def dibujar_menu(self, actualizar=False):
        '''
        Esta función dibuja por primera vez o actualizara el menu en pantalla.

        actualizar => booleano (Si esto es True solo se actualizara el hilo de resolver sudoku con la nueva tabla)
        '''
        if actualizar == True:
            # Actualizo hilo con nueva tabla (resolver sudoku) sin ejecutar para luego:
            hilo_1 = threading.Thread(target=SolucionarSudoku.resolver_sudoku, args=(self.tabla, self.lista_cuadrados))
            # Actualizo botón con el nuevo thread que tiene la nueva tabla a solucionar
            self.b_resolver_sudoku.configure(text="Resolver\nSudoku", command=lambda: hilo_1.start())

        else: # Dibujamos tabla por primera vez
            # Creo hilo (resolver sudoku) sin ejecutar para luego:
            hilo_1 = threading.Thread(target=SolucionarSudoku.resolver_sudoku, args=(self.tabla, self.lista_cuadrados))
            # Segundo hilo para enseñar resultado mas rápido:
            hilo_2 = threading.Thread(target=self.display_resultado_sudoku)
            # Esto seria como el "div" del menu
            self.div_menu = tk.Frame(self.ventana, bg="#F3F3F3", width=self.ANCHO_MENU, height=self.TAMAÑO_VENTANA_INICIAL[1])
            # Configuro para que no sea escalable y este después de los cuadrados horizontalmente
            self.div_menu.grid(row=0, column=9, rowspan=9, sticky="nw")
            self.ventana.grid_columnconfigure(len(self.tabla), weight=0) # weight 0 porque en referencia con los cuadrados queremos que escale la mitad que ellos

            # Añado el titulo del menu al div menu con un string var en constructor
            titulo_menu = tk.Label(self.div_menu, textvariable=self.string_var_menu)
            titulo_menu.pack(pady=20)
            # Botones para generar nuevo sudoku,borrar cuadrado y resolver sudoku
            b_nuevo_sudoku = tk.Button(self.div_menu, fg="white", bg="#0067C0", text="Nuevo\nSudoku", border=1, command=self.nuevo_sudoku)
            b_borrar_cuadrado = tk.Button(self.div_menu, fg="white", bg="#0067C0", text="Borrar cuadrado\nseleccionado", command=self.eliminar_cuadrado_label)

            # Ejecuto hilo resolver sudoku con backtracking (asi podemos resolver el sudoku mientras estamos en bucle principal)
            # Lo guardo en instancia para poder actualizarlo luego
            self.b_resolver_sudoku = tk.Button(self.div_menu, fg="white", bg="#0067C0", text="Resolver\nSudoku", command=lambda: hilo_1.start())
            # resolver sudoku rápido con tabla ya resulta antes:
            b_resolver_sudoku_rápido = tk.Button(self.div_menu, fg="white", bg="#0067C0", text="Resolver\nSudoku rápido", command=hilo_2.start)

            br = tk.Label(self.div_menu, text="", height=12, bg="#F3F3F3") # espacio vació para que se vea mas fondo
            b_nuevo_sudoku.pack()
            b_borrar_cuadrado.pack(pady=20, padx=10)
            self.b_resolver_sudoku.pack()
            b_resolver_sudoku_rápido.pack(pady=20)
            br.pack()

    def asignar_click_labels(self):
        '''
        Esta función su misión es asignar evento de click por <Button-1> => click izq ratón
        a todos los labels de la cuadricula.
        '''
        for i in range(len(self.lista_cuadrados)):
            for j in range(len(self.lista_cuadrados)):
                # cada una de los "labels" de la cuadricula les asignamos un evento de click (cuando hay click izq del ratón)
                self.lista_cuadrados[i][j][0].bind("<Button-1>", self.input_usuario) # cuando hay evento se manda a función => input_usuario()

    def input_usuario(self, event):
        '''
        En esta función la misión es ver que label ha hecho click y hacer la acción conveniente:
        '''
        keystrokes_aceptados = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        fila, colum = self.fila_colum_seleccionado # saco ultima fila columna seleccionada (si la hay)
        objeto_tkinter = event.widget # que tipo de objeto es: puede ser o label o un evento de teclado
        tecla = event.keysym # consigue la tecla pulsada

        if isinstance(objeto_tkinter, tk.Label) and self.click_label == False: # es un label!

            objeto_tkinter.config(bg="lightsalmon", highlightthickness=1, highlightbackground="green", borderwidth=0) # cambio el aspecto del label a un borde de color verde
            self.click_label = True # a hecho click ahora podemos aceptar eventos de teclado por ejemplo un numero
            # Encuentro el numero de fila y columna:
            for i in range(len(self.lista_cuadrados)):
                for j in range(len(self.lista_cuadrados)):
                    if self.lista_cuadrados[i][j][0] == objeto_tkinter:
                        self.fila_colum_seleccionado = i, j # he encontrado la fila y columna

        elif (tecla in keystrokes_aceptados) and (self.click_label == True) and (self.fila_colum_seleccionado[0] != None): # es un input de teclado! del 1-9 y antes se ha hecho click en un cuadro
            if self.tabla_solucionado[fila][colum] == int(tecla): # si el valor es el mismo que la tabla solucionada:
                self.tabla[fila][colum] = int(tecla) # cambio valor 0 de tabla al numero del keystroke
                self.lista_cuadrados[fila][colum][1].set(str(tecla)) # cambio el StringVar del Label
                self.lista_cuadrados[fila][colum][0].configure(bg="green", highlightthickness=0, highlightbackground="black", borderwidth=1)
                self.fila_colum_seleccionado = None, None # quito cuadrado seleccionado
                self.click_label = False # Ahora puedes volver a intentarlo
            else:
                self.lista_cuadrados[fila][colum][1].set(str(tecla)) # cambio el StringVar del Label
                self.lista_cuadrados[fila][colum][0].configure(bg="red", highlightthickness=0, highlightbackground="black", borderwidth=1)
                self.fila_colum_seleccionado = None, None # quito cuadrado seleccionado
                self.VIDAS_JUEGO -= 1 # quitamos una vida de las 3
                self.actualizar_pantalla_vidas() # actualizo vida pantalla, si vida = 0 cierro el juego
                self.click_label = False if self.VIDAS_JUEGO > 0 else True # Si le quedan vidas puede volver a intentarlo

    def nuevo_sudoku(self):
        '''
        Creo sudoku con mi función generar_sudoku() luego lo aplico a mi tabla
        resuelvo el sudoku y imprimo en pantalla el nuevo sudoku con dibujar_tabla()
        '''
        if 0 in [val for sublist in self.tabla for val in sublist]: # Si hay mas de un cero en la tabla:
            self.tabla = GenerarSudoku.generar_sudoku(self.tabla) # generar nuevo sudoku aleatorio
            self.tabla_solucionado = copy.deepcopy(self.tabla) # genero copia de nuevo sudoku
            SolucionarSudoku.resolver_sudoku(self.tabla_solucionado) # resolver tabla sudoku
            self.asignar_click_labels() # asigna botones a todos los labels (solo botón ratón izq)
            self.dibujar_menu(actualizar=True) # no creo el menu entero solo actualizo botón resolver sudoku con la nueva tabla
            self.actualizar_tabla_sudoku() # actualizo valores de los labels con actualizar_tabla_sudoku
        else:
            messagebox.showwarning("Sudoku ya resulto", "Alerta: Este sudoku ya ha sido resuelto con lo cual no se puede generar otro, inicia el programa otra vez")

    def actualizar_pantalla_vidas(self):
        '''
        Esta función actualiza en pantalla las vidas del jugador con VIDAS_JUEGO => StringVar del Label
        ademas si vida es = 0 se cierra el juego sudoku
        '''
        self.string_var_menu.set("Menu Sudoku\nVidas: " + str(self.VIDAS_JUEGO))
        if self.VIDAS_JUEGO == 0:
            time.sleep(1.5)
            exit() # cierro programa

    def eliminar_cuadrado_label(self):
        '''
        Esta función eliminara el cuadrado seleccionado anteriormente en la tabla y
        en la lista de labels y si no se ha seleccionado anteriormente enviara en "pop up" de error

        '''
        if self.click_label == True:
            fila, colum = self.fila_colum_seleccionado
            self.tabla[fila][colum] = 0 # cambio el valor de la lista tabla
            self.lista_cuadrados[fila][colum][0].configure(bg="darksalmon" if fila % 2 == 0 else "lightsalmon", highlightthickness=0, border=1) # cambio propiedades del label
            self.lista_cuadrados[fila][colum][1].set("") # cambio el StringVar del label a string vació
            self.click_label = False # usuario puede hacer otra acción
        else:
            messagebox.showerror("Error: Sin selección", "Error: No has seleccionado ningún recuadro, selecciona un recuadro y luego dale al botón eliminar")

    def cerrar_ventana(self):
        #https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.Message
        if messagebox.askokcancel("Cerrar", "¿Quieres cerrar el programa?"):
            self.ventana.destroy()
            exit()
        

    



if __name__ == "__main__":
    mi_sudoku = Sudoku("Sudoku Juego")
    mi_sudoku.dibujar_tabla()
    mi_sudoku.dibujar_menu()
    mi_sudoku.run_sudoku()

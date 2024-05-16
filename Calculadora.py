#vamos a desarrollar calculadora con la libreria tkinter
import tkinter as Tk
from tkinter import ttk
from tkinter import END
import cmath as Mat

#i=0
#def Obtener(dato):
#    global i
#    i+=1
#    Pantalla_Linea1.insert(i, dato)

i=0

def Obtener(d):
	global i
	i+=1
	Pantalla_Linea2.insert(i, d)
	
def operacion():
	global i
	ecuacion = Pantalla_Linea2.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			Pantalla_Linea1.delete(0, END)
			Pantalla_Linea1.insert(0, ecuacion)
			Pantalla_Linea2.delete(0,END)
			Pantalla_Linea2.insert(0,result)
			
			longitud = len(result)
			i = longitud
		except:
			result = 'ERROR'
			Pantalla_Linea2.delete(0,END)
			Pantalla_Linea2.insert(0,result)
	else:
		pass


def borrar_unoauno():
	global i 
	if i==-1:
		pass
	else:
		Pantalla_Linea2.delete(i, last= None)
		i-=1

def borrar_todo():
    # Borrando todo luego de pulsar boton AC 
    Pantalla_Linea1.delete(0, END) 
    Pantalla_Linea2.delete(0, END) 

#creamos la ventana de la calculadora
ventana_calculadoraB = Tk.Tk()
ventana_calculadoraB.title("Calculadora")
#ventana_calculadoraB.geometry("+500+80")
#ventana_calculadoraB.config(bg= "white")
#ventana_calculadoraB.resizable(0,0)
ventana_calculadoraB.iconbitmap(bitmap= "icocal.ico")
ventana_calculadoraB.columnconfigure(0, weight=1)
ventana_calculadoraB.rowconfigure(0, weight=1)
ventana_calculadoraB.rowconfigure(1, weight=1)
ventana_calculadoraB.rowconfigure(2, weight=1)


#Declaramos y configuramos los estilos
Estilo_Frame = ttk.Style()
Estilo_Frame.theme_use('clam')
Estilo_Frame.configure('mainframe.TFrame', backgraund="#DBDBDB")

#Estilo_Pantalla1 = ttk.Style()
#Estilo_Pantalla1.configure('Pantalla1.TEntry', 
#    font= ("arial", 30),
#    justify="right",
#    backgraund="White"
#    )

#Estilo_Pantalla2 = ttk.Style()
#Estilo_Pantalla2.configure('Pantalla2.TEntry', 
#    font= 'arial 40', 
#    justify="left", 
#    background="White"
#    )

Estilo_Botones_Numeros = ttk.Style()
Estilo_Botones_Numeros.configure('Botones_Numeros.TButton',
        font="arial 22",
        width=5,
        background="#FFFFFF",
        relief="flat"
        )

Estilo_Botones_Borrar=ttk.Style()
Estilo_Botones_Borrar.configure('Botones_Borrar.TButton',
        font="arial 22",
        width=5,
        background="#B71C1C",
        relief="flat"
        )
Estilo_Botones_Borrar.map('Botones_Borrar.TButton',
        foreground=[('active', '#FFFFFF')],
        #background=[('active', '#FFFFFF')]
        )

Estilo_Botones_Operadores = ttk.Style()
Estilo_Botones_Operadores.configure('Botones_Operadores.TButton',
        font="arial 22",
        width=5,
        background="#CECECE",
        relief="flat")


#pantalla
    #Variable para la entrada de texto
Entrada1 = ""
#Entrada2 = ""    
    #Pantalla de entrada
Pantalla_Linea1  = ttk.Entry(ventana_calculadoraB, style='Pantalla1.TEntry', font= "arial 30", justify="right")
Pantalla_Linea1.grid(column=0, row=0, columnspan=4, sticky=("W, N, E, S"))


Pantalla_Linea2  = ttk.Entry(ventana_calculadoraB, style='Pantalla2.TEntry', font="arial 40", justify="right", )
Pantalla_Linea2.grid(column=0, row=1, columnspan=4, sticky=("W, N, E, S"))


#frame donde estaran los botones
mainframe = ttk.Frame(ventana_calculadoraB, style="mainframe.TFrame")
mainframe.grid(column=0, row=2, sticky= ("W, N, E, S"))
#esto es para hacer que sea adaptable a la pantalla completa
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)


#Resultado = ttk.Label(mainframe, font= ("Arial 10"))
#Resultado.grid(column=0,row=0)


#botones
Boton0 = ttk.Button(mainframe, text="0", command=lambda: Obtener(0), style='Botones_Numeros.TButton')
Boton1 = ttk.Button(mainframe, text="1", command=lambda: Obtener(1), style='Botones_Numeros.TButton')
Boton2 = ttk.Button(mainframe, text="2", command=lambda: Obtener(2), style='Botones_Numeros.TButton')
Boton3 = ttk.Button(mainframe, text="3", command=lambda: Obtener(3), style='Botones_Numeros.TButton')
Boton4 = ttk.Button(mainframe, text="4", command=lambda: Obtener(4), style='Botones_Numeros.TButton')
Boton5 = ttk.Button(mainframe, text="5", command=lambda: Obtener(5), style='Botones_Numeros.TButton')
Boton6 = ttk.Button(mainframe, text="6", command=lambda: Obtener(6), style='Botones_Numeros.TButton')
Boton7 = ttk.Button(mainframe, text="7", command=lambda: Obtener(7), style='Botones_Numeros.TButton')
Boton8 = ttk.Button(mainframe, text="8", command=lambda: Obtener(8),  style='Botones_Numeros.TButton')
Boton9 = ttk.Button(mainframe, text="9", command=lambda: Obtener(9), style='Botones_Numeros.TButton')
Botonpunto = ttk.Button(mainframe, text=".", command=lambda: Obtener("."),  style='Botones_Operadores.TButton')

Boton_abrir_parentesis = ttk.Button(mainframe, text="(", command=lambda: Obtener('('),  style='Botones_Operadores.TButton')
Boton_cerrar_parentesis = ttk.Button(mainframe, text=")", command=lambda: Obtener(')'), style='Botones_Operadores.TButton')

Boton_borrar = ttk.Button(mainframe, text=chr(9003), command=lambda: borrar_unoauno(), style='Botones_Borrar.TButton')
Boton_borrar_todo = ttk.Button(mainframe, text="AC", command=lambda: borrar_todo(), style='Botones_Borrar.TButton')

Boton_Division = ttk.Button(mainframe, text=chr(247), command=lambda: Obtener('/'), style='Botones_Operadores.TButton')
Boton_multiplica = ttk.Button(mainframe, text="x", command=lambda: Obtener('*'), style='Botones_Operadores.TButton')
Boton_Suma = ttk.Button(mainframe, text="+", command=lambda: Obtener('+'), style='Botones_Operadores.TButton')
Boton_Resta = ttk.Button(mainframe, text="-", command=lambda: Obtener('-'), style='Botones_Operadores.TButton')
Boton_raiz = ttk.Button(mainframe, text="√", command=lambda: Obtener('**(1/2)'),  style='Botones_Operadores.TButton')
Boton_cuadrado = ttk.Button(mainframe, text="X²", command=lambda: Obtener('**2'), style='Botones_Operadores.TButton')
Boton_Igual = ttk.Button(mainframe, text="=", command=lambda: operacion(), style='Botones_Operadores.TButton')


#Mostremos todo en el frame cargamos los botones
#entrada_texto.grid(column=0, row=0)

Boton_cuadrado.grid(column=0, row=0, sticky= ("W, N, E, S"))
Boton_abrir_parentesis.grid(column=1, row=0, sticky= ("W, N, E, S"))
Boton_cerrar_parentesis.grid(column=2, row=0, sticky= ("W, N, E, S"))
Boton_borrar_todo.grid(column=3, row=0, sticky= ("W, N, E, S"))
Boton_borrar.grid(column=2, row=5, sticky= ("W, N, E, S"))

Boton9.grid(column=2 , row=1, sticky= ("W, N, E, S"))
Boton8.grid(column=1 , row=1, sticky= ("W, N, E, S"))
Boton7.grid(column=0, row=1, sticky= ("W, N, E, S"))

Boton6.grid(column=2, row=2, sticky= ("W, N, E, S"))
Boton5.grid(column=1 , row=2, sticky= ("W, N, E, S"))
Boton4.grid(column=0, row=2, sticky= ("W, N, E, S"))

Boton3.grid(column=2, row=3, sticky= ("W, N, E, S"))
Boton2.grid(column=1 , row=3, sticky= ("W, N, E, S"))
Boton1.grid(column=0 , row=3, sticky= ("W, N, E, S"))

Boton0.grid(column=0 , row=4, columnspan=2, sticky= ("W, N, E, S"))
Botonpunto.grid(column=2 , row=4, sticky= ("W, N, E, S"))

#Botones de operaciones
Boton_Division.grid(column=3, row=1, sticky= ("W, N, E, S"))
Boton_multiplica.grid(column=3, row=2, sticky= ("W, N, E, S"))
Boton_Suma.grid(column=3, row=3, sticky= ("W, N, E, S"))
Boton_Resta.grid(column=3, row=4, sticky= ("W, N, E, S"))

Boton_Igual.grid(column=0, row=5, columnspan=2, sticky= ("W, N, E, S"))
Boton_raiz.grid(column=3, row=5, sticky= ("W, N, E, S"))

#ventana_calculadoraC = tk()
#ventana_calculadoraC.title("Calculadora Cientifica")

#ventana_calculadoraC.mainloop()
for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)


ventana_calculadoraB.mainloop()
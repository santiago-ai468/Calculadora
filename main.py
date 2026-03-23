import tkinter as tk


# funcion para actualizar la pantalla

def click_boton(valor):
    actual= pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, str(actual) + str(valor))


# funcion para calcular el resultado

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        
        pantalla.delete(0, tk.End)
        pantalla.insert(0, 'ERROR')


# funcion para borrar

def borrrar():
    pantalla.delete(0, tk.END)


# configuracion ventana

ventana = tk.Tk()
ventana.title('Calculadora')


# pantalla

pantalla = tk.Entry(ventana, width=25, font=('Arial', 16), justify='right')
pantalla.grid(row=0, column=0, columnspan=4)


# botones

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

fila = 1
col = 0
for boton in botones:

    comando = lambda x=boton: click_boton(x)
    if boton == '=': comando = calcular
    elif boton == 'C': comando = borrrar
    tk.Button(ventana, text=boton, width=5, command=comando).grid(row=fila, column=col)
    col += 1
    if col > 3:
        col = 0
        fila += 1


ventana.mainloop()
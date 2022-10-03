from cgitb import text
from tkinter import Tk,Text,Button,END,re

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Calculadora")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(self.ventana, state="disabled", width=40, height=3, background="black", foreground="white", font=("Helvetica",15))

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""

        #Crear los botones de la calculadora
        boton1=self.crearBoton(7)
        boton2=self.crearBoton(8)
        boton3=self.crearBoton(9)
        boton4=self.crearBoton(u"\u232B",escribir=False)
        boton5=self.crearBoton(4)
        boton6=self.crearBoton(5)
        boton7=self.crearBoton(6)
        boton8=self.crearBoton(u"\u00F7")
        boton9=self.crearBoton(1)
        boton10=self.crearBoton(2)
        boton11=self.crearBoton(3)
        boton12=self.crearBoton("*")
        boton13=self.crearBoton(".")
        boton14=self.crearBoton(0)
        boton15=self.crearBoton("+")
        boton16=self.crearBoton("-")
        boton17=self.crearBoton("=",escribir=False,ancho=20,alto=2)
        #Ubicar los botones con el gestor grid 
        botones = [boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17]
        #Inicializar el contador en 0
        Contador = 0
        #Bucle for para definir un rango
        for fila in range (1,5):
            #Anidar bucle for 
            for columna in range (4):
                botones [Contador].grid(row = fila, column = columna)
                Contador+= 1

            #Ubicar el ultimo boton al final
        botones[16].grid(row = 5, column = 0, columnspan = 4)
        return 
    #Crear un boton mo0strando el valor pasado por el parametro 
    def crearBoton(self,valor,escribir = True, ancho=9, alto=1):
        return Button (self.ventana, text=valor, width=ancho, height= alto, font=("Helvetica",15), command=lambda:self.click(valor, escribir))  

    #Controla el evento disparado al hacer click en un boton
    def click (self, texto, escribir):
        #Si el parametro escribir es true entonces el parametro del texto debe mostrarse en pantalla, si es false no debe mostrarse en pantalla
        if not escribir:
            #Solo calcular cuando hay una operación a ser evaluada y si el usuario presiona el simbolo igual 
            if texto == "=" and self.operacion != "":
                #Remplazar el valor unicode de la divición por el operador divición de phyton "/"
                self.operacion = re.sub(u"\u00F7", "/", self.operacion) 
                resultado= str(eval(self.operacion))
                self.operacion = ""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            #Si se presiono el boton de borrar se debe de limpiar la pantalla
            elif texto == u"\u232B":
                self.operacion = ""
                self.limpiarPantalla()
         #Mostar texto
        else:
            self.operacion += str(texto)
            self.mostrarEnPantalla(texto)
        return
    #Borrar el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state = "normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state = "disabled")
        return

    #Muestra en la pantalla de la calculadora el cobntenido de las operaciones y los resultados 
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state = "normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state = "disabled")
        return

ventana_principal = Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop() 
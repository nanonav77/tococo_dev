from tkinter import *
from tkinter import ttk

class FrameOrder(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        initframe = Frame(self, bg='#BDC3C7',width=420,height=500)
        initframe.place(x=280, y=105) 

        ## Indicamos la etiqueta inicial de número de orden        
        varOrder   = StringVar() 
        labelOrder = Label(initframe, textvariable=varOrder,bg='#BDC3C7',fg='#454545')
        labelOrder.config(font=("Courier", 15,'bold')) 
        labelOrder.place(x=18, y=16)
        varOrder.set('Número de Orden: 0000')
        ## Indicamos la etiqueta inicial de número de orden 
        
        
        ## Enlistamos los elementos que componen los radio button de categoría
        labelCategoria = Label(initframe, text="Categoría:",bg='#BDC3C7',fg='#454545')
        labelCategoria.config(font=("Courier", 11,'bold'))
        labelCategoria.place(x=20, y=50)
                 
 
        radioCategoria = IntVar()

        ## Función para filtrar los productos según la categoría seleccionada
        def filtrarCategoria():
            print(radioCategoria.get())
        ## Función para filtrar los productos según la categoría seleccionada

        rdioArroz = Radiobutton(initframe, text='Arroz',fg='#454545', command=filtrarCategoria,
                                    variable=radioCategoria, value=1,bg='#BDC3C7',highlightthickness=0).place(x=20, y=70) 
        rdioPapas = Radiobutton(initframe, text='Papas',fg='#454545', command=filtrarCategoria,
                                    variable=radioCategoria, value=2,bg='#BDC3C7',highlightthickness=0).place(x=20, y=95) 
        rdioTacos = Radiobutton(initframe, text='Tacos',fg='#454545', command=filtrarCategoria,
                                    variable=radioCategoria, value=3,bg='#BDC3C7',highlightthickness=0).place(x=20, y=120) 
        rdioPollo = Radiobutton(initframe, text='Pollo',fg='#454545', command=filtrarCategoria,
                                    variable=radioCategoria, value=4,bg='#BDC3C7',highlightthickness=0).place(x=20, y=145)
        rdioHamburguesas = Radiobutton(initframe, text='Hamburguesas',fg='#454545', command=filtrarCategoria,
                                    variable=radioCategoria, value=5,bg='#BDC3C7',highlightthickness=0).place(x=20, y=170)
        rdioNachos = Radiobutton(initframe, text='Nachos',fg='#454545', command=filtrarCategoria,
                                    variable=radioCategoria, value=6,bg='#BDC3C7',highlightthickness=0).place(x=20, y=195)
        rdioCarnes = Radiobutton(initframe, text='Carnes',fg='#454545', command=filtrarCategoria,
                                    variable=radioCategoria, value=7,bg='#BDC3C7',highlightthickness=0).place(x=20, y=220)
        rdioCombos = Radiobutton(initframe, text='Combos',fg='#454545', command=filtrarCategoria,
                                    variable=radioCategoria, value=8,bg='#BDC3C7',highlightthickness=0).place(x=20, y=245)
        ## Enlistamos los elementos que componen los radio button de categoría

        ## Enlistamos los elementos que componen el selector de productos
        labelProducto = Label(initframe, text="Producto:",bg='#BDC3C7',fg='#454545')
        labelProducto.config(font=("Courier", 11,'bold'))
        labelProducto.place(x=215, y=50)

        listboxProductos = Listbox(initframe,width=22,height=9)
        listboxProductos.insert(1, "Python")
        listboxProductos.insert(2, "Perl")
        listboxProductos.insert(3, "C")
        listboxProductos.insert(4, "PHP")
        listboxProductos.insert(5, "JSP")
        listboxProductos.insert(6, "Ruby")
        listboxProductos.insert(7, "PHP")
        listboxProductos.insert(8, "JSP")
        listboxProductos.insert(9, "Ruby")
        listboxProductos.place(x=215, y=75)
        ## Enlistamos los elementos que componen el selector de productos

        ## BOTONES PARA AGREGAR, DESAGREGAR Y LIMPIAR PRODUCTOS A UNA ORDEN ##
        
        buttonAdd = Button(initframe, width=11,height=1, bg='#229954', bd=0,highlightbackground="#454545",borderwidth=0,text="Añadir...",command=agregarProducto)
        buttonAdd.place(x=30, y=280)

        buttonRemove = Button(initframe, width=11,height=1, bg='#A93226', bd=0,highlightbackground="#454545",borderwidth=0, text="Eliminar..",command=eliminarProducto)
        buttonRemove.place(x=155, y=280)

        buttonClean = Button(initframe, width=11,height=1, bg='#2E86C1', bd=0,highlightbackground="#454545",borderwidth=0, text="Limpiar..",command=limpiarOrden)
        buttonClean.place(x=281, y=280)
        
        ## BOTONES PARA AGREGAR, DESAGREGAR Y LIMPIAR PRODUCTOS A UNA ORDEN ##
    

if __name__ == "__main__":
    app = FrameOrder(None)
    app.title('Initial')
    app.mainloop()



## Inicializamos función para agregar un producto a la lista
def agregarProducto():
    print("nano")


## Inicializamos función para eliminar un producto a la lista
def eliminarProducto():
    print("nano")

## Inicializamos función para limpiar la orden total
def limpiarOrden():
    print("nano")
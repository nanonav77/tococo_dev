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
        labelOrder.place(x=10, y=18)
        varOrder.set('Número de Orden: 0000')
        ## Indicamos la etiqueta inicial de número de orden 
        
        
        ## Enlistamos los elementos que componen los radio button de categoría
        labelCategoria = Label(initframe, text="Categoría:",bg='#BDC3C7',fg='#454545')
        labelCategoria.config(font=("Courier", 11,'bold'))
        labelCategoria.place(x=20, y=50)
        
        radioCategoria = IntVar() 
 
        rdioArroz = Radiobutton(initframe, text='Arroz',fg='#454545',
                                    variable=radioCategoria, value=1,bg='#BDC3C7',highlightthickness=0).place(x=20, y=70) 
        rdioPapas = Radiobutton(initframe, text='Papas',fg='#454545',
                                    variable=radioCategoria, value=2,bg='#BDC3C7',highlightthickness=0).place(x=20, y=95) 
        rdioTacos = Radiobutton(initframe, text='Tacos',fg='#454545',
                                    variable=radioCategoria, value=3,bg='#BDC3C7',highlightthickness=0).place(x=20, y=120) 
        rdioPollo = Radiobutton(initframe, text='Pollo',fg='#454545',
                                    variable=radioCategoria, value=4,bg='#BDC3C7',highlightthickness=0).place(x=20, y=145)
        rdioHamburguesas = Radiobutton(initframe, text='Hamburguesas',fg='#454545',
                                    variable=radioCategoria, value=5,bg='#BDC3C7',highlightthickness=0).place(x=20, y=170)
        rdioNachos = Radiobutton(initframe, text='Nachos',fg='#454545',
                                    variable=radioCategoria, value=6,bg='#BDC3C7',highlightthickness=0).place(x=20, y=195)
        rdioCarnes = Radiobutton(initframe, text='Carnes',fg='#454545',
                                    variable=radioCategoria, value=7,bg='#BDC3C7',highlightthickness=0).place(x=20, y=220)
        rdioCombos = Radiobutton(initframe, text='Combos',fg='#454545',
                                    variable=radioCategoria, value=8,bg='#BDC3C7',highlightthickness=0).place(x=20, y=245)
        ## Enlistamos los elementos que componen los radio button de categoría

        ## Enlistamos los elementos que componen el selector de productos
        labelProducto = Label(initframe, text="Producto:",bg='#BDC3C7',fg='#454545')
        labelProducto.config(font=("Courier", 11,'bold'))
        labelProducto.place(x=215, y=50)

        listboxProductos = Listbox(initframe,width=22,height=7)
        listboxProductos.insert(1, "Python")
        listboxProductos.insert(2, "Perl")
        listboxProductos.insert(3, "C")
        listboxProductos.insert(4, "PHP")
        listboxProductos.insert(5, "JSP")
        listboxProductos.insert(6, "Ruby")
        listboxProductos.insert(7, "PHP")
        listboxProductos.insert(8, "JSP")
        listboxProductos.insert(9, "Ruby")
        listboxProductos.place(x=215, y=70)
        ## Enlistamos los elementos que componen el selector de productos

        ## BOTONES PARA AGREGAR, DESAGREGAR Y LIMPIAR PRODUCTOS A UNA ORDEN ##
        buttonAC = Button(initframe, width=4,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0,text="Add")
        buttonAC.place(x=215, y=220)

        buttonAP = Button(initframe, width=4,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Rem")
        buttonAP.place(x=276, y=220)

        buttonMP = Button(initframe, width=4,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Mod")
        buttonMP.place(x=338, y=220)
        
        ## BOTONES PARA AGREGAR, DESAGREGAR Y LIMPIAR PRODUCTOS A UNA ORDEN ##


if __name__ == "__main__":
    app = FrameOrder(None)
    app.title('Initial')
    app.mainloop()
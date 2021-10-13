from tkinter import *
from tkinter import ttk

class FrameHistory(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        initframe = Frame(self, bg='#BDC3C7',width=560,height=500)
        initframe.place(x=650, y=91)

        ## Indicamos la etiqueta inicial de número de orden        
        varHistory   = StringVar() 
        labelHistory = Label(initframe, textvariable=varHistory,bg='#BDC3C7',fg='#454545')
        labelHistory.config(font=("Courier", 15,'bold')) 
        labelHistory.place(x=18, y=16)
        varHistory.set('Historial de Ordenes')
        ## Indicamos la etiqueta inicial de número de orden 
        
        buttonPagar = Button(initframe, width=3,height=1, bg='#229954', bd=0,highlightbackground="#229954",borderwidth=0)
        buttonPagar.place(x=18, y=74)

        buttonExportarExcel = Button(initframe, width=20,height=1, bg='#229954', bd=0,highlightbackground="#229954",borderwidth=0, text="Exportar a Excel...")
        buttonExportarExcel.place(x=71, y=74)

        buttonBuscarOrden = Button(initframe, width=12,height=1, bg='#2E86C1', bd=0,highlightbackground="#2E86C1",borderwidth=0, text="Buscar Orden...")
        buttonBuscarOrden.place(x=260, y=74)

        buttonEliminarOrden = Button(initframe, width=16,height=1, bg='#A93226', bd=0,highlightbackground="#A93226",borderwidth=0, text="Eliminar Orden...")
        buttonEliminarOrden.place(x=387, y=74)         

        ## TABLA PARA VISUALIZAR EL HISTORIAL DE LAS ÓRDENES
        tablaHistorial = ttk.Treeview(initframe, column=("N°","Cliente", "Fecha", "Total","Estado"), show='headings', height=18)
        tablaHistorial.column("# 1", anchor=CENTER, width=50)
        tablaHistorial.heading("# 1", text="N°")
        tablaHistorial.column("# 2", anchor=CENTER, width=190)
        tablaHistorial.heading("# 2", text="Cliente")
        tablaHistorial.column("# 3", anchor=CENTER, width=125)
        tablaHistorial.heading("# 3", text="Fecha")
        tablaHistorial.column("# 4", anchor=CENTER, width=80)
        tablaHistorial.heading("# 4", text="Total")  
        tablaHistorial.column("# 5", anchor=CENTER, width=80)
        tablaHistorial.heading("# 5", text="Estado")         
        tablaHistorial.place(x=18, y=110)    

        tablaHistorial.insert('', 'end', text="1", values=('005','Daniel Navarro',"12/08/2021 12:00","10800"))      

if __name__ == "__main__":
    app = FrameHistory(None)
    app.title('Initial')
    app.mainloop()
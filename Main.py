from tkinter import *

root = Tk()                            # Llame al método Tk () para inicializar una instancia de formulario raíz
root.title('Sistema Tococo')           # método title () para establecer el texto del título
root.geometry('1240x650')              # geometry () establece el tamaño de la ventana, el signo de multiplicación aquí no es *, sino la letra x minúscula en inglés
root.configure(background="#ABB2B9")
root.resizable(False, False)

## COLOCAR IMAGEN DE ICON EN VENTANA PRINCIPAL ##

## COLOCAR IMAGEN DE ICON EN VENTANA PRINCIPAL ##

## FRAMES CONTENIDOS EN LA VENTANA PRINCIPAL ##
frameH = Frame(root, height=70, bg='#353535')
frameH.pack_propagate(0)
frameH.pack(side='top', padx=0, pady=0, anchor='w', fill='x')

frameV = Frame(root, width=250, bg='#454545')
frameV.pack_propagate(0)
frameV.pack(side='left', padx=0, pady=0, anchor='w', fill='y')

frameOrder = Frame(root, width=420,height=500, bg='#BDC3C7')
frameOrder.place(x=280, y=100)

frameHistory = Frame(root, width=480,height=500, bg='#BDC3C7')
frameHistory.place(x=730, y=100)
## FRAMES CONTENIDOS EN LA VENTANA PRINCIPAL ##

## BOTONES INCLUIDOS EN EL FRAME VERTICAL (BOTONES DEL MENU) ##
buttonAC = Button(frameV, width=28,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0,text="Agregar Categoría")
buttonAC.place(x=0, y=32)

buttonAP = Button(frameV, width=28,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Agregar Producto")
buttonAP.place(x=0, y=90)

buttonMP = Button(frameV, width=28,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Modificar Producto")
buttonMP.place(x=0, y=148)

buttonCV = Button(frameV, width=28,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Consultar Ventas")
buttonCV.place(x=0, y=206)
## BOTONES INCLUIDOS EN EL FRAME VERTICAL (BOTONES DEL MENU) ##


root.mainloop()


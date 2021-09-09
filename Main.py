from tkinter import *
from FrameOrder import FrameOrder
from FrameHistory import FrameHistory
from PIL import Image, ImageTk

root = Tk()                            # Llame al método Tk () para inicializar una instancia de formulario raíz
root.title('Sistema Tococo')           # método title () para establecer el texto del título
root.geometry('1240x650')              # geometry () establece el tamaño de la ventana, el signo de multiplicación aquí no es *, sino la letra x minúscula en inglés
root.configure(background="#ABB2B9")
root.resizable(False, False)

## COLOCAR IMAGEN DE ICONO GENERAL ##
renderIcono = ImageTk.PhotoImage(Image.open("./images/pp.jpeg"))
root.iconphoto(False, renderIcono)
## COLOCAR IMAGEN DE ICONO GENERAL ##

## FRAMES CONTENIDOS EN LA VENTANA PRINCIPAL ##
frameV = Frame(root, width=250, bg='#454545')
frameV.pack_propagate(0)
frameV.pack(side='left', padx=0, pady=0, anchor='w', fill='y')

frameH = Frame(root, height=70, bg='#353535')
frameH.pack_propagate(0)
frameH.pack(side='top', padx=0, pady=0, anchor='w', fill='x')

## Frames de Orden de Compra e Historial
FrameOrder.initialize(root)
FrameHistory.initialize(root)

## FRAMES CONTENIDOS EN LA VENTANA PRINCIPAL ##

## COLOCAR IMAGEN DE ICON EN VENTANA PRINCIPAL ##
renderPagina = ImageTk.PhotoImage(Image.open("./images/ww.jpg"))
imagenPagina = Label(frameV, image=renderPagina,width=170,height=90)
imagenPagina.place(x=37, y=7)
## COLOCAR IMAGEN DE ICON EN VENTANA PRINCIPAL ##

## BOTONES INCLUIDOS EN EL FRAME VERTICAL (BOTONES DEL MENU) ##
buttonAC = Button(frameV, width=28,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0,text="Agregar Categoría")
buttonAC.place(x=0, y=105)

buttonAP = Button(frameV, width=28,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Agregar Producto")
buttonAP.place(x=0, y=163)

buttonMP = Button(frameV, width=28,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Modificar Producto")
buttonMP.place(x=0, y=221)

buttonCV = Button(frameV, width=28,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Consultar Ventas")
buttonCV.place(x=0, y=274)
## BOTONES INCLUIDOS EN EL FRAME VERTICAL (BOTONES DEL MENU) ##


root.mainloop()


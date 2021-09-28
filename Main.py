from tkinter import *
from FrameOrder import FrameOrder
from FrameHistory import FrameHistory
from PIL import Image, ImageTk

root = Tk()                            # Llame al método Tk () para inicializar una instancia de formulario raíz
root.title('Sistema Tococo')

ancho_ventana = 1240
alto_ventana = 650

x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
root.configure(background="#ABB2B9")
root.resizable(False, False)

## COLOCAR IMAGEN DE ICONO GENERAL ##
renderIcono = ImageTk.PhotoImage(Image.open("./images/pp.jpeg"))
root.iconphoto(False, renderIcono)
## COLOCAR IMAGEN DE ICONO GENERAL ##

## FRAMES CONTENIDOS EN LA VENTANA PRINCIPAL ##
frameH = Frame(root, height=70, bg='#353535')
frameH.pack_propagate(0)
frameH.pack(side='top', padx=0, pady=0, anchor='w', fill='x')

frameV = Frame(root, width=173, bg='#454545')
frameV.pack_propagate(0)
frameV.pack(side='left', padx=0, pady=0, anchor='w', fill='y')

## Frames de Orden de Compra e Historial
FrameOrder.initialize(root)
FrameHistory.initialize(root)

## FRAMES CONTENIDOS EN LA VENTANA PRINCIPAL ##

## COLOCAR IMAGEN DE ICON EN VENTANA PRINCIPAL ##
renderPagina = ImageTk.PhotoImage(Image.open("./images/ww.jpg"))
imagenPagina = Label(frameH, image=renderPagina,width=170,height=90)
imagenPagina.place(x=1, y=1)
## COLOCAR IMAGEN DE ICON EN VENTANA PRINCIPAL ##

## BOTONES INCLUIDOS EN EL FRAME VERTICAL (BOTONES DEL MENU) ##
buttonAC = Button(frameV, width=19,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0,text="Agregar Categoría")
buttonAC.place(x=0, y=20)

buttonAP = Button(frameV, width=19,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Agregar Producto")
buttonAP.place(x=0, y=78)

buttonMP = Button(frameV, width=19,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Modificar Producto")
buttonMP.place(x=0, y=136)

buttonCV = Button(frameV, width=19,height=2, bg='#454545', bd=0,highlightbackground="#454545",borderwidth=0, text="Consultar Ventas")
buttonCV.place(x=0, y=194)
## BOTONES INCLUIDOS EN EL FRAME VERTICAL (BOTONES DEL MENU) ##


root.mainloop()


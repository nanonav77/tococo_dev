import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="tococo_db"
)

class DBConsulta(object):

  def obtenerProductosCategoria(self,id_categoria):

    listaProductos = []
    
    consulta = mydb.cursor()

    consulta.execute("SELECT * FROM toc_producto where id_categoria = " + str(id_categoria))

    productos = consulta.fetchall()

    for x in productos:
      
      listaProductos.append(x)    

    return listaProductos

  
  def informacionProducto(sefl,producto):

    datosProducto = []

    consulta = mydb.cursor()

    consulta.execute("SELECT * FROM toc_producto where producto = '" + producto +"'")

    producto = consulta.fetchall()

    for x in producto:
      
      datosProducto.append(x)

    return datosProducto[0]

db = DBConsulta()
db.informacionProducto("Porción Sencilla")
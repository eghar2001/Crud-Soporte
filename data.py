import sqlite3
from model import Producto


LEN_MAX_NOMBRE = 100

class ProductoNoEncontradoException(Exception):
   pass


class ProductoData:
   def get_one(self,id:int):
      conn = sqlite3.connect("app.db")
      cursor = conn.cursor()
      producto = cursor.execute("""
                    SELECT * FROM productos
                    WHERE id = :id_prod
                    """, {"id_prod":id}).fetchone()
      if not producto:
         raise ProductoNoEncontradoException
      producto = Producto(nombre=producto[1], cantidad=producto[2], precio=producto[3], id=producto[0])
      conn.commit()
      conn.close()
      return producto



   def crear_producto(self, producto: Producto):
      conn = sqlite3.connect("app.db")
      cursor = conn.cursor()
      cursor.execute("""
          INSERT INTO productos
          (nombre, cantidad, precio)
          VALUES
          (?,?,?)""", (producto.nombre, producto.cantidad, producto.precio))
      product_con_id = Producto(nombre= producto.nombre, cantidad= producto.cantidad, precio = producto.precio, id = cursor.lastrowid)
      conn.commit()
      conn.close()
      return product_con_id


   def find_all(self):
      conn = sqlite3.connect("app.db")
      cursor = conn.cursor()
      productos = cursor.execute("""
              SELECT * FROM productos
              """).fetchall()
      productos = [Producto(nombre= producto[1], cantidad= producto[2], precio = producto[3], id =producto[0] ) for producto in productos]
      conn.commit()
      conn.close()
      return productos

   def borrar_producto(self, producto:Producto):
      conn = sqlite3.connect("app.db")
      cursor = conn.cursor()
      cursor.execute("""
              DELETE FROM productos WHERE id = :id_prod
              """, {"id_prod":producto.id})
      conn.commit()
      conn.close()

   def editar_producto(self, producto:Producto):
      conn = sqlite3.connect("app.db")
      cursor = conn.cursor()

      cursor.execute("""
    UPDATE productos SET nombre = :nombre_prod, cantidad = :cantidad_prod, precio = :precio_prod
    WHERE id = :id_prod
""", {"nombre_prod": producto.nombre, "cantidad_prod": producto.cantidad, "precio_prod": producto.precio,
      "id_prod": producto.id})
      conn.commit()
      conn.close()

if __name__ == "__main__":
   conn = sqlite3.connect("app.db")
   cursor = conn.cursor()
   cursor.execute(f"""CREATE TABLE IF NOT EXISTS productos (
            id integer PRIMARY KEY AUTOINCREMENT,
            nombre varchar({LEN_MAX_NOMBRE}),
            cantidad int,
            precio float  )""")

   conn.commit()
   conn.close()
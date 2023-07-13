from kivy.app import App
from model import Producto
from logica import ProductoLogic


class Formulario(App):
    producto_logic = ProductoLogic()

    productos = producto_logic.find_all()
    def enviar(self):


        producto = Producto(
            nombre=self.root.ids.nombre.text,
            cantidad = int(self.root.ids.cantidad.text),
            precio = float(self.root.ids.precio.text)
        )

        producto = self.producto_logic.crear_producto(producto)

        self.root.ids.recycle_productos.data.append(producto.get_data())
        print("Se ha creado un producto con exito!!")
        self.borrar()

    def borrar(self):
        self.root.ids.nombre.text = ""
        self.root.ids.cantidad.text = ""
        self.root.ids.precio.text = ""

    def actualizar_productos(self):
        self.productos = self.producto_logic.find_all()

    def buscar_productos(self):
        return self.producto_logic.find_all()


    pass


if __name__ == "__main__":
    Formulario().run()

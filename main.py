from kivy.app import App
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.button import Button
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from model import Producto
from logica import ProductoLogic
import re



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

    def cargar_lista(self):
        self.root.ids.recycle_productos.data = [{"text":producto.get_text(),"id":producto.id} for producto in self.buscar_productos()]

    def editar(self, id:int):
        print("se esta ejecutando el editar")
        print(id)
    pass


if __name__ == "__main__":
    Formulario().run()

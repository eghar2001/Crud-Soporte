from kivy.app import App
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.button import Button
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from data import ProductoNoEncontradoException
from model import Producto
from logica import ProductoLogic
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout



class RecyclableButton(RecycleDataViewBehavior, Button):

    def on_press(self):
        App.get_running_app().editar_o_eliminar(self.id)

def windows_error(title:str, mensaje:str):
    popup = Popup(title=title, size_hint=(None, None), size=(400, 200))
    label = Label(text=mensaje)
    button = Button(text='Cerrar', size_hint=(None, None), size=(100, 50))
    button.bind(on_release=popup.dismiss)

    box_layout = BoxLayout(orientation='vertical')
    box_layout.add_widget(label)
    box_layout.add_widget(button)

    popup.content = box_layout
    popup.open()

def editar(id_prod):
    print(id_prod)

class Formulario(App):
    producto_logic = ProductoLogic()
    producto_actual:Producto
    productos = producto_logic.find_all()
    def agregar_producto(self):
        try:
            producto = Producto(
                nombre=self.root.ids.nombre_agregar.text,
                cantidad = int(self.root.ids.cantidad_agregar.text),
                precio = float(self.root.ids.precio_agregar.text)
            )
            self.producto_logic.crear_producto(producto)

        except Exception:
            windows_error('Error', 'Ningún campo debe estar vacío')



        print("Se ha creado un producto con exito!!")







    def buscar_productos(self):
        return self.producto_logic.find_all()

    def cargar_lista(self):
        self.root.ids.recycle_productos.data = [{"text":producto.get_text(),"id":producto.id} for producto in self.buscar_productos()]


    def borrar_producto(self):
        self.producto_logic.borrar_producto(self.producto_actual)
        self.cargar_lista()
        print("Se ha borrado con exito!!!")

    def cargar_editar(self):
        self.root.ids.nombre_editar.text = self.producto_actual.nombre
        self.root.ids.cantidad_editar.text = str(self.producto_actual.cantidad)
        self.root.ids.precio_editar.text = str(self.producto_actual.precio)

    def editar_o_eliminar(self, id:int):
        id_prod = int(id)

        try:
            self.producto_actual = self.producto_logic.get_one(id_prod)

            self.root.current = "producto_editar_o_eliminar"
            self.root.transition.direction = "left"
        except ProductoNoEncontradoException:
            pass

    def editar_producto(self):
        try:
            self.producto_actual.nombre= self.root.ids.nombre_editar.text
            self.producto_actual.cantidad = int(self.root.ids.cantidad_editar.text)
            self.producto_actual.precio = float(self.root.ids.precio_editar.text)
            self.producto_logic.editar_producto(self.producto_actual)
            print("Se ha editado el producto")
        except Exception:
            windows_error('Error', 'Error en algun campo')

    def borrar_producto_actual(self):
        self.producto_actual = None
    pass


if __name__ == "__main__":
    Formulario().run()

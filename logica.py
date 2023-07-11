from model import Producto
from data import ProductoData


class ProductoLogic:
    producto_data = ProductoData()
    def crear_producto(self, producto:Producto):
        def validar_nombre(nombre:str):
            if 3<= len(nombre) <= 20:
                return True
            print("por nombre")
            raise Exception
        if validar_nombre(producto.nombre)  :
            return self.producto_data.crear_producto(producto)



    def find_all(self):
        productos = self.producto_data.find_all()
        return productos

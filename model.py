from dataclasses import dataclass

from unicodedata import decimal


@dataclass
class Producto:
    _id: int
    _nombre: str
    _cantidad: int
    _precio: float

    def __init__(self, nombre:str, cantidad:int, precio :float,id:int = None):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def __str__(self):
        return f"Producto<id:{self.id},nombre: {self.nombre},cantidad:{self.cantidad}, precio: {self.precio}>"

    def __repr__(self):
        return f"Producto<id:{self.id},nombre: {self.nombre},cantidad:{self.cantidad}, precio: {self.precio}>"

    def get_text(self):
        return f"{self.nombre} x {self.cantidad} -- ${self.precio}"




    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def precio(self) -> float:
        return round(self._precio,2)

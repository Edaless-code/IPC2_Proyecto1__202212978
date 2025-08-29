from .nodo import Nodo

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def recorrer(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

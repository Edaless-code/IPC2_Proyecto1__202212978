class Estacion:
    def __init__(self, id_estacion, nombre):
        self.id_estacion = id_estacion
        self.nombre = nombre

    def __str__(self):
        return f"Estacion({self.id_estacion}, {self.nombre})"

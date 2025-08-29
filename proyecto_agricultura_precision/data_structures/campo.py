from .lista import Lista

class Campo:
    def __init__(self, id_campo, nombre):
        self.id_campo = id_campo
        self.nombre = nombre
        self.estaciones = Lista()        # Lista de Estacion
        self.sensores_suelo = Lista()    # Lista de SensorSuelo
        self.sensores_cultivo = Lista()  # Lista de SensorCultivo

    def __str__(self):
        return f"Campo({self.id_campo}, {self.nombre})"

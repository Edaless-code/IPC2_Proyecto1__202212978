class SensorSuelo:
    def __init__(self, id_sensor, nombre):
        self.id_sensor = id_sensor
        self.nombre = nombre
        # Diccionario: idEstacion -> frecuencia
        self.frecuencias = {}

    def __str__(self):
        return f"SensorSuelo({self.id_sensor}, {self.nombre}, frecs={self.frecuencias})"

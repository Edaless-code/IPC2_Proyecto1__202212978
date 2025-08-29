import xml.etree.ElementTree as ET
from data_structures.campo import Campo
from data_structures.estacion import Estacion
from data_structures.sensor_suelo import SensorSuelo
from data_structures.sensor_cultivo import SensorCultivo
from data_structures.lista import Lista

# Lista global de campos agrícolas
lista_campos = Lista()

def cargar_archivo():
    ruta = input("Ingrese la ruta del archivo: ").strip()
    nombre = input("Ingrese el nombre del archivo: ").strip()
    archivo = f"{ruta}/{nombre}"

    try:
        tree = ET.parse(archivo)
        root = tree.getroot()

        for campo_xml in root.findall("campo"):
            id_campo = campo_xml.get("id")
            nombre_campo = campo_xml.get("nombre")
            print(f"➢ Cargando {nombre_campo}")

            campo_obj = Campo(id_campo, nombre_campo)

            # Estaciones base
            estaciones_xml = campo_xml.find("estacionesBase")
            if estaciones_xml is not None:
                for est_xml in estaciones_xml.findall("estacion"):
                    id_est = est_xml.get("id")
                    nombre_est = est_xml.get("nombre")
                    print(f"➢ Creando estación base {id_est}")
                    campo_obj.estaciones.agregar(Estacion(id_est, nombre_est))

            # Sensores de suelo
            sensores_suelo_xml = campo_xml.find("sensoresSuelo")
            if sensores_suelo_xml is not None:
                for sensor_xml in sensores_suelo_xml.findall("sensorS"):
                    id_s = sensor_xml.get("id")
                    nombre_s = sensor_xml.get("nombre")
                    sensor_obj = SensorSuelo(id_s, nombre_s)
                    for freq_xml in sensor_xml.findall("frecuencia"):
                        id_est = freq_xml.get("idEstacion")
                        valor = int(freq_xml.text.strip())
                        sensor_obj.frecuencias[id_est] = valor
                    campo_obj.sensores_suelo.agregar(sensor_obj)

            # Sensores de cultivo
            sensores_cultivo_xml = campo_xml.find("sensoresCultivo")
            if sensores_cultivo_xml is not None:
                for sensor_xml in sensores_cultivo_xml.findall("sensorT"):
                    id_t = sensor_xml.get("id")
                    nombre_t = sensor_xml.get("nombre")
                    sensor_obj = SensorCultivo(id_t, nombre_t)
                    for freq_xml in sensor_xml.findall("frecuencia"):
                        id_est = freq_xml.get("idEstacion")
                        valor = int(freq_xml.text.strip())
                        sensor_obj.frecuencias[id_est] = valor
                    campo_obj.sensores_cultivo.agregar(sensor_obj)

            lista_campos.agregar(campo_obj)

        print("✅ Archivo cargado correctamente.")

    except FileNotFoundError:
        print("❌ No se encontró el archivo.")
    except ET.ParseError:
        print("❌ Error al parsear el XML.")

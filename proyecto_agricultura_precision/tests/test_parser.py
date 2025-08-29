import file_io.parser_xml as parser_xml



def probar_parser(): 
    # Llamamos a la función de carga
    parser_xml.cargar_archivo()

    # Recorremos la lista global de campos
    for campo in parser_xml.lista_campos.recorrer():
        print(f"\n=== {campo.nombre} (ID: {campo.id_campo}) ===")

        print("\nEstaciones base:")
        for est in campo.estaciones.recorrer():
            print(f"  - {est.id_estacion}: {est.nombre}")

        print("\nSensores de suelo:")
        for sensor in campo.sensores_suelo.recorrer():
            print(f"  - {sensor.id_sensor}: {sensor.nombre}")
            for id_est, freq in sensor.frecuencias.items():
                print(f"      {id_est} → {freq}")

        print("\nSensores de cultivo:")
        for sensor in campo.sensores_cultivo.recorrer():
            print(f"  - {sensor.id_sensor}: {sensor.nombre}")
            for id_est, freq in sensor.frecuencias.items():
                print(f"      {id_est} → {freq}")

if __name__ == "__main__":
    probar_parser()

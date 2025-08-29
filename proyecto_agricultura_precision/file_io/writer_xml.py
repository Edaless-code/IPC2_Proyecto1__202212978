import xml.etree.ElementTree as ET

def escribir(resultados):
    """
    Genera un archivo XML de salida con las matrices reducidas (Fr)
    y los datos del estudiante.
    """
    ruta = input("Ingrese la ruta donde guardar el archivo: ").strip()
    nombre = input("Ingrese el nombre del archivo de salida (sin extensión): ").strip()
    # Si el usuario no pone .xml, se lo agregamos
    if not nombre.lower().endswith(".xml"):
        nombre += ".xml"

    archivo_salida = f"{ruta}/{nombre}"


    # Nodo raíz
    root = ET.Element("reporte")

    # Datos del estudiante
    estudiante = ET.SubElement(root, "estudiante")
    ET.SubElement(estudiante, "carnet").text = "202212978"
    ET.SubElement(estudiante, "nombre").text = "Edgar Alessandro Chocon Oliva"
    ET.SubElement(estudiante, "curso").text = "Introducción a la Programación y Computación II"
    ET.SubElement(estudiante, "carrera").text = "Ingeniería en Sistemas"
    ET.SubElement(estudiante, "semestre").text = "Segundo Semestre 2025"

    # Campos agrícolas procesados
    for campo_id, datos in resultados.items():
        campo_elem = ET.SubElement(root, "campo", id=campo_id)

        # Estaciones reducidas de suelo
        estaciones_suelo = ET.SubElement(campo_elem, "estacionesReducidasSuelo")
        for idx, grupo in enumerate(datos["grupos_s"]):
            est_elem = ET.SubElement(estaciones_suelo, "grupo", id=f"G{idx+1}")
            est_elem.text = ", ".join(grupo)

        # Matriz Fr[n,s]
        matriz_suelo_elem = ET.SubElement(campo_elem, "matrizSuelo")
        for fila in datos["Fr_s"]:
            fila_elem = ET.SubElement(matriz_suelo_elem, "fila")
            fila_elem.text = " ".join(map(str, fila))

        # Estaciones reducidas de cultivo
        estaciones_cultivo = ET.SubElement(campo_elem, "estacionesReducidasCultivo")
        for idx, grupo in enumerate(datos["grupos_t"]):
            est_elem = ET.SubElement(estaciones_cultivo, "grupo", id=f"G{idx+1}")
            est_elem.text = ", ".join(grupo)

        # Matriz Fr[n,t]
        matriz_cultivo_elem = ET.SubElement(campo_elem, "matrizCultivo")
        for fila in datos["Fr_t"]:
            fila_elem = ET.SubElement(matriz_cultivo_elem, "fila")
            fila_elem.text = " ".join(map(str, fila))

    # Guardar archivo
    tree = ET.ElementTree(root)
    try:
        tree.write(archivo_salida, encoding="utf-8", xml_declaration=True)
        print(f"✅ Archivo XML generado en: {archivo_salida}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")

import sys
import file_io.parser_xml as parser_xml
import file_io.writer_xml as writer_xml
from processing import matrices, agrupamiento
from reports import graficador

# Variables globales para mantener resultados en memoria
resultados = {}

def opcion_cargar():
    parser_xml.cargar_archivo()
    resultados.clear()
    print("✅ Archivo cargado y datos en memoria.")

def opcion_procesar():
    if parser_xml.lista_campos.cabeza is None:
        print("❌ No hay datos cargados. Use la opción 1 primero.")
        return

    for campo in parser_xml.lista_campos.recorrer():
        # Generar matrices F
        est_s, sens_s, Fns = matrices.generar_matriz_suelo(campo)
        est_t, sens_t, Fnt = matrices.generar_matriz_cultivo(campo)

        # Binarizar → Fp
        Fp_s = agrupamiento.binarizar_matriz(Fns)
        Fp_t = agrupamiento.binarizar_matriz(Fnt)

        # Agrupar estaciones
        grupos_s, patrones_s, _ = agrupamiento.agrupar_por_patron(Fp_s, est_s)
        grupos_t, patrones_t, _ = agrupamiento.agrupar_por_patron(Fp_t, est_t)

        # Matrices reducidas Fr
        Fr_s = agrupamiento.generar_matriz_reducida(Fns, grupos_s, est_s)
        Fr_t = agrupamiento.generar_matriz_reducida(Fnt, grupos_t, est_t)

        resultados[campo.id_campo] = {
            "est_s": est_s, "sens_s": sens_s, "Fns": Fns,
            "est_t": est_t, "sens_t": sens_t, "Fnt": Fnt,
            "Fp_s": Fp_s, "Fp_t": Fp_t,
            "grupos_s": grupos_s, "grupos_t": grupos_t,
            "Fr_s": Fr_s, "Fr_t": Fr_t
        }

    print("✅ Procesamiento completado.")

def opcion_escribir():
    if not resultados:
        print("❌ No hay datos procesados. Use la opción 2 primero.")
        return
    writer_xml.escribir(resultados)

def opcion_mostrar_estudiante():
    print("\n👤 Datos del estudiante")
    print("Carnet: 202212978")
    print("1: Edgar Alessandro Chocon Oliva")
    print("Curso: Introducción a la Programación y Computación II")
    print("Carrera: Ingeniería en Sistemas")
    print("Semestre: 2")
    print("Documentación: aun por definir")

def opcion_grafica():
    if not resultados:
        print("❌ No hay datos procesados. Use la opción 2 primero.")
        return

    print("\n=== Campos disponibles ===")
    for cid, datos in resultados.items():
        print(f"- ID: {cid}")

    campo_id = input("Ingrese el ID del campo agrícola que desea graficar: ").strip()

    if campo_id not in resultados:
        print("❌ Campo no encontrado.")
        return

    graficador.generar(resultados[campo_id])


def mostrar_menu():
    print("\n=== Menú principal ===")
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            opcion_cargar()
        elif opcion == "2":
            opcion_procesar()
        elif opcion == "3":
            opcion_escribir()
        elif opcion == "4":
            opcion_mostrar_estudiante()
        elif opcion == "5":
            opcion_grafica()
        elif opcion == "6":
            print("👋 Saliendo...")
            sys.exit()
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()

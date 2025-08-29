import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import file_io.parser_xml as parser_xml
from processing import matrices, agrupamiento

def probar_agrupamiento():
    parser_xml.cargar_archivo()

    for campo in parser_xml.lista_campos.recorrer():
        # Generar F[n,s]
        est_s, sens_s, Fns = matrices.generar_matriz_suelo(campo)
        matrices.imprimir_matriz(est_s, sens_s, Fns, "Matriz F[n,s]")

        # Binarizar → Fp[n,s]
        Fp_s = agrupamiento.binarizar_matriz(Fns, umbral=0)
        matrices.imprimir_matriz(est_s, sens_s, Fp_s, "Matriz Fp[n,s]")

        # Agrupar estaciones por patrón
        grupos, patrones, mapa = agrupamiento.agrupar_por_patron(Fp_s, est_s)
        print("\nGrupos de estaciones (por patrón):")
        for idx, grupo in enumerate(grupos):
            print(f"Grupo {idx+1}: {grupo}  Patrón: {patrones[idx]}")

        # Generar Fr[n,s]
        Fr_s = agrupamiento.generar_matriz_reducida(Fns, grupos, est_s)
        matrices.imprimir_matriz([f"G{idx+1}" for idx in range(len(grupos))], sens_s, Fr_s, "Matriz Fr[n,s]")

if __name__ == "__main__":
    probar_agrupamiento()

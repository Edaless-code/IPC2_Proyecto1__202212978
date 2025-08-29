import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import file_io.parser_xml as parser_xml
from processing import matrices

def probar_matrices():
    parser_xml.cargar_archivo()

    for campo in parser_xml.lista_campos.recorrer():
        est_s, sens_s, Fns = matrices.generar_matriz_suelo(campo)
        matrices.imprimir_matriz(est_s, sens_s, Fns, "Matriz F[n,s]")

        est_t, sens_t, Fnt = matrices.generar_matriz_cultivo(campo)
        matrices.imprimir_matriz(est_t, sens_t, Fnt, "Matriz F[n,t]")

if __name__ == "__main__":
    probar_matrices()

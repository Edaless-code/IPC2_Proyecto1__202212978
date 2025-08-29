import numpy as np

def binarizar_matriz(matriz, umbral=0):
    """
    Convierte la matriz F en Fp:
    - Si valor > umbral → 1
    - Si valor <= umbral → 0
    """
    return (matriz > umbral).astype(int)


def agrupar_por_patron(matriz_binaria, estaciones):
    """
    Agrupa estaciones que tienen el mismo patrón de 0s y 1s.
    Retorna:
    - grupos: lista de listas con IDs de estaciones agrupadas
    - patrones: lista de patrones únicos
    - mapa_estacion_a_grupo: dict para saber a qué grupo pertenece cada estación
    """
    patrones = {}
    grupos = []
    mapa_estacion_a_grupo = {}

    for idx, fila in enumerate(matriz_binaria):
        patron = tuple(fila)
        if patron not in patrones:
            patrones[patron] = len(grupos)
            grupos.append([estaciones[idx]])
        else:
            grupos[patrones[patron]].append(estaciones[idx])
        mapa_estacion_a_grupo[estaciones[idx]] = patrones[patron]

    return grupos, list(patrones.keys()), mapa_estacion_a_grupo


def generar_matriz_reducida(matriz_original, grupos, estaciones):
    """
    Suma las filas de estaciones que pertenecen al mismo grupo para obtener Fr.
    """
    num_grupos = len(grupos)
    num_columnas = matriz_original.shape[1]
    Fr = np.zeros((num_grupos, num_columnas), dtype=int)

    for g_idx, grupo in enumerate(grupos):
        for est in grupo:
            i = estaciones.index(est)
            Fr[g_idx] += matriz_original[i]

    return Fr

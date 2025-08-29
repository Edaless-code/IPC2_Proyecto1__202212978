import numpy as np

def generar_matriz_suelo(campo):
    """
    Genera la matriz F[n,s] para un campo agrícola.
    Filas = estaciones base
    Columnas = sensores de suelo
    """
    estaciones = [est.id_estacion for est in campo.estaciones.recorrer()]
    sensores = [sensor for sensor in campo.sensores_suelo.recorrer()]

    matriz = np.zeros((len(estaciones), len(sensores)), dtype=int)

    for j, sensor in enumerate(sensores):
        for i, est_id in enumerate(estaciones):
            matriz[i, j] = sensor.frecuencias.get(est_id, 0)

    return estaciones, [s.id_sensor for s in sensores], matriz


def generar_matriz_cultivo(campo):
    """
    Genera la matriz F[n,t] para un campo agrícola.
    Filas = estaciones base
    Columnas = sensores de cultivo
    """
    estaciones = [est.id_estacion for est in campo.estaciones.recorrer()]
    sensores = [sensor for sensor in campo.sensores_cultivo.recorrer()]

    matriz = np.zeros((len(estaciones), len(sensores)), dtype=int)

    for j, sensor in enumerate(sensores):
        for i, est_id in enumerate(estaciones):
            matriz[i, j] = sensor.frecuencias.get(est_id, 0)

    return estaciones, [s.id_sensor for s in sensores], matriz


def imprimir_matriz(estaciones, sensores, matriz, titulo):
    """
    Imprime la matriz con etiquetas de estaciones y sensores.
    """
    print(f"\n{titulo}")
    print("      " + "  ".join(f"{s:>6}" for s in sensores))
    for i, est in enumerate(estaciones):
        fila = "  ".join(f"{val:>6}" for val in matriz[i])
        print(f"{est:>6}  {fila}")

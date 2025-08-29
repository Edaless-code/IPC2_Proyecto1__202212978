from graphviz import Digraph
import numpy as np

def generar(datos_campo):
    """
    Genera una gráfica con Graphviz a partir de los datos procesados de un campo.
    El usuario elige si quiere graficar F, Fp o Fr y si es de suelo o cultivo.
    """
    print("\n=== Generar gráfica ===")
    print("1. Matriz F[n,s] (Suelo)")
    print("2. Matriz Fp[n,s] (Suelo binaria)")
    print("3. Matriz Fr[n,s] (Suelo reducida)")
    print("4. Matriz F[n,t] (Cultivo)")
    print("5. Matriz Fp[n,t] (Cultivo binaria)")
    print("6. Matriz Fr[n,t] (Cultivo reducida)")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        estaciones, sensores, matriz = datos_campo["est_s"], datos_campo["sens_s"], datos_campo["Fns"]
    elif opcion == "2":
        estaciones, sensores, matriz = datos_campo["est_s"], datos_campo["sens_s"], datos_campo["Fp_s"]
    elif opcion == "3":
        estaciones = [f"G{i+1}" for i in range(len(datos_campo["grupos_s"]))]
        sensores, matriz = datos_campo["sens_s"], datos_campo["Fr_s"]
    elif opcion == "4":
        estaciones, sensores, matriz = datos_campo["est_t"], datos_campo["sens_t"], datos_campo["Fnt"]
    elif opcion == "5":
        estaciones, sensores, matriz = datos_campo["est_t"], datos_campo["sens_t"], datos_campo["Fp_t"]
    elif opcion == "6":
        estaciones = [f"G{i+1}" for i in range(len(datos_campo["grupos_t"]))]
        sensores, matriz = datos_campo["sens_t"], datos_campo["Fr_t"]
    else:
        print("❌ Opción inválida.")
        return

    # Crear grafo
    dot = Digraph(comment="Gráfica de matriz", format="png")
    dot.attr(rankdir="LR")  # Layout de izquierda a derecha

    # Nodos de estaciones
    for est in estaciones:
        dot.node(est, est, shape="box", style="filled", color="lightblue")

    # Nodos de sensores
    for sens in sensores:
        dot.node(sens, sens, shape="ellipse", style="filled", color="lightgreen")

    # Aristas según matriz
    for i, est in enumerate(estaciones):
        for j, sens in enumerate(sensores):
            valor = matriz[i, j] if isinstance(matriz, np.ndarray) else matriz[i][j]
            if valor != 0:
                dot.edge(est, sens, label=str(valor))

    # Guardar y renderizar
    nombre_salida = input("Nombre del archivo de la gráfica (sin extensión): ").strip()
    if not nombre_salida:
        nombre_salida = "grafica"
    dot.render(nombre_salida, cleanup=True)
    print(f"✅ Gráfica generada: {nombre_salida}.png")

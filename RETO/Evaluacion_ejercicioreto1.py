# definimos fuera del ciclo
constantes = {
    "comb_min": 500,
    "t": 5,
    "tiempo_max": 60,
    "consumo": 50
}

historial = [] # definimos la lista vacia


while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ejecutar simulación de combustible y velocidad")
    print("2. Imprimir listas y diccionarios")
    print("3. Salir")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        historial = []

        constantes = {
            "comb_min": 500,
            "t": 5,
            "tiempo_max": 60,
            "consumo": 50
        }

        print("\nSimulación: Combustible y Velocidad\n")

        try:
            comb_inicial = float(input("Ingrese el combustible inicial: "))
            v_inicial = float(input("Ingrese la velocidad inicial: "))
            a = float(input("Ingrese la aceleración inicial: "))
            resistencia_aire = float(input("Ingrese la resistencia del aire: "))
        except ValueError:
            print("Entrada inválida: por favor ingrese valores numéricos.")
            continue
        except ValueError:
            print("Ingresa valores numéricos válidos.")
            continue
        comb_actual = comb_inicial
        velocidad = v_inicial
        tiempo = 0
        i = 0
        MAX_I = constantes["tiempo_max"] // constantes["t"]

        while i < MAX_I and comb_actual > 0:
            if comb_actual <= constantes["comb_min"]:
                v_objetivo = 400
                accion = "Desacelerar - ALERTA: Combustible bajo"
            else:
                v_objetivo = 500
                accion = "Acelerar"

            if velocidad >= v_objetivo:
                a = a - 5
            else:
                a = a + 5

            velocidad = velocidad + (a - resistencia_aire) * constantes["t"]
            tiempo = tiempo + constantes["t"]
            comb_actual = comb_actual - constantes["consumo"]
            i = i + 1
            registro = {
                "iteracion": i,
                "tiempo": tiempo,
                "velocidad": velocidad,
                "combustible": comb_actual,
                "accion": accion
            }
            historial.append(registro)

        print("\n--- HISTORIAL DE LA SIMULACIÓN ---")
        for registro in historial:
            print("Iteración:", registro["iteracion"])
            print("Tiempo:", registro["tiempo"], "segundos")
            print("Velocidad:", round(registro["velocidad"], 2), "m/s")
            print("Combustible:", round(registro["combustible"], 2))
            print("Acción:", registro["accion"])
            print("---------------------------")

        if historial:
            velocidades = [r["velocidad"] for r in historial]
            combustibles = [r["combustible"] for r in historial]

            vel_min = min(velocidades)
            vel_max = max(velocidades)
            vel_prom = sum(velocidades) / len(velocidades)
            comb_min = min(combustibles)
            comb_max = max(combustibles)
            comb_prom = sum(combustibles) / len(combustibles)

            print("\n=== ESTADÍSTICAS ===")
            print(f"Velocidad -> mín: {round(vel_min,2)} m/s | máx: {round(vel_max,2)} m/s | prom: {round(vel_prom,2)} m/s")
            print(f"Combustible -> mín: {round(comb_min,2)} | máx: {round(comb_max,2)} | prom: {round(comb_prom,2)}")
        else:
            print("\nNo hubo iteraciones (revisa valores iniciales).")

        print("\nCálculo finalizado")
        print("Total de iteraciones:", i)
        print("Tiempo total:", tiempo, "segundos")
        print("Estado final -> Velocidad:", round(velocidad, 2), "m/s | Combustible:", round(comb_actual, 2))

    elif opcion == "2":
        print("\n--- Contenido del diccionario 'constantes' ---")
        for clave, valor in constantes.items():
            print(f"{clave}: {valor}")

        if 'historial' in locals() and historial:
            print("\n--- Contenido de la lista 'historial' ---")
            for registro in historial:
                print(
                    f"Iteración {registro['iteracion']}: Tiempo = {registro['tiempo']}s, "
                    f"Velocidad = {round(registro['velocidad'], 2)} m/s, "
                    f"Combustible = {round(registro['combustible'], 2)}, "
                    f"Acción = {registro['accion']}"
                )
        else:
            print("\n La lista 'historial' está vacía. Ejecuta primero la simulación (opción 1).")

    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingresa 1, 2 o 3.")





while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("A. Combustible y Velocidad")
    print("B.  Altitud y Ángulo de ataque")
    print("C. ")
    print("D. Salir")

    opcion = input("Selecciona una opción: ").upper()

    match opcion:
        case "A":
            # Definición de la función simulacion() fuera de cualquier bloque
        
            historial = []

            constantes = {
                "comb_min": 500,
                "t": 5,
                "tiempo_max": 60,
                "consumo": 50
            }

            print("\nSimulación: Combustible y Velocidad\n")

            comb_inicial = float(input("Ingrese el combustible inicial: "))
            v_inicial = float(input("Ingrese la velocidad inicial: "))
            a = float(input("Ingrese la aceleración inicial: "))
            resistencia_aire = float(input("Ingrese la resistencia del aire: "))

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
                print("Velocidad:", registro["velocidad"], "m/s")
                print("Combustible:", registro["combustible"])
                print("Acción:", registro["accion"])
                print("---------------------------")

            print("\nCálculo finalizado")
            print("Total de iteraciones:", i)
            print("Tiempo total:", tiempo, "segundos")
            print("Estado final -> Velocidad:", velocidad, "m/s | Combustible:", comb_actual)


# test_rutina.py
# Rutina mágica de Cerón - test actualizado con nueva lógica de ejercicios, carga y descanso

from utils.ejercicio import generar_rutina_biseriada

# Selección de músculos simulada
musculos_seleccionados = ["Pecho", "Abdomen"]

rutina = generar_rutina_biseriada(musculos_seleccionados)

if not rutina:
    print("Error: Debes seleccionar exactamente 2 músculos.")
else:
    m1, m2 = musculos_seleccionados
    print("\n--- Rutina mágica de Cerón ---\n")

    for bloque in rutina:
        print(f"{bloque['Bloque']}:")
        
        # Ejercicio 1
        e1 = bloque[m1]
        print(f"{m1}: {e1['nombre']}, carga: {e1['carga']}")
        print(f"Recuperación: {e1['descanso']}")
        print("—" * 48)

        # Ejercicio 2
        e2 = bloque[m2]
        print(f"{m2}: {e2['nombre']}, carga: {e2['carga']}")
        print(f"Recuperación: {e2['descanso']}")
        print("—" * 48)

        print(f"→ Repetir secuencia {bloque['Repeticiones']} veces respetando recuperación.\n")
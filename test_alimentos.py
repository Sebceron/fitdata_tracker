# test_alimentos.py
# Prueba de la función buscar_alimento() desde utils/alimentos.py

from utils.alimentos import buscar_alimento

# Prueba con un alimento ejemplo
nombre = "arroz"
resultados = buscar_alimento(nombre)

# Mostrar resultados
for i, alimento in enumerate(resultados, 1):
    print(f"\nResultado {i}:")
    print(f"Nombre: {alimento['nombre']}")
    print(f"Calorías por 100g: {alimento['calorias']}")
    print(f"Proteínas: {alimento['proteinas']}g")
    print(f"Grasas: {alimento['grasas']}g")
    print(f"Carbohidratos: {alimento['carbohidratos']}g")
# utils/alimentos.py
# Módulo para buscar alimentos y sus calorías/macronutrientes usando la API de Open Food Facts

import requests

def buscar_alimento(nombre):
    """
    Busca un alimento en la API de Open Food Facts por nombre.
    Retorna una lista con los primeros resultados y su información nutricional.
    """
    url = "https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        "search_terms": nombre,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": 5
    }

    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    resultados = []

    for producto in datos.get("products", []):
        nombre = producto.get("product_name", "No disponible")
        nutriments = producto.get("nutriments", {})
        calorias = nutriments.get("energy-kcal_100g", "No disponible")
        proteinas = nutriments.get("proteins_100g", "No disponible")
        grasas = nutriments.get("fat_100g", "No disponible")
        carbohidratos = nutriments.get("carbohydrates_100g", "No disponible")

        resultados.append({
            "nombre": nombre,
            "calorias": calorias,
            "proteinas": proteinas,
            "grasas": grasas,
            "carbohidratos": carbohidratos
        })

    return resultados

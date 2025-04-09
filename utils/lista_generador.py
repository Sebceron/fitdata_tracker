# utils/lista_generador.py
import random
from utils.lista_mercado import MERCADO_FIT

def generar_lista_personalizada(objetivo):
    categorias = ["Proteínas", "Carbohidratos Complejos", "Grasas Saludables", "Vegetales y Fibra", "Snacks Saludables", "Frutas", "Extras Básicos"]
    lista_final = {}

    for cat in categorias:
        opciones = MERCADO_FIT.get(cat, [])
        if not opciones:
            continue

        cantidad = 5 if cat != "Frutas" else 3
        if objetivo == "Definición":
            if cat == "Carbohidratos Complejos":
                cantidad = 3
        elif objetivo == "Volumen":
            if cat == "Carbohidratos Complejos":
                cantidad = 7
            if cat == "Snacks Saludables":
                cantidad = 6

        lista_final[cat] = random.sample(opciones, min(len(opciones), cantidad))

    return lista_final

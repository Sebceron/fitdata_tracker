# utils/imc.py
# Funciones para calcular y clasificar el IMC

# --------------------------------
# Función que calcula el IMC
# --------------------------------
def calcular_imc(peso_kg, altura_cm):
    """
    Cálculo del Índice de Masa Corporal (IMC)
    Fórmula: IMC = peso (kg) / altura (m)^2
    """
    altura_m = altura_cm / 100
    imc = peso_kg / (altura_m ** 2)
    return imc

# --------------------------------
# Función que clasifica el IMC
# --------------------------------
def clasificar_imc(imc):
    """
    Clasificación del IMC según la OMS.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"



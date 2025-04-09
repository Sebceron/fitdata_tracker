# utils/calorias.py
# ---------------------------------------------
# Funciones para calcular TMB y calorías objetivo
# ---------------------------------------------

def calcular_tmb(sexo, peso, altura, edad):
    """
    Cálculo de la Tasa Metabólica Basal (TMB) usando la fórmula de Mifflin-St Jeor:
    TMB (hombres)   = 10 * peso + 6.25 * altura - 5 * edad + 5
    TMB (mujeres)   = 10 * peso + 6.25 * altura - 5 * edad - 161

    Parámetros:
    - sexo: 'Masculino' o 'Femenino'
    - peso: en kilogramos (float)
    - altura: en centímetros (int)
    - edad: en años (int)

    Retorna:
    - TMB como float
    """
    if sexo == "Masculino":
        return 10 * peso + 6.25 * altura - 5 * edad + 5
    else:
        return 10 * peso + 6.25 * altura - 5 * edad - 161


def calcular_calorias_objetivo(tmb, nivel_actividad, objetivo):
    """
    Ajuste de calorías totales según nivel de actividad y objetivo físico.

    Parámetros:
    - tmb: Tasa metabólica basal (float)
    - nivel_actividad: string con opción seleccionada
    - objetivo: 'Perder peso', 'Ganar peso', 'Mantener peso'

    Retorna:
    - Calorías diarias estimadas como float
    """
    # Multiplicadores estándar según actividad física
    niveles = {
        "Sedentario (poco o nada de ejercicio)": 1.2,
        "Ligero (1-3 días/semana)": 1.375,
        "Moderado (3-5 días/semana)": 1.55,
        "Activo (6-7 días/semana)": 1.725,
        "Muy activo (2 veces por día o trabajo físico)": 1.9
    }

    calorias_mantenimiento = tmb * niveles[nivel_actividad]

    if objetivo == "Perder peso":
        return calorias_mantenimiento - 500  # déficit sugerido
    elif objetivo == "Ganar peso":
        return calorias_mantenimiento + 500  # superávit sugerido
    else:
        return calorias_mantenimiento
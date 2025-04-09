# utils/suplementos.py
def recomendar_suplementos(objetivo):
    suplementos = {
        "Ganar masa muscular": [
            "Proteína whey",
            "Creatina monohidratada",
            "Gainers (hipercalóricos)",
            "BCAA (aminoácidos ramificados)",
            "Beta-alanina"
        ],
        "Perder grasa corporal": [
            "L-carnitina",
            "Proteína isolatada",
            "Cafeína",
            "Extracto de té verde",
            "CLA (ácido linoleico conjugado)"
        ],
        "Mejorar rendimiento y energía": [
            "Pre-entrenos con cafeína",
            "Beta-alanina",
            "Citrulina malato",
            "Creatina",
            "Electrolitos"
        ],
        "Recuperación muscular": [
            "Glutamina",
            "Caseína",
            "Magnesio",
            "Omega-3",
            "ZMA"
        ]
    }
    return suplementos.get(objetivo, ["No hay recomendaciones para este objetivo."])

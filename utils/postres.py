# utils/postres.py
import random

# Lista general con todos los postres
POSTRES_TODOS = [
    "Yogur griego natural con nueces y canela",
    "Manzana con mantequilla de maní sin azúcar",
    "Chía pudding con leche vegetal sin azúcar y frambuesas",
    "Gelatina sin azúcar con fresas",
    "Helado casero de plátano congelado y cacao amargo",
    "Mousse de aguacate y cacao endulzado con stevia",
    "Fresas con crema de coco sin azúcar",
    "Tortitas de avena y claras con canela",
    "Rodajas de pepino con limón y tajín",
    "Smoothie verde con espinaca, pepino y jengibre",
    "Tarta de queso saludable sin base y sin azúcar",
    "Durazno al horno con esencia de vainilla y canela",
    "Bolas energéticas de avena, coco y almendras sin azúcar",
    "Pudín de semillas de lino y leche de almendra",
    "Mini muffins de calabacín con harina de avena",
    "Rodajas de kiwi con coco rallado",
    "Compota casera de manzana sin azúcar",
    "Tostadas de arroz integral con ricotta y canela",
    "Bol de granola casera sin azúcar con yogur natural",
    "Crema fría de cacao, aguacate y vainilla sin azúcar",
    "Fresas al horno con ralladura de naranja",
    "Melón con gotas de limón y hojas de menta",
    "Chips de manzana al horno con canela",
    "Copo de avena con bebida vegetal y arándanos",
    "Batido frío de café con leche vegetal sin azúcar",
    "Brochetas de fruta fresca y semillas",
    "Mini panquecas de avena y proteína sin azúcar",
    "Rodajas de zanahoria con hummus especiado",
    "Mousse de tofu con cacao y esencia de vainilla",
    "Pudín de agar-agar con leche de coco y almendra",
    "Tostadas integrales con requesón, canela y stevia",
    "Helado de yogur natural con trozos de kiwi y coco rallado",
    "Manzana al horno con nueces y canela",
    "Galletas caseras de avena, plátano y canela sin azúcar",
    "Brownies de garbanzos y cacao sin harinas refinadas",
    "Smoothie bowl de frutas rojas con semillas de chía",
    "Mousse de proteína con gelatina sin azúcar",
    "Tarta de manzana fit sin masa, solo con huevo, avena y canela",
    "Yogur de coco con almendras fileteadas y frambuesas",
    "Chips de pera horneados con canela",
    "Nieve de mango natural congelado",
    "Barritas caseras de avena, dátiles y proteína",
    "Trufas energéticas con cacao, avena y almendras molidas",
    "Muffins de avena y zanahoria sin azúcar",
    "Flan de coco y claras con esencia de vainilla",
    "Pudín de proteína con leche vegetal y semillas de chía",
    "Chocolate amargo 85% con mantequilla de almendra",
    "Yogur griego con frambuesas y cacao en polvo",
    "Smoothie de calabaza, proteína y canela",
    "Paletas heladas de leche vegetal, fresas y stevia",
    "Bizcocho esponjoso de banana, avena y claras",
    "Compota de pera y canela sin azúcar",
    "Parfait de yogur con avena activada y fruta",
    "Bocaditos de zanahoria y coco rallado",
    "Maní tostado con cacao amargo en polvo",
    "Taza de leche dorada fría con cúrcuma y canela",
    "Crema fría de ricotta con gotas de esencia de almendra",
    "Turrón fit de almendras, clara y stevia",
    "Crumble saludable de avena y frutos rojos",
    "Smoothie de proteína de vainilla con chía y mango",
    "Crema de calabaza con canela y esencia de vainilla",
    "Helado de frutos rojos sin azúcar con base de yogur",
    "Mini cheesecake de ricotta con base de avena",
    "Dátiles rellenos de nuez bañados en cacao amargo",
    "Mermelada casera de frutos rojos sin azúcar",
    "Rollitos de canela fit con harina de avena",
    "Granizado de limón natural con hojas de menta",
    "Peras cocidas al vino tinto sin azúcar",
    "Pan de plátano y avena con nueces",
    "Tarta crujiente de avena con manzana y canela",
    "Smoothie de espinaca, piña y proteína de vainilla",
    "Mousse de remolacha y cacao con stevia",
    "Pops de yogurt griego congelado con frutas picadas",
    "Compota tibia de ciruela y manzana sin azúcar",
    "Trufas de coco rallado, chía y esencia de vainilla",
    "Manzanas caramelizadas al horno con stevia",
    "Crepes de avena y claras rellenos de frutos rojos",
    "Galletas de almendra y canela sin harina",
    "Torta de zanahoria fit con cobertura de queso light",
    "Tarta helada de plátano y mantequilla de almendra",
    "Flan de huevo light con leche vegetal y stevia",
    "Cuadrados de avena, zanahoria y coco sin azúcar",
    "Batido de chocolate oscuro y proteína vegetal",
    "Pudín de arroz integral con bebida vegetal y canela",
    "Trufas veganas de cacao y almendras sin azúcar",
    "Bizcochitos de naranja y avena sin harina refinada",
    "Smoothie bowl de papaya, mango y coco",
    "Copa de frutos secos con yogur y esencia de ron",
    "Rebanadas de batata horneadas con canela",
    "Tartaletas de avena y frutas frescas sin azúcar"
]

POSTRES_CATEGORIZADOS = {
    "Pre-entreno dulce": [
        "Galletas de avena, banana y proteína vegetal",
        "Smoothie de plátano con proteína y mantequilla de maní",
        "Barritas energéticas de dátiles, avena y almendras",
        "Tostadas integrales con requesón y miel natural",
        "Bizcocho de avena con proteína de vainilla",
        "Batido de avena, manzana y canela",
        "Pan de plátano sin azúcar con nueces",
        "Bol de yogur griego con granola casera",
        "Mini panquecas de avena con proteína",
        "Batido de leche vegetal, avena y canela",
        "Bowl de banana, crema de cacahuate y chía",
        "Torta de zanahoria fit con avena y stevia"
    ],

    "Para antojo nocturno": [
        "Yogur griego natural con nueces y canela",
        "Manzana al horno con canela y almendras",
        "Compota tibia de ciruela y manzana sin azúcar",
        "Pops de yogur congelado con frutas",
        "Rodajas de kiwi con coco rallado",
        "Taza de leche dorada con cúrcuma y vainilla",
        "Tostadas de arroz con ricotta y stevia",
        "Chips de manzana al horno con canela",
        "Crema tibia de avena y cacao sin azúcar",
        "Mousse de tofu con cacao y vainilla",
        "Bocaditos de zanahoria con mantequilla de almendra",
        "Gelatina sin azúcar con fresas"
    ],

    "Apto para diabéticos": [
        "Chía pudding con leche de almendra sin azúcar",
        "Mini muffins de calabacín con harina de avena",
        "Gelatina sin azúcar con frutos rojos",
        "Smoothie de pepino, espinaca y limón",
        "Tartaleta sin base de yogur y frambuesas",
        "Turrón fit de almendras y clara de huevo",
        "Mousse de aguacate con cacao y stevia",
        "Rebanadas de batata con canela",
        "Yogur sin azúcar con topping de nueces",
        "Compota casera de manzana con esencia de vainilla",
        "Crema fría de ricotta y gotas de almendra"
    ],

    "Bajo en carbohidrato": [
        "Rodajas de zanahoria con hummus especiado",
        "Fresas con crema de coco sin azúcar",
        "Trufas de coco, almendra y cacao amargo",
        "Mousse de tofu con cacao y esencia de vainilla",
        "Rollitos de pepino con crema de aguacate",
        "Batido de proteína y mantequilla de almendra",
        "Yogur griego con canela y semillas de chía",
        "Bol de nueces con cacao y coco rallado",
        "Gelatina con colágeno y limón",
        "Huevos rellenos dulces con canela y vainilla (sí, estilo keto!)",
        "Mousse de queso cottage con frambuesas",
        "Smoothie de proteína con espinaca y mantequilla de maní"
    ]
}


# Esta función FALTABA antes
def obtener_postre_random():
    return random.choice(POSTRES_TODOS)

def obtener_postre_total_random():
    return random.choice(POSTRES_TODOS)

def obtener_postre_por_categoria(categoria):
    if categoria in POSTRES_CATEGORIZADOS:
        return random.choice(POSTRES_CATEGORIZADOS[categoria])
    return "No hay postres disponibles para esta categoría."
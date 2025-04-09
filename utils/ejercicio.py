# utils/ejercicios.py
import random

PORCENTAJES_CARGA = ["30%", "40%", "50%", "60%", "70%", "80%", "90%"]
TIEMPOS_DESCANSO = ["45 segundos", "60 segundos", "75 segundos", "90 segundos"]

EJERCICIOS = {
    "Pecho": [
        "Press plano con barra", "Press inclinado con mancuernas", "Aperturas en máquina",
        "Fondos abiertos", "Crossover en polea", "Press declinado", "Vuelos con mancuerna",
        "Press en Smith", "Press inclinado con barra", "Press plano con mancuernas",
        "Push-ups", "Press con agarre cerrado", "Press Hammer en máquina",
        "Flexiones con palmada", "Press declinado en máquina", "Press con bandas",
        "Fondos entre bancos", "Aperturas inclinadas", "Press con resistencia variable",
        "Press en máquina convergente"
    ],
    "Bíceps": [
        "Curl alterno mancuernas", "Curl martillo", "Curl en banco inclinado",
        "Curl concentración", "Curl polea baja", "Curl barra recta",
        "Curl barra Z parado", "Curl predicador", "Curl araña",
        "Curl con cuerda en polea", "Curl con banda elástica", "Curl tipo 21",
        "Curl en banco Scott", "Curl isométrico contra pared", "Curl Z sentado",
        "Curl martillo inclinado", "Curl cruzado con mancuerna",
        "Curl con cuerda alternado", "Curl con giro supino", "Curl en polea alta"
    ],
    "Tríceps": [
        "Press francés", "Fondos en banco", "Extensión polea alta", "Copa a una mano",
        "Extensión barra Z", "Patada de tríceps", "Extensión con cuerda",
        "Press cerrado con barra", "Press con mancuerna sobre cabeza",
        "Fondos paralelas", "Extensión inclinada con mancuerna",
        "Extensión en banco plano", "Extensión en polea baja",
        "Rompecráneos con barra", "Patada con cuerda en polea",
        "Extensión con barra recta de pie", "Press con mancuernas juntos",
        "Pushdown agarre invertido", "Kickback con banda", "Extensión cruzada"
    ],
    "Espalda": [
        "Jalón al pecho", "Remo con barra", "Peso muerto", "Dominadas",
        "Remo en máquina", "Pull-over", "Remo con mancuerna", "Dominadas con lastre",
        "Remo polea baja", "Jalón tras nuca", "Peso muerto rumano",
        "Remo T-bar", "Remo con cuerda baja", "Jalón con agarre estrecho",
        "Jalón con agarre neutro", "Remo invertido TRX", "Pull-over con mancuerna",
        "Peso muerto con déficit", "Remo en polea unilateral", "Remo en banco plano"
    ],
    "Piernas": [
        "Sentadilla libre", "Prensa 45°", "Extensiones de piernas",
        "Curl femoral", "Zancadas con barra", "Zancadas con mancuerna",
        "Peso muerto rumano", "Elevación de talones", "Hip thrust",
        "Sentadilla goblet", "Step-up en banco", "Sentadilla frontal",
        "Peso muerto sumo", "Desplantes laterales", "Curl femoral de pie",
        "Sentadilla búlgara", "Zancadas en máquina Smith", "Peso muerto unilateral",
        "Adducción en máquina", "Extensión con banda"
    ],
    "Hombros": [
        "Press militar", "Elevaciones laterales", "Pájaros deltoide posterior",
        "Press Arnold", "Elevación frontal", "Encogimientos de hombros",
        "Press en máquina", "Face pull", "Elevación lateral inclinada",
        "Press con mancuernas sentado", "Elevaciones con banda",
        "Remo al cuello con barra Z", "Elevación lateral unilatera",
        "Encogimientos con barra detrás", "Elevación 90° con mancuernas",
        "Press de hombros con kettlebell", "Press Landmine a un brazo",
        "Press con barra detrás del cuello", "Remo alto con cuerda",
        "Isométrico lateral con disco"
    ],
    "Abdomen": [
        "Crunch abdominal en suelo", "Elevaciones de piernas en barra",
        "Plancha isométrica", "Encogimientos en máquina",
        "Crunch con cuerda en polea", "Toques de talón", "Crunch bicicleta",
        "Elevaciones piernas tumbado", "Ab rollouts", "Plancha con elevación de pierna",
        "Crunch en banco declinado", "Escaladores", "Plancha lateral",
        "Elevaciones de piernas colgado", "Giros rusos con balón",
        "Plancha dinámica", "Elevaciones de cadera en suelo",
        "Plancha con toque de hombros", "Crunch con disco", "V-ups"
    ],
    "Glúteos": [
        "Hip thrust con barra", "Patada de glúteo en polea",
        "Peso muerto rumano unilateral", "Sentadillas sumo",
        "Abducción en máquina", "Puente de glúteos",
        "Zancadas caminando", "Sentadilla goblet profunda",
        "Elevaciones de cadera con mancuerna", "Patada con banda",
        "Sentadilla con pausa", "Step-up con mancuerna",
        "Patada de glúteo en máquina", "Glute bridge con barra",
        "Zancadas laterales", "Step-down unilateral",
        "Puente a una pierna", "Bandas laterales walk",
        "Sentadilla isométrica en pared", "Frog pumps"
    ]
}

def generar_rutina_biseriada(musculos):
    if len(musculos) != 2:
        return []

    m1, m2 = musculos
    ejercicios_m1 = random.sample(EJERCICIOS[m1], 4)
    ejercicios_m2 = random.sample(EJERCICIOS[m2], 4)

    rutina = []
    for i in range(4):
        ejercicio1 = {
            "nombre": ejercicios_m1[i],
            "carga": random.choice(PORCENTAJES_CARGA),
            "descanso": random.choice(TIEMPOS_DESCANSO)
        }
        ejercicio2 = {
            "nombre": ejercicios_m2[i],
            "carga": random.choice(PORCENTAJES_CARGA),
            "descanso": random.choice(TIEMPOS_DESCANSO)
        }
        rutina.append({
            "Bloque": f"Bloque {chr(65+i)}",
            m1: ejercicio1,
            m2: ejercicio2,
            "Repeticiones": 3 + (i % 2)
        })

    return rutina

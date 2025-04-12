# ============================
#        CONFIGURACIÓN
# ============================

import streamlit as st

# Este debe ser el primer comando de Streamlit
st.set_page_config(page_title="Método Cerón", layout="centered")

# ============================
#       IMPORTACIONES
# ============================

# Librerías estándar
import os
import sys
import random
import requests
import pandas as pd

# Librerías externas
from streamlit_lottie import st_lottie
from streamlit_carousel import carousel
import streamlit.components.v1 as components

# Estilos globales Apple/Samsung
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Ruta absoluta para importar desde cualquier tab
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# ============================
#     FUNCIONES PERSONALIZADAS
# ============================

from utils.imc import calcular_imc, clasificar_imc
from utils.calorias import calcular_tmb, calcular_calorias_objetivo
from utils.alimentos import buscar_alimento
from utils.ejercicio import generar_rutina_biseriada
from utils.timer import iniciar_timer_minutos, iniciar_timer_segundos, reproducir_alarma
from utils.postres import (
    obtener_postre_random, obtener_postre_total_random,
    obtener_postre_por_categoria, POSTRES_CATEGORIZADOS
)
from utils.suplementos import recomendar_suplementos
from utils.lista_mercado import obtener_lista_mercado_fit, generar_lista_personalizada
from utils.noticias import obtener_estudios_nutricion

# ============================
#     FUNCIONES AUXILIARES
# ============================

@st.cache_data(ttl=3600)
def obtener_estudios_cached():
    return obtener_estudios_nutricion()

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title("🏋️‍♂️ Método Cerón")



frases_motivacionales = [
    "“Cada célula de tu cuerpo está escuchando lo que comes.”",
    "“Lo que no se mide, no mejora.”",
    "“La disciplina es el puente entre tus metas y tus resultados.”",
    "“Come para nutrir tu cuerpo, no solo para llenarlo.”",
    "“Tu cuerpo puede soportar casi cualquier cosa. Es tu mente la que debes convencer.”",
    "“Entrena como si tu vida dependiera de ello… porque lo hace.”",
    "“No estás comiendo menos, estás comiendo con propósito.”",
    "“El sudor es solo la grasa llorando por salir.”",
    "“Lo que haces hoy define tu salud de mañana.”",
    "“Si no haces tiempo para cuidarte, tendrás que hacer tiempo para enfermarte.”",
    "“El dolor de la disciplina pesa gramos, el del arrepentimiento toneladas.”",
    "“No se trata de ser el mejor, sino de ser mejor que ayer.”",
    "“La comida puede ser tu medicina o tu veneno.”",
    "“Un cuerpo saludable es un templo, no un basurero.”",
    "“No estás a dieta, estás diseñando tu nueva vida.”",
    "“Tu progreso vive donde termina tu zona de confort.”",
    "“Tu cuerpo escucha todo lo que tu mente dice.”",
    "“No renuncies por una recaída. Aprende y sigue.”",
    "“La constancia vence al talento cuando el talento no es constante.”",
    "“La verdadera transformación comienza en la mente.”",
    "“El músculo más importante a entrenar es tu voluntad.”",
    "“Cuidarte no es egoísmo, es supervivencia.”",
    "“El hambre emocional no se llena con comida.”",
    "“Descansar también es parte del progreso.”",
    "“Tu cuerpo no te está castigando, está hablándote.”",
    "“La salud no es un objetivo, es un estilo de vida.”",
    "“Cada decisión cuenta, incluso cuando nadie te ve.”",
    "“Comer bien es un acto de amor propio.”",
    "“Hazlo por ti, por tu futuro, por tu paz.”",
    "“La energía que das, es la energía que regresa.”",
    "“Mueve tu cuerpo, mueve tu vida.”",
    "“Ningún alimento vale más que tu bienestar.”",
    "“Si lo vas a hacer, hazlo bien.”",
    "“No te castigues por caer, celébrate por levantarte.”",
    "“Los hábitos son la arquitectura de tus resultados.”",
    "“No necesitas motivación, necesitas compromiso.”",
    "“La comida no es la enemiga, es información para tus células.”",
    "“No estás empezando de cero, estás empezando con experiencia.”",
    "“Hoy puede ser el primer día de tu nueva vida.”",
    "“La fuerza física comienza con la mental.”",
    "“No existe progreso sin incomodidad.”",
    "“Tu cuerpo grita lo que tu mente calla.”",
    "“El cambio no se siente cómodo, pero sí valioso.”",
    "“Recuerda por qué empezaste.”",
    "“No es magia, es ciencia, esfuerzo y consistencia.”",
    "“El verdadero lujo es estar saludable.”",
    "“El descanso no es debilidad, es estrategia.”",
    "“Cuidar tu cuerpo es respetar tu existencia.”",
    "“Lo fácil viene con costo; lo difícil, con resultados.”",
    "“Tu cuerpo refleja cómo te tratas.”",
    "“La comida es el combustible, no la recompensa.”",
    "“Cada comida es una oportunidad de sanarte.”",
    "“Invertir en salud es la mejor rentabilidad.”",
    "“Lo que repites, te forma.”",
    "“Los cambios grandes nacen de decisiones pequeñas repetidas.”",
    "“Tu cuerpo, tu responsabilidad, tu revolución.”",
    "“La transformación no es visible al principio, pero se siente.”",
    "“Hazlo con miedo, con flojera, pero hazlo.”",
    "“Cambia la excusa por una intención.”",
    "“Cada repetición es un voto por la persona que quieres ser.”",
    "“Lo más difícil no es empezar, es no rendirse.”",
    "“Entrenar también es sanar.”",
    "“Cuida tu energía, es lo más valioso que tienes.”",
    "“Tu salud es el verdadero capital.”",
    "“Haz ejercicio como si tu mente dependiera de ello… porque lo hace.”",
    "“No necesitas hacerlo perfecto, solo necesitas hacerlo.”",
    "“Cada gota de sudor riega tu mejor versión.”",
    "“Tú eres tu mayor proyecto.”",
    "“Ser saludable no es un objetivo, es un lenguaje diario.”",
    "“El esfuerzo siempre deja huella, aunque aún no la veas.”",
    "“Cuida tu cuerpo. Es el único lugar donde vas a vivir.”"
]

frase_seleccionada = random.choice(frases_motivacionales)

# Reemplaza la definición de tabs por esta nueva:
tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "✨ Inicio", "🧍 IMC", "🔥 Calorías Objetivo", "🥦 Alimentos",
    "🏋️ Rutina Cerón", "🍩 Postre Fit", "⏰ Timer",
    "🍽️ Postres filtrados", "💊 Suplementos", "🛒 Mercado Fit", "📰 Estudios Científicos"
])


# -------------------------------
# TAB 0 - Inicio con Frase Motivacional
# -------------------------------


with tab0:
    # BLOQUE 1: Hero visual estilo Apple
    st.markdown("""
        <div class="hero-section">
            <h1 class="animate-in text-center">Bienvenido al ecosistema fitness inteligente</h1>
            <p class="hero-sub animate-slide text-center">
                Transforma tu cuerpo con ciencia, nutrición y resultados.
            </p>
        </div>
    """, unsafe_allow_html=True)





# BLOQUE 2: Frase motivacional del día - estilo minimalista Apple
st.markdown(f"""
    <style>
        .frase-apple {{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1.2rem 0;
            animation: fadeIn 1s ease-out both;
        }}

        .frase-contenido {{
            backdrop-filter: blur(10px);
            background: rgba(0, 0, 0, 0.3);  /* Fondo más oscuro para resaltar letra blanca */
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 16px;
            padding: 1rem 1.5rem;
            max-width: 720px;
            color: #ffffff;
            font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 1.2rem;
            font-weight: 500;
            text-align: center;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
            line-height: 1.6;
        }}

        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(10px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
    </style>

    <div class="frase-apple">
        <div class="frase-contenido">
            “{frase_seleccionada}”
        </div>
    </div>
""", unsafe_allow_html=True)






    # BLOQUE 2: Carrusel visual estilo Apple
st.markdown("""
<div class="apple-carousel">
    <div class="carousel-item">
        <img src="https://images.unsplash.com/photo-1605296867304-46d5465a13f1?auto=format&fit=crop&w=1500&q=80" class="carousel-image" />
        <div class="carousel-caption">
            <h3>Activa tu potencial</h3>
            <p>Transforma tu cuerpo desde casa con rutinas personalizadas.</p>
        </div>
    </div>

    <div class="carousel-item">
        <img src="https://images.unsplash.com/photo-1605296866942-59a1b8f5f6f3?auto=format&fit=crop&w=1500&q=80" class="carousel-image" />
        <div class="carousel-caption">
            <h3>Nutrición que potencia</h3>
            <p>Come de forma inteligente, vive con energía real.</p>
        </div>
    </div>

    <div class="carousel-item">
        <img src="https://images.unsplash.com/photo-1581009146145-4f12acf24cba?auto=format&fit=crop&w=1500&q=80" class="carousel-image" />
        <div class="carousel-caption">
            <h3>Resultados sostenibles</h3>
            <p>Sin magia. Solo ciencia, hábitos y consistencia.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)




# -------------------------------
# TAB 1 - IMC
# -------------------------------
with tab1:
    st.subheader("💪 Calculadora de IMC")
    peso = st.number_input("Ingresa tu peso (kg):", min_value=30.0, max_value=200.0, step=0.5, key="peso_imc")
    altura = st.number_input("Ingresa tu altura (cm):", min_value=130, max_value=220, step=1, key="altura_imc")

    if st.button("Calcular IMC"):
        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc)
        st.success(f"Tu IMC es: {imc:.2f}")
        st.info(f"Clasificación: {clasificacion}")

# -------------------------------
# TAB 2 - Calorías Objetivo
# -------------------------------
with tab2:
    st.subheader("🔥 Calculadora de Calorías Objetivo")
    sexo = st.radio("Sexo:", ["Masculino", "Femenino"], horizontal=True)
    edad = st.number_input("Edad:", min_value=10, max_value=90, step=1)
    peso_cal = st.number_input("Peso (kg):", min_value=30.0, max_value=200.0, step=0.5, key="peso_cal")
    altura_cal = st.number_input("Altura (cm):", min_value=130, max_value=220, step=1, key="altura_cal")

    nivel_actividad = st.selectbox("Nivel de actividad física:", [
        "Sedentario (poco o nada de ejercicio)",
        "Ligero (1-3 días/semana)",
        "Moderado (3-5 días/semana)",
        "Activo (6-7 días/semana)",
        "Muy activo (2 veces por día o trabajo físico)"
    ])

    objetivo = st.selectbox("Objetivo físico:", ["Mantener peso", "Perder peso", "Ganar peso"])

    if st.button("Calcular calorías objetivo"):
        tmb = calcular_tmb(sexo, peso_cal, altura_cal, edad)
        calorias_dia = calcular_calorias_objetivo(tmb, nivel_actividad, objetivo)
        st.success(f"Tu requerimiento diario estimado es: {int(calorias_dia)} kcal")
        st.caption("Este número es aproximado, y puede variar según tu cuerpo y estilo de vida.")

# -------------------------------
# TAB 3 - Alimentos
# -------------------------------
with tab3:
    st.subheader("🥦 Buscador de Alimentos y Calorías de Cerón")
    nombre_alimento = st.text_input("Escribe el nombre de un alimento para buscar:", placeholder="Ej: arroz, manzana, pollo")

    if st.button("Buscar información nutricional"):
        if nombre_alimento.strip() == "":
            st.warning("Por favor, ingresa el nombre de un alimento.")
        else:
            resultados = buscar_alimento(nombre_alimento)
            if resultados:
                st.success(f"Se encontraron {len(resultados)} alimentos:")
                for i, alimento in enumerate(resultados, 1):
                    st.markdown(f"**{i}. {alimento['nombre']}**")
                    st.markdown(f"- Calorías por 100g: `{alimento['calorias']}` kcal")
                    st.markdown(f"- Proteínas: `{alimento['proteinas']}` g")
                    st.markdown(f"- Grasas: `{alimento['grasas']}` g")
                    st.markdown(f"- Carbohidratos: `{alimento['carbohidratos']}` g")
                    st.markdown("---")
            else:
                st.warning("No se encontraron resultados. Prueba con otro término.")

# -------------------------------
# TAB 4 - Rutina Aleatoria Cerón
# -------------------------------
with tab4:
    st.subheader("🏋️ Rutina mágica de Cerón")
    st.markdown("Selecciona 2 grupos musculares para generar una rutina biseriada personalizada.")

    opciones = list(sorted(set(generar_rutina_biseriada.__globals__["EJERCICIOS"].keys())))
    seleccionados = st.multiselect("Selecciona exactamente 2 músculos:", opciones, max_selections=2)
    

    if len(seleccionados) == 2:
        if st.button("✨ Generar rutina mágica de Cerón"):
            rutina = generar_rutina_biseriada(seleccionados)
            m1, m2 = seleccionados

            for bloque in rutina:
                st.markdown(f"### {bloque['Bloque']}")
                e1 = bloque[m1]
                e2 = bloque[m2]

                st.markdown(f"**{m1}**: {e1['nombre']}, **Carga**: {e1['carga']}, **Recuperación**: {e1['descanso']}")
                st.markdown(f"**{m2}**: {e2['nombre']}, **Carga**: {e2['carga']}, **Recuperación**: {e2['descanso']}")
                st.markdown(f"→ Repetir secuencia **{bloque['Repeticiones']} veces** respetando recuperación.")
                st.markdown("---")
    elif len(seleccionados) > 2:
        st.warning("Solo puedes seleccionar 2 músculos.")




# -------------------------------
# TAB 5 - Postres recomendados por Cerón
# -------------------------------
with tab5:
    st.subheader("🍩 Postres saludables por Cerón")
    st.markdown(
        "¿Tienes ansiedad o antojo? Haz clic en el botón y recibe una sugerencia dulce, "
        "baja en calorías, apta para fitness y diabéticos. ¡Aprobada por el sensei Cerón!"
    )

    if st.button("🎲 Recomiéndame un postre"):
        postre = obtener_postre_random()
        st.success(f"**Recomendación:** {postre}")



# -------------------------------
# TAB 6 - Temporizador de Entrenamiento
# -------------------------------
with tab6:
    st.subheader("⏱️ Temporizador de Entrenamiento")

    st.markdown("### **Temporizador por Minutos**")
    minutos = st.slider("Selecciona los minutos:", 1, 60, 5)
    if st.button("Iniciar temporizador de minutos"):
        iniciar_timer_minutos(minutos)
        reproducir_alarma()

    st.markdown("---")  # Separador visual

    st.markdown("### **Temporizador por Segundos**")
    segundos = st.slider("Selecciona los segundos:", 10, 90, 60, step=10)
    if st.button("Iniciar temporizador de segundos"):
        iniciar_timer_segundos(segundos)
        reproducir_alarma()




# -------------------------------
# TAB 7 - Postres filtrados
# -------------------------------
with tab7:
    st.subheader("🍽️ Filtra tu postre saludable")

    tipo = st.radio("¿Cómo deseas filtrar?", ["🎲 Aleatorio total", "🎯 Por categoría"])

    if tipo == "🎲 Aleatorio total":
        if st.button("Mostrar cualquier postre saludable"):
            postre = obtener_postre_total_random()
            st.success(f"**Postre recomendado:** {postre}")
    else:
        categoria = st.selectbox("Selecciona una categoría:", list(POSTRES_CATEGORIZADOS.keys()))
        if st.button("Mostrar postre por categoría"):
            postre = obtener_postre_por_categoria(categoria)
            st.success(f"**Postre recomendado:** {postre}")


# -------------------------------
# TAB 8 - Suplementos deportivos por objetivo
# -------------------------------
with tab8:
    st.subheader("💊 Recomendador de Suplementos Deportivos")
    st.markdown(
        "Selecciona tu objetivo principal de entrenamiento y obtendrás una lista de suplementos comunes "
        "utilizados por deportistas y culturistas según esa meta."
    )

    # Menú desplegable con los objetivos
    objetivo = st.selectbox("Selecciona tu objetivo principal:", [
        "Ganar masa muscular",
        "Perder grasa corporal",
        "Mejorar rendimiento y energía",
        "Recuperación muscular"
    ])

    # Botón para generar las recomendaciones
    if st.button("🔍 Recomendar suplementos"):
        recomendaciones = recomendar_suplementos(objetivo)

        # Mostrar cada suplemento recomendado
        st.success("Recomendaciones del coach Cerón:")
        for suplemento in recomendaciones:
            st.markdown(f"- **{suplemento}**")



# -------------------------------
# TAB 9 - Listas de Mercado inteligente
# -------------------------------
with tab9:
    st.subheader("🛒 Lista de Mercado Fitness Personalizada")
    st.markdown("Selecciona tu objetivo y genera una lista aleatoria de alimentos saludables basada en tu estilo fitness.")

    objetivo_usuario = st.selectbox("Selecciona tu objetivo de entrenamiento:", ["Mantenimiento", "Volumen", "Definición"])
    restricciones = st.multiselect("¿Tienes alguna restricción dietaria?", [
    "Sin gluten", "Sin lactosa", "Vegano", "Keto", "Diabético", "Sin frutos secos"
])


    if st.button("🎯 Generar lista de mercado"):
        # Generar lista
        lista = generar_lista_personalizada(objetivo_usuario)
        st.success("Lista generada con éxito.")

        # Mostrar en secciones por categoría
        for categoria, items in lista.items():
            st.markdown(f"### {categoria}")
            for item in items:
                st.markdown(f"- {item}")
            st.markdown("---")

        # Convertir a DataFrame
        import pandas as pd
        df_lista = pd.DataFrame([
            (categoria, alimento)
            for categoria, alimentos in lista.items()
            for alimento in alimentos
        ], columns=["Categoría", "Alimento"])

        # Botón de descarga con estilo
        st.download_button(
            label="📥 Descargar lista de mercado (Excel)",
            data=df_lista.to_csv(index=False).encode("utf-8"),
            file_name="lista_mercado_fit.csv",
            mime="text/csv",
        )

        



# -------------------------------
# TAB 10 - Estudios Científicos de Nutrición
# -------------------------------

with tab10:
    st.subheader("🧠 Estudios Científicos de Nutrición y Fitness")
    st.caption("Fuente: Europe PMC")

    estudios = obtener_estudios_nutricion()

    if estudios:
        st.markdown("#### **Conocimiento aplicado es poder.**")
        st.caption("Descubre cómo la ciencia respalda tu nutrición y entrenamiento.")

        # Función para extraer etiquetas desde resumen o título
        def extraer_etiquetas(texto):
            temas = {
                "proteína": ["proteína", "protein", "whey"],
                "entrenamiento": ["entrenamiento", "training", "exercise", "físico"],
                "dieta": ["dieta", "diet", "keto", "mediterránea"],
                "suplementos": ["supplement", "creatina", "creatine", "bcaa"],
                "ayuno": ["ayuno", "fasting", "intermittent"],
                "peso corporal": ["weight loss", "obesity", "adelgazar", "pérdida"],
                "cardiovascular": ["cardio", "heart", "corazón"],
                "diabetes": ["diabetes", "glucosa", "insulina"]
            }
            etiquetas = set()
            texto_lower = texto.lower()
            for tag, palabras in temas.items():
                if any(p in texto_lower for p in palabras):
                    etiquetas.add(tag)
            return etiquetas

        # HTML y estilos del carrusel
        carrusel_html = """
        <style>
        .card-cientifica {
            flex: 0 0 auto;
            width: 320px;
            background-color: #1a1a1a;
            color: #f0f0f0;
            border-radius: 12px;
            box-shadow: 4px 4px 12px rgba(0,0,0,0.3);
            padding: 16px;
            transition: transform 0.2s ease-in-out;
        }
        .card-cientifica:hover {
            transform: scale(1.02);
        }
        .card-cientifica h4 {
            margin-top: 8px;
            font-size: 18px;
        }
        .card-cientifica p {
            font-size: 13px;
            color: #ccc;
        }
        .carrusel-container {
            display: flex;
            overflow-x: auto;
            gap: 20px;
            padding: 10px;
        }
        .tag {
            background-color: #2b2b2b;
            color: #6dd3ff;
            font-size: 11px;
            padding: 4px 8px;
            margin: 2px 4px 2px 0;
            display: inline-block;
            border-radius: 8px;
            font-weight: bold;
        }
        </style>
        <div class="carrusel-container">
        """

        for est in estudios[:8]:
            etiquetas = extraer_etiquetas(est["titulo"] + " " + est["resumen"])
            tags_html = " ".join([f"<span class='tag'>#{tag}</span>" for tag in etiquetas])

            card = f"""
            <div class="card-cientifica">
                {tags_html}
                <h4>{est['titulo'][:60]}...</h4>
                <p><strong>{est['fecha']}</strong> — {est['autores'][:40]}...</p>
                <p>{est['resumen'][:110]}...</p>
                <a href="{est['url']}" target="_blank" style="color: #6dd3ff;">Leer estudio completo</a>
            </div>
            """
            carrusel_html += card

        carrusel_html += "</div>"
        components.html(carrusel_html, height=370)
    else:
        st.warning("No se pudieron cargar los estudios en este momento.")





        
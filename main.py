import pandas as pd
import streamlit as st
from utils.imc import calcular_imc, clasificar_imc
from utils.calorias import calcular_tmb, calcular_calorias_objetivo
from utils.alimentos import buscar_alimento
from utils.ejercicio import generar_rutina_biseriada
from utils.timer import iniciar_timer_minutos, iniciar_timer_segundos, reproducir_alarma
from utils.postres import obtener_postre_random, obtener_postre_total_random, obtener_postre_por_categoria, POSTRES_CATEGORIZADOS
from utils.suplementos import recomendar_suplementos
from utils.lista_mercado import obtener_lista_mercado_fit, generar_lista_personalizada
from utils.noticias import obtener_estudios_nutricion
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

# --- Cache para estudios científicos ---
@st.cache_data(ttl=3600)
def obtener_estudios_cached():
    return obtener_estudios_nutricion()

# --- Función para cargar animaciones Lottie desde una URL ---
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Método Cerón", layout="centered")
st.title("🏋️‍♂️ Método Cerón - Asistente Fitness Inteligente")

# --- Animación y carrusel de estudios científicos ---
st.markdown("### 🧬 Estudios científicos recientes sobre nutrición")
st.caption("Explora los últimos avances y estudios abiertos de nutrición, salud y bienestar:")

animacion_news = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_j1adxtyb.json")
st_lottie(animacion_news, height=200, key="news_loader")

estudios = obtener_estudios_cached()
if estudios:
    carrusel_html = """
    <div style="display: flex; overflow-x: auto; gap: 16px; padding: 10px;">
    """
    for est in estudios[:5]:
        card = f"""
        <div style="flex: 0 0 auto; width: 320px; border: 1px solid #ddd; border-radius: 10px; overflow: hidden; box-shadow: 2px 2px 5px #ccc;">
            <div style="padding: 12px;">
                <strong>{est['titulo'][:70]}...</strong>
                <p style="font-size: 13px;">{est['resumen'][:100]}...</p>
                <p style="font-size: 12px; color: gray;">{est['autores']} - {est['fecha']}</p>
                <a href="{est['url']}" target="_blank">Leer estudio completo</a>
            </div>
        </div>
        """
        carrusel_html += card
    carrusel_html += "</div>"
    components.html(carrusel_html, height=330)
else:
    st.info("Cargando estudios científicos...")




# --- Tabs ---
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "🢍 IMC", "🔥 Calorías Objetivo", "🥦 Alimentos",
    "🏋️ Rutina Cerón", "🍩 Postre Fit", "⏰ Timer",
    "🍽️ Postres filtrados", "💊 Suplementos", "🛒 Mercado Fit", "📃 Estudios Científicos"
])





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
# TAB 10 - Noticias Fitness Diarias
# -------------------------------


with tab10:
    st.subheader("🧠 Estudios Científicos de Nutrición y Fitness")
    st.caption("Fuente: Europe PMC")

    estudios = obtener_estudios_nutricion()
    if estudios:
        for estudio in estudios:
            with st.expander(estudio["titulo"]):
                st.markdown(f"**Autores:** {estudio['autores']}")
                st.markdown(f"**Fecha:** {estudio['fecha']}")
                st.write(estudio["resumen"])
                st.markdown(f"[Leer estudio completo]({estudio['url']})")
    else:
        st.warning("No se pudieron cargar los estudios en este momento.")




















# --- Configuración Inicial ---
st.set_page_config(page_title="Método Cerón", layout="centered")
st.title("🏋️‍♂️ Método Cerón - Asistente Fitness Inteligente")

# --- Carga animación desde URL ---
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animacion_news = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_j1adxtyb.json")
st_lottie(animacion_news, height=200, key="news_loader")

st.markdown("### 🔬 Estudios científicos recientes sobre nutrición")
st.caption("Explora los últimos avances y estudios abiertos de nutrición, salud y bienestar:")

# --- Carrusel de estudios científicos ---
estudios = obtener_estudios_nutricion()

if estudios:
    carrusel_html = """
    <div style="display: flex; overflow-x: auto; gap: 16px; padding: 10px;">
    """
    for est in estudios[:5]:
        card = f"""
        <div style="flex: 0 0 auto; width: 320px; border: 1px solid #ddd; border-radius: 10px; overflow: hidden; box-shadow: 2px 2px 5px #ccc;">
            <div style="padding: 12px;">
                <strong>{est['titulo'][:70]}...</strong>
                <p style="font-size: 13px;">{est['resumen'][:100]}...</p>
                <p style="font-size: 12px; color: gray;">{est['autores']} - {est['fecha']}</p>
                <a href="{est['url']}" target="_blank">Leer estudio completo</a>
            </div>
        </div>
        """
        carrusel_html += card
    carrusel_html += "</div>"
    components.html(carrusel_html, height=320)
else:
    st.info("Cargando estudios científicos...")

# --- Tabs ---
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "🢍 IMC", "🔥 Calorías Objetivo", "🥦 Alimentos",
    "🏋️ Rutina Cerón", "🍩 Postre Fit", "⏰ Timer",
    "🍽️ Postres filtrados", "💊 Suplementos", "🛒 Mercado Fit", "📃 Estudios Científicos"
])

# El resto de las tabs continúa exactamente igual que tu versión anterior.

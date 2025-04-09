# utils/timer.py
import time
import streamlit as st
from datetime import timedelta

# Temporizador de minutos
def iniciar_timer_minutos(minutos):
    tiempo_total = minutos * 60
    barra = st.progress(0, text="⏱️ Contador de minutos")
    for i in range(tiempo_total):
        time.sleep(1)
        barra.progress((i + 1) / tiempo_total, text=f"{minutos - (i + 1) // 60} min {59 - (i % 60)} seg restantes")
    st.success("¡Tiempo completado!")
    st.balloons()

# Temporizador de segundos
def iniciar_timer_segundos(segundos):
    barra = st.progress(0, text="⏱️ Contador de segundos")
    for i in range(segundos):
        time.sleep(1)
        barra.progress((i + 1) / segundos, text=f"{segundos - i - 1} segundos restantes")
    st.success("¡Tiempo completado!")
    st.balloons()

# Simulación de alarma (mensaje y emoji, sin sonido por ahora)
def reproducir_alarma():
    st.warning("⏰ ¡Alarma! El temporizador ha terminado. ¡A darle duro!")

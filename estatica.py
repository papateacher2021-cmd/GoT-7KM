import streamlit as st
import os

st.set_page_config(page_title="Westeros 3D & Interactive Map", layout="wide")

# --- Reproductor de Música Medieval en la barra lateral ---
st.sidebar.title("⚔️ Ambiente Medieval")
audio_path = "ambient_music.mp3"

if os.path.exists(audio_path):
    st.sidebar.audio(audio_path, format="audio/mp3", loop=True)
else:
    st.sidebar.info("Coloca 'ambient_music.mp3' en la carpeta para escuchar la música de fondo.")

# --- Vista del Mapa Personalizado ---
st.title("⚔️ Interactive Map of the Seven Kingdoms")
st.markdown("### *Mapa de los Seven Kingdoms para disfrute de mi amada esposa Monica*")

MAP_IMAGE_PATH = "Westeros_Full_Map.jpeg"

if os.path.exists(MAP_IMAGE_PATH):
    st.image(MAP_IMAGE_PATH, use_container_width=True)
else:
    st.warning("Guarda la imagen generada como 'Westeros_Full_Map.jpg' en la carpeta de tu proyecto.")

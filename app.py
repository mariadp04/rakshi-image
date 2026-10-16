import streamlit as st

st.set_page_config(
    page_title="RAKSHI Image Computer",
    page_icon="🖼️",
    layout="centered"
)

st.title("🖼️ RAKSHI Image Computer")
st.write("Describe una imagen. RAKSHI investiga referencias, mejora tu idea y la convierte en una imagen.")

idea = st.text_area(
    "Escribe tu idea",
    placeholder="Ejemplo: un gato astronauta flotando sobre Barcelona al atardecer"
)

estilo = st.selectbox(
    "Elige un estilo",
    ["Cinematográfico", "Realista", "Anime", "Fantasía", "Ilustración", "Logo", "Pixel art"]
)

formato = st.selectbox(
    "Elige el formato",
    ["Cuadrado", "Vertical", "Horizontal"]
)

if st.button("Generar imagen"):
    if idea.strip() == "":
        st.warning("Escribe primero una idea.")
    else:
        st.info("Próximamente: aquí se conectará el generador de imágenes.")
        st.write(f"**Idea:** {idea}")
        st.write(f"**Estilo:** {estilo}")
        st.write(f"**Formato:** {formato}")

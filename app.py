import streamlit as st

st.set_page_config(
    page_title="RAKSHI",
    page_icon="🌌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo oscuro tipo ChatGPT / Perplexity
st.markdown("""
<style>
    .stApp {
        background-color: #0b0f19;
        color: #e6e9f2;
    }
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }
    h1, h2, h3, p, span {
        color: #e6e9f2;
    }
    .stChatMessage {
        background-color: #151b2b;
        border-radius: 16px;
        border: 1px solid #232b3d;
    }
    .stButton > button {
        background-color: #6d5efc;
        color: white;
        border-radius: 12px;
        border: none;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #7f72ff;
    }
    div[data-testid="stChatInput"] {
        border-radius: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Cabecera
st.markdown("## 🌌 RAKSHI")
st.markdown("Tu asistente para crear imágenes con inteligencia artificial.")

# Mostrar conversación
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada estilo chat
prompt = st.chat_input("Describe la imagen que quieres crear...")

if prompt:
    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta provisional de RAKSHI
    respuesta = (
        f"He recibido tu idea:\n\n**{prompt}**\n\n"
        "Próximamente mejoraré este texto con Gemini y generaré la imagen. "
        "Por ahora, RAKSHI está en fase de diseño."
    )

    with st.chat_message("assistant"):
        st.markdown(respuesta)

    st.session_state.messages.append(
        {"role": "assistant", "content": respuesta}
    )

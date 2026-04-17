import streamlit as st
from src.predict import runPredict

# -------------------------------
# Congfiguración de la página | Page configuration
# -------------------------------
st.set_page_config(
    page_title="Predicción de Penales",
    page_icon="⚽",
    layout="centered"
)

st.title("⚽ Predicción de Penales")

st.write("Ingresa los datos del tiro penal:")

# -------------------------------
# Inputs del usuario | User inputs
# -------------------------------

# Pie dominante
Kicker_Foot = st.selectbox(
    "Pie dominante del jugador",
    [ "Derecha", "Izquierda"]
)

if Kicker_Foot == "Derecha":
    Kicker_Foot = "R"
if Kicker_Foot == "Izquierda":
    Kicker_Foot = "L"


# Marcador actual del partido | Current match score
col1, col2 = st.columns(2)

with col1:
    Home_Goals = st.number_input("Goles Local", min_value=0, step=1)

with col2:
    Away_Goals = st.number_input("Goles Visitante", min_value=0, step=1)

# Minuto del partido | Match minute
Minute = st.slider(
    "Minuto del partido",
    min_value=1,
    max_value=90,
    value=45,
    step=1
)

# Equipo rival | Opponent team
Team_Type = st.selectbox(
    "Equipo rival",
    ["Local", "Visitante"]
)

if Team_Type == "Local":
    Team_Type = "H"
if Team_Type == "Visitante":
    Team_Type = "A"


# -------------------------------
# Boton de prediccion | Prediction button
# -------------------------------

# Crear diccionario con datos ingresados | Create dictionary with entered data
dataPredict = {
    "Kicker_Foot": Kicker_Foot,
    "Home_Goals": Home_Goals,
    "Away_Goals": Away_Goals,
    "Minute": Minute,
    "Team_Type": Team_Type
}

if st.button("Predecir"):
    # Mostrar spinner mientras se realiza la predicción | Show spinner while making prediction
    with st.spinner("Realizando prediccion..", show_time=True):
        result = runPredict(dataPredict)
        
    st.subheader("El jugador elegirá:")
    st.success(result)

    # Mostrar datos ingresados | Show entered data
    st.write("Datos ingresados:")
    st.write({
        "Kicker_Foot": Kicker_Foot,
        "Home_Goals": Home_Goals,
        "Away_Goals": Away_Goals,
        "Minute": Minute,
        "Team_Type": Team_Type
    })
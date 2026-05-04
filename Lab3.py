import streamlit as st
import pandas as pd

st.title("Bienvenido")

vehiculos = pd.read_csv("Electric_Vehicle_Population.csv")
gimnasio = pd.read_csv("GymExerciseTracking.csv")
videojuegos = pd.read_csv("steam_store_data_2024.csv")
netflix = pd.read_csv("netflix_titles.csv")

datasets = {
    "vehiculos":vehiculos,
    "gimnasio":gimnasio,
    "videojuegos":videojuegos,
    "netflix":netflix
}

opciones = st.selectbox(
    "Selecciona una base de datos",
    ["None", "vehiculos", "gimnasio", "videojuegos", "netflix"]
)

if opciones in datasets:
    dataset = datasets[opciones]
    dataset.index = dataset.index + 1
    st.subheader(f"Base de datos {opciones}")
    st.write(dataset.head(6))
    st.write(dataset.shape)

    estadisticas = list(dataset.select_dtypes(include="number").columns)
    st.subheader("Que estadistica queires ver?")
    seleccionestadisticas = st.selectbox(
        " ",
        [None] + estadisticas
    )
    if seleccionestadisticas:
        st.write(dataset[seleccionestadisticas].describe())

    st.subheader(f"Columnas {opciones}")
    for columnas in dataset.columns:
        st.write(columnas)
    

    
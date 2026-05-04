import streamlit as st
import pandas as pd

st.title("Bienvenido")

vehiculos = pd.read_csv("Electric_Vehicle_Population.csv")
gimnasio = pd.read_csv("GymExerciseTracking.csv")
videojuegos = pd.read_csv("steam_store_data_2024.csv")
netflix = pd.read_csv("netflix_titles.csv")

opciones = st.selectbox(
    "Selecciona una base de datos",
    ["vehiculos", "gimnasio", "videojuegos", "netflix"]
)
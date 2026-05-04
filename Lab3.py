import streamlit as st
import pandas as pd

st.title("Bienvenido a tu base de datos")

vehiculos = pd.read_csv("Electric_Vehicle_Population.csv")
gimnasio = pd.read_csv("GymExerciseTracking.csv")
videojuegos = pd.read_csv("steam_store_data_2024.csv")
netflix = pd.read_csv("netflix_titles.csv")


if "datos_gimnasio" not in st.session_state:
    st.session_state.datos_gimnasio = gimnasio.copy()
if "datos_videojuegos" not in st.session_state:
    st.session_state.datos_videojuegos = videojuegos.copy()


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
    
    if opciones == "gimnasio":
        dataset = st.session_state.datos_gimnasio
    elif opciones == "videojuegos":
        dataset = st.session_state.datos_videojuegos
    else:
        dataset = datasets[opciones]

    st.subheader(f"Base de datos {opciones}")
    st.write(dataset.head(6))
    st.write(dataset.shape)

    if opciones == "vehiculos":
        with st.expander("Filtrar por..."):
            seleccion_filtrado = st.selectbox(
                "Filtrar por...",
                ["Año", "Precio"]
            )
            if seleccion_filtrado == "Año":
                filtro_año =st.number_input("Modelo anterior al año ", min_value=2000, max_value=2025)
                st.write(vehiculos[vehiculos["Model Year"] < filtro_año])

            elif seleccion_filtrado == "Precio":
                filtro_precio =st.number_input("Precio menor a ", min_value=0.0, max_value=845000.00)
                st.write(vehiculos[vehiculos["Base_MSRP"] < filtro_precio])

            

    elif opciones == "gimnasio":
        copia_gimnasio = st.session_state.datos_gimnasio

        with st.expander("Filtrar por..."):
            seleccion_filtrado = st.selectbox(
                "Filtrar por...",
                ["Calorias quemadas", "Porcentaje de grasa"]
            )
            if seleccion_filtrado == "Calorias quemadas":
                filtro_calorias =st.number_input("Calorias quemadas mayor o igual a ", min_value=0.0)
                st.write(copia_gimnasio[copia_gimnasio["Calories_Burned"] >= filtro_calorias])

            elif seleccion_filtrado == "Porcentaje de grasa":
                filtro_porcentaje =st.number_input("Porcentaje de grasa menor o igual a ", min_value=0.0)
                st.write(copia_gimnasio[copia_gimnasio["Fat_Percentage"] <= filtro_porcentaje])

        with st.expander("Agregar nuevo registro"):
            nuevo_registro_gimnasio = {}
            
            for columnas in copia_gimnasio.columns:
                if copia_gimnasio[columnas].dtype == "object":
                    valor = st.text_input(f"{columnas}")
                
                else:
                    valor = st.number_input(f"{columnas}")
                nuevo_registro_gimnasio[columnas] = valor

            if st.button("Agregar"):
                nueva_fila = pd.DataFrame([nuevo_registro_gimnasio])
                st.session_state.datos_gimnasio = pd.concat([st.session_state.datos_gimnasio, nueva_fila], ignore_index=True)
                st.success("Agregado correctamente")
        
        

    elif opciones == "videojuegos":
        copia_videojuegos = st.session_state.datos_videojuegos

        with st.expander("Filtrar por..."):
            seleccion_filtrado = st.selectbox(
                "Filtrar por...",
                ["Precio", "Descuento"]
            )
            if seleccion_filtrado == "Precio":
                filtro_precio =st.number_input("Precio mayor a ", min_value=0.0)
                st.write(copia_videojuegos[copia_videojuegos["price"] > filtro_precio])

            elif seleccion_filtrado == "Porcentaje de grasa":
                filtro_porcentaje =st.number_input("Porcentaje de grasa menor o igual a ", min_value=0.0)
                st.write(copia_videojuegos[copia_videojuegos["salePercentage"] <= filtro_porcentaje])


        with st.expander("Agregar nuevo registro"):
            nuevo_registro_videojuegos = {}
            
            for columnas in copia_videojuegos.columns:
                if copia_videojuegos[columnas].dtype == "object":
                    valor = st.text_input(f"{columnas}")
                
                else:
                    valor = st.number_input(f"{columnas}")
                nuevo_registro_videojuegos[columnas] = valor

            if st.button("Agregar"):
                nueva_fila = pd.DataFrame([nuevo_registro_videojuegos])
                st.session_state.datos_videojuegos = pd.concat([st.session_state.datos_videojuegos, nueva_fila], ignore_index=True)
                st.success("Agregado correctamente")

    elif opciones == "netflix":
        with st.expander("Filtrar por..."):
            seleccion_filtrado = st.selectbox(
                "Filtrar por...",
                ["Duracion", "Ultima actualizacion"]
            )
            if seleccion_filtrado == "Duracion":
                filtro_duracion =st.number_input("Duracion mayor a ")
                st.write(netflix[netflix["duration"] > filtro_duracion])

            elif seleccion_filtrado == "Ultima actualizacion":
                filtro_actualizaion =st.number_input("Ultima actualizacion antes del año ")
                st.write(netflix[netflix["date_added"] < filtro_actualizaion])


    estadisticas = list(dataset.select_dtypes(include="number").columns)
    with st.expander("Estadisticas"):
        seleccionestadisticas = st.selectbox(
            " ",
            [None] + estadisticas
        )
        if seleccionestadisticas:
            st.write(dataset[seleccionestadisticas].describe())

    with st.expander(f"Columnas {opciones}"):
        for columnas in dataset.columns:
            st.write(columnas)

    
    

    
import streamlit as st
import joblib
import numpy as np
import pandas as pd

#Titulo de la pagina
st.title("Predictor")

#breve descripcion de la pag

st.markdown("""
    * En esta página se pueden ingresar las caracteristicas de los hogares y estimar el precio de la vivienda
            """)

#se define ruta del modelo formato pkl

model_filename = 'precios.pkl'

#se carga el modelo
loaded_model = joblib.load(model_filename)


with st.form('predictor'):
    rm = st.text_input(label="Número de habitaciones por vivienda")
    zn = st.text_input(label="Proporción de terrenos zonificados")
    ptratio = st.text_input(label="Número de estudiantes por maestro")
    indus = st.text_input(label="Proporción de acres de negocios no minoristas")

    submit = st.form_submit_button(label='Enviar')
    if submit:
        # Validación: Convertir valores a float y manejar errores
        try:
             rm = float(rm) if rm else None
             zn = float(zn) if zn else None
             ptratio = float(ptratio) if ptratio else None
             indus = float(indus) if indus else None

             if None in [rm, zn, ptratio, indus]:
                st.error("Por favor, llena todos los campos correctamente.")
             else:        
                input = pd.DataFrame({
                    "RM": [rm],
                    "ZN": [zn],
                    "PTRATIO": [ptratio],
                    "LSTAT": [indus]
                })
                predicted_price = loaded_model.predict(input)

                st.success(f"El precio estimado de la casa es: ${predicted_price[0][0]:.2f} mil dolares")
        except ValueError:
            st.error("Por favor, ingresa solo valores numéricos.")
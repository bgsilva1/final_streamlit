import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Titulo de la pagina
st.title("Modelo")

#breve descripcion de la pag

st.markdown("""
    * En esta página se muestran las diferentes metricas de los modelos estimados.
    * El mejor modelo estimado en base  (MSE, RMSE y R2) es el modelo 1 de regresión lineal.
    * El modelo 2 ridge tambien tiene metricas muy similares pero por debajo a la regresión lineal.
            """)

#Grafico se MSE de los modelos estimados
#importo archivo de metricas

metricas = pd.read_csv("metricas.csv")

st.dataframe(metricas) 

option = st.selectbox(
    "Que metrica visualizar?",
    ("Mean Absolute Error", "Mean Squared Error", "Root Mean Squared Error", "R2"),
    index=None,
    placeholder="Evaluacion de modelo",
)

if option == "Mean Absolute Error":
    st.bar_chart(data=metricas.loc[metricas['metrica'] == "MAE"], 
             x="metrica",
             stack=False)
elif option == "Mean Squared Error":
    st.bar_chart(data=metricas.loc[metricas['metrica'] == "MSE"], 
             x="metrica",
             stack=False)
elif option == "Root Mean Squared Error":
    st.bar_chart(data=metricas.loc[metricas['metrica'] == "RMSE"], 
             x="metrica",
             stack=False)
elif option == "R2":
    st.bar_chart(data=metricas.loc[metricas['metrica'] == "R2"], 
             x="metrica",
             stack=False)
else:
    st.write("Loading")
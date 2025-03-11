import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

# -- Set page config
#Configurar nombre en pestana e icono
apptittle = 'Trabajo final'

st.set_page_config(page_title=apptittle, page_icon=":eyeglasses:")

# configurar navegacion
#Inicio - Dashboard
#Modelo
#Predictor
#Acerca de

inicio =  st.Page("pages/inicio.py", 
                  title="Inicio")

chat = st.Page("pages/chat.py",
               title="Chat IA")

modelo = st.Page("pages/modelo.py",
                 title="Metricas")

predictor = st.Page("pages/predictor.py",
                    title="Modelo")

acerca = st.Page("pages/acerca.py",
                 title="Acerca de")

#declarar navigation

pg = st.navigation(
    {
        "Inicio": [inicio, predictor, chat],
        "Ajuste del modelo": [modelo],
        "Acerca de": [acerca]
    }
)


pg.run()




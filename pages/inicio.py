import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

#cargar base
boston = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")



#histograma precio
fig, ax = plt.subplots()
sns.histplot(boston, x="medv" ,bins=30, kde=True)  # kde=True agrega la densidad estimada
plt.xlabel("Precio de las casas*")
plt.ylabel("Frecuencia")
plt.title("Histograma de datos precio de casas (MEDV)")
#plt.show()

fig2 = px.histogram(boston, x="medv", nbins=30, title="Distribución del precio de las casas")
fig2.update_traces(marker=dict(color='#7C9EB2',line=dict(width=2, color='white')))
fig2.update_layout(
    xaxis_title="Precio de las casas*",
    yaxis_title="Frecuencia"
)


#histograma rm
fig3 = px.histogram(boston, x="rm", nbins=30, title="Distribución del Número de habitaciones")
fig3.update_traces(marker=dict(color='#52528C',line=dict(width=2, color='white')))
fig3.update_layout(
    xaxis_title="Número de habitaciones",
    yaxis_title="Frecuencia"
)

#histograma zn
fig4 = px.histogram(boston, x="zn", nbins=30, title="Distribución del proporción de terrenos residenciales zonificados para lotes de más de 25.000 pies cuadrados")
fig4.update_traces(marker=dict(color='#372554',line=dict(width=2, color='white')))
fig4.update_layout(
    xaxis_title="Proporción de terrenos residenciales*",
    yaxis_title="Frecuencia"
)

#histograma ptratio
fig5 = px.histogram(boston, x="ptratio", nbins=30, title="pupil-teacher ratio by town")
fig5.update_traces(marker=dict(color='#8499B1',line=dict(width=2, color='white')))
fig5.update_layout(
    xaxis_title="Número de estudiantes por maestro",
    yaxis_title="Frecuencia"
)

#histograma indus
fig6 = px.histogram(boston, x="indus", nbins=30, title="proporción de acres de negocios no minoristas por ciudad")
fig6.update_traces(marker=dict(color='#231123',line=dict(width=2, color='white')))
fig6.update_layout(
    xaxis_title="Proporción de acres de negocios no minoristas",
    yaxis_title="Frecuencia"
)

#Scatter plot 
fig7=px.scatter(boston, y="medv", x="indus",
                title="Relacion precio zona de acres")
fig7.update_traces(marker=dict(color='#a5c4d4',line=dict(width=2, color='white')))
fig7.update_layout(
    xaxis_title="Proporción de acres de negocios no minoristas",
    yaxis_title="Precio de las casas"
)




#medidas de tendencia central medv
mean = round(np.mean(boston['medv']),2)
med = round(np.median(boston['medv']),2)
dstd = round(np.std(boston['medv']),2)

#medidas de tendencia central rm
mean_rm = round(np.mean(boston['rm']),2)
med_rm = round(np.median(boston['rm']),2)
dstd_rm = round(np.std(boston['rm']),2)

#medidas de tendencia central zn
mean_zn = round(np.mean(boston['zn']),2)
med_zn = round(np.median(boston['zn']),2)
dstd_zn = round(np.std(boston['zn']),2)

#medidas de tendencia central ptratio
mean_ptratio = round(np.mean(boston['ptratio']),2)
med_ptratio = round(np.median(boston['ptratio']),2)
dstd_ptratio = round(np.std(boston['ptratio']),2)

#medidas de tendencia central indus
mean_indus = round(np.mean(boston['indus']),2)
med_indus = round(np.median(boston['indus']),2)
dstd_indus = round(np.std(boston['indus']),2)


#-----------Front----------------------

#Titulo de la pagina
st.title("Inicio")

#breve descripcion

st.markdown("""
    Este es un aplicativo diseñado para predecir los precios de casas
    Se utilizan las siguientes variables:
    * Numero de habitaciones por vivienda
    * Proporción de terrenos residenciales zonificados para lotes de más de 25.000 pies cuadrados
    * Ratio estudiante-maestros
    * proporción de acres de negocios no minoristas por ciudad
    
    En la pagina de modelo se habla acerca de la selecicon del modelo
    En lapagina predictor se pueden ingresar las caracteristicas de la casa y predecir su precio      """)

#MEDV
st.header('Precio de la vivienda')

a, b = st.columns(2)

a.plotly_chart(fig2)
b.metric("Promedio", mean, border=True)
b.metric("Mediana", med, border=True)
b.metric("Desviacion Estandar", dstd ,  border=True)

#RM
st.subheader('Numero de habitaciones por vivienda')

c, d = st.columns(2)

c.plotly_chart(fig3)
d.metric("Promedio", mean_rm,  border=True)
d.metric("Mediana", med_rm, border=True)
d.metric("Desviacion Estandar", dstd_rm, border=True)

#ZN
st.subheader('Proporción de terrenos residenciales zonificados')

e, f = st.columns(2)

e.plotly_chart(fig4)
f.metric("Promedio", mean_zn, border=True)
f.metric("Mediana", med_zn, border=True)
f.metric("Desviacion Estandar", dstd_zn, border=True)


#Ptratio
st.subheader('Ratio estudiante-maestro')

g, h = st.columns(2)

g.plotly_chart(fig5)
h.metric("Promedio", mean_ptratio, border=True)
h.metric("Mediana", med_ptratio, border=True)
h.metric("Desviacion Estandar", dstd_ptratio, border=True)

#indus
st.subheader('proporción de acres de negocios no minoristas por ciudad')

i, j = st.columns(2)

i.plotly_chart(fig6)
j.metric("Promedio", mean_indus, border=True)
j.metric("Mediana", med_indus, border=True)
j.metric("Desviacion Estandar", dstd_indus, border=True)


#scatter plot
st.subheader("Relacion entre variables")

# Diccionario para mapear nombres del desplegable a columnas del dataset
column_map = {
    "Precio de la casa": "medv",
    "Numero de habitaciones": "rm",
    "Terrenos residenciales zonificados": "zn",
    "Ratio estudiante maestro": "ptratio",
    "proporcion de acres no minoristas": "indus"
}

# Menús desplegables en Streamlit
option_x = st.selectbox(
    "Variable en el eje X:",
    list(column_map.keys()),
    index=None,
    placeholder="Selecciona variable para X"
)

option_y = st.selectbox(
    "Variable en el eje Y:",
    list(column_map.keys()),
    index=None,
    placeholder="Selecciona variable para Y"
)

# Verificar que se haya seleccionado ambas variables antes de graficar
if option_x and option_y:
    fig7 = px.scatter(boston, x=column_map[option_x], y=column_map[option_y],
                      title=f"Relación entre {option_x} y {option_y}")

    fig7.update_traces(marker=dict(line=dict(width=0.5, color='white')))
    
    fig7.update_layout(
        xaxis_title=option_x,
        yaxis_title=option_y
    )
    
    st.plotly_chart(fig7)
else:
    st.warning("Por favor, selecciona variables en ambos ejes.")

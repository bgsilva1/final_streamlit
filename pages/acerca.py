import streamlit as st

#Titulo de la pagina
st.title("Acerca de")

#breve descripcion de la pag

st.markdown("""
    * Esta página fue desarrollada por Bryan Silva. Econommista entusiasta por los datos. :)
            """)

#import streamlit as st
#import time
#
#'Starting a long computation...'
#
## Add a placeholder
#latest_iteration = st.empty()
#bar = st.progress(0)
#
#for i in range(100):
#  # Update the progress bar with each iteration.
#  latest_iteration.text(f'Iteration {i+1}')
#  bar.progress(i + 1)
#  time.sleep(0.1)
#
#'...and now we\'re done!'

st.title("Distribución de 4 Columnas y 2 Filas en Streamlit")

# Primera fila
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write("Columna 1 - Fila 1")
    st.button("Botón 1")
with col2:
    st.write("Columna 2 - Fila 1")
    st.button("Botón 2")
with col3:
    st.write("Columna 3 - Fila 1")
    st.button("Botón 3")
with col4:
    st.write("Columna 4 - Fila 1")
    st.button("Botón 4")

# Segunda fila
col5, col6, col7, col8 = st.columns(4)
with col5:
    st.write("Columna 1 - Fila 2")
    st.button("Botón 5")
with col6:
    st.write("Columna 2 - Fila 2")
    st.button("Botón 6")
with col7:
    st.write("Columna 3 - Fila 2")
    st.button("Botón 7")
with col8:
    st.write("Columna 4 - Fila 2")
    st.button("Botón 8")
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
import json
import streamlit as st

boston = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")
boston_f = boston[["medv", "rm", "zn","ptratio", "indus"]]

st.title("CHAT IA")
st.write("Chatea con la base de datos")




with st.form('chat'):
     st.write("Consulta por medio de un prompt al data frame")
     user_input = st.text_input("Haz tu pregunta")



     submit = st.form_submit_button(label='Go')
     if submit:
        prompt=f"Eres un asistente experto en análisis de datos. Tu tarea es responder preguntas basadas en el DataFrame proporcionado.\
                 No incluyas código Python ni explicaciones técnicas sobre cómo obtienes la respuesta. \
                 Responde de manera clara y concisa, utilizando lenguaje natural.\
                 Pregunta: {user_input}"

        chat = ChatMistralAI(api_key=st.secrets.general.api__key,temperature = 0.7,model="mistral-large-latest")

        agent_executor = create_pandas_dataframe_agent(chat,
                                                    boston_f,
                                                    verbose=False,
                                                    allow_dangerous_code=True,
                                                    agent_type="tool-calling")

        ai_msg = agent_executor.invoke(prompt)
         # Convertir el JSON a un diccionario de Python
        data_dict = json.loads(json.dumps(ai_msg))

         # Extraer el valor del campo 'output'
        output_value = data_dict["output"]

         # Imprimir el resultado
        st.write(output_value)
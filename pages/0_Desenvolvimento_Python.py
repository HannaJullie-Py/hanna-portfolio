import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Desenvolmento Python',
    page_icon='https://cdn.iconscout.com/icon/free/png-256/free-python-3521655-2945099.png', # Esse é um URL como Favicon, pode ser um emoji ou outra imagem.
)

col1, col2, col3 = st.columns(3)

with col2:
    st.title("Desenvolvimento Python")
    st.write("Nesta pagina você irá ver alguns dos meus dotes no python. Projetos e joguinhos não estão de fora. Se divirte e veja se gosta de como eu escrevo meus códigos!!!")

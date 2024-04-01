import streamlit as st
import pandas as pd
import numpy as np
import subprocess



st.set_page_config(
    page_title='Desenvolmento Python',
    page_icon='https://cdn.iconscout.com/icon/free/png-256/free-python-3521655-2945099.png', # Esse é um URL como Favicon, pode ser um emoji ou outra imagem.
)


st.header("Desenvolvimento Python")
st.write("Nesta pagina você irá ver alguns dos meus dotes no python. Projetos e joguinhos não estão de fora. Se divirta e veja se gosta de como eu escrevo meus códigos!!!")
st.divider
st.title("Tap Code Translate")
st.write("Código que traduz português para uma codifição chamada Tap Code. obs: não use acentos!!!")
code = subprocess.run(['python','https://github.com/HannaJullie-Py/hanna-portfolio/blob/main/pages/tap_code_translate_by_hanna_(ver_0_1).py'])
st.code(code)

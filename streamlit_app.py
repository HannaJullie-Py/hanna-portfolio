import streamlit as st
import numpy as np
import pandas as pd

# Altera o nome do site e o favicon
st.set_page_config(
    page_title='Portifólio da Hanna',
    page_icon='https://i.imgur.com/FH02wR3.png', # Esse é um URL como Favicon, pode ser um emoji ou outra imagem.
)

col1, col2 = st.columns(2)
with col1:
    st.image('https://i.imgur.com/nw0vi8l.png')

with col2:
    st.title('Quem sou eu?')
    st.write('Meu nome é Hanna Patrocinio, sou desenvolvedora em python, artista em pixel, aspirante à poeta e musicista. Comecei na área de programação há pouco tempo, tenho formação em Python e MySQL. Sou artista desde que me conheço por gente, arte é vida. ')

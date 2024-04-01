import streamlit as st
import pandas as pd
import numpy as np
import time 

st.set_page_config(
    page_title='Criação de Músicas',
    page_icon='https://github.com/HannaJullie-Py/hanna-portfolio/blob/main/download.png?raw=true'
)

st.title('Criação de Músicas')
st.write('Nesta Página, você verá as melhores músicas que eu fiz nesses longos anos como produtora musical. Aproveite!')
st.divider()
col1, col2, col3 = st.columns(3)
with col2:
    st.markdown('#Hanna Jullie - Sangue Azul')
st.video("https://www.youtube.com/watch?v=wuXSKruNcaA")
st.divider

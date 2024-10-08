import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Pixel Arts',
    page_icon='🖌️', # Esse é um emoji como Favicon, pode ser um URL ou outra imagem.
)

st.title("Pixel Arts")
st.write("Nesta página você vê algumas das muitas pixel arts que fiz durante todos os meus anos. Aproveite!")
st.divider()
st.title('Cenários')
st.image("https://i.imgur.com/Rg4nTKk.jpeg")
st.image("https://i.imgur.com/puiqQTj.jpeg")
st.divider()
st.title('Ideias Abstratas')
st.image('https://i.imgur.com/R7BzwP6.jpeg')
st.image('https://i.imgur.com/6xovNV8.jpeg')
st.image('https://i.imgur.com/BbuJcNr.jpeg')
st.image("https://i.imgur.com/faRST8D.png")
st.divider()
st.title('Retratos')
st.image("https://i.imgur.com/nxVyR7s.png")
st.image("https://i.imgur.com/AadOZUA.png")
st.image('https://i.imgur.com/Z9q0eMY.jpg')
st.image("https://i.imgur.com/Qb1UOop.png", caption="Ekko de Arcane/League of Legends")
st.image("https://i.imgur.com/O90LORQ.png")
st.image("https://i.imgur.com/jSF6beH.png", caption="Quem vos fala")
st.image("https://i.imgur.com/8pTPlv2.png")
st.image("https://i.imgur.com/01BfNzC.png")
st.image("https://i.imgur.com/kXYc7bI.png")
st.image("https://i.imgur.com/3e0vkof.png", caption="Minha namorada")
st.image("https://i.imgur.com/taNZ1I0.png")
st.divider()
st.title("Não Relacionados")
st.caption("Não são Pixel Arts ou não são algo que eu normalmente faço.")
st.image("https://i.imgur.com/FH02wR3.png", caption= 'Logo deste site.')
st.image('https://i.imgur.com/TBvRRfw.jpg', caption= 'Logo que fiz para outro site.')
st.divider()
col8, col9, col0 = st.columns(3)
with col9:
    st.write('Todos os direitos reservados | ©')

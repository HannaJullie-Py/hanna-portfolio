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
st.divider()
st.title('Tap Code Translate')
st.caption('Código feito para traduzir Inglês para uma codificação chamada Tap Code e depois de Tap Code para Inglês')


st.write('Tradutor de Palavras para Tap Code')
st.caption("O Tap Code é escrito por você e lido pelo nosso programa da seguinte forma: Você começa pela horizontal e depois para a vertical. Exemplo: A letra 'G' se encontra em 2 (horizontal) e 2 (vertical). Você utiliza pontos espaçados para se comunicar ao invés dos números. Exemplo: A letra 'E' se encontra em: '. .....'. Você utiliza uma barra (/) para dar espaço")
col1, col2, col3 = st.columns(3)
with col2:
    st.title('Alfabeto')
    st.image('https://www.cachesleuth.com/images/tap/tapcode.png')
codigo = st.text_input('Digite o código para o tradutor decodificar')
butao = st.button('Decodificar')  
texto = ''
samo = 0
tradu = ''
codigo += '  '


for cod in codigo:
    if cod == ' ':
        samo +=1
    if samo < 2:
        tradu = tradu + cod
    if cod == '/':
        texto = texto + ' '
    if samo == 2:
        if tradu == '. .':
            texto = texto + 'A'
        if tradu == '. ..':
            texto = texto + 'B'
        if tradu == '. ...':
            texto = texto + 'C'
        if tradu == '. ....':
            texto =  texto + 'D'
        if tradu == '. .....':
            texto = texto + 'E'
        if tradu == '.. .':
            texto = texto + 'F'
        if tradu == '.. ..':
            texto = texto + 'G'
        if tradu == '.. ...':
            texto = texto + 'H'
        if tradu == '.. ....':
            texto = texto + 'I'
        if tradu == '.. .....':
            texto = texto + 'J'
        if tradu == '... .':
            texto = texto + 'L'
        if tradu == '... ..':
            texto = texto + 'M'
        if tradu == '... ...':
            texto = texto + 'N'
        if tradu == '... ....':
            texto = texto + 'O'
        if tradu == '... .....':
            texto = texto + 'P'
        if tradu == '.... .':
            texto = texto + 'Q'
        if tradu == '.... ..':
            texto = texto + 'R'
        if tradu == '.... ...':
            texto = texto + 'S'
        if tradu == '.... ....':
            texto = texto + 'T'
        if tradu == '.... .....':
            texto = texto + 'U'
        if tradu == '..... .':
            texto = texto + 'V'
        if tradu == '..... ..':
            texto = texto + 'W'
        if tradu == '..... ...':
            texto = texto + 'X'
        if tradu == '..... ....':
            texto = texto + 'Y'
        if tradu == '..... .....':
            texto = texto + 'Z'
        tradu = ''
    if samo ==3:
        samo = 0
if butao:
    with st.spinner('Carregando...'):
        time.sleep(5)
    st.caption(f':violet[{texto}]')

st.divider()

st.title('Traduzir de palavras para Tap Code')
frase = st.text_input('Digite o código para o tradutor codificar')
botao = st.button('Codificar')  
for letra in frase:
    lista.append(letra)
    if letra == ' ':
        codu = '/'
        space = True
    if letra == 'A':
        codu = lista[0]
    if letra == 'B':
        codu = lista[1]
    if letra == 'C':
        codu = lista[2]
    if letra == 'D':
        codu = lista[3]
    if letra == 'E':
        codu = lista[4]
    if letra == 'F':
        codu = lista[5]
    if letra == 'G':
        codu = lista[6]
    if letra == 'H':
        codu = lista[7]
    if letra == 'I':
        codu = lista[8]
    if letra == 'J':
        codu = lista[9]
    if letra == 'L':
        codu = lista[10]
    if letra == 'M':
        codu = lista[11]
    if letra == 'N':
        codu = lista[12]
    if letra == 'O':
        codu = lista[13] 
    if letra == 'P':
        codu = lista[14]
    if letra == 'Q':
        codu = lista[15]
    if letra == 'R':
        codu = lista[16]
    if letra == 'S':
        codu = lista[17]
    if letra == 'T':
        codu = lista[18]
    if letra == 'U':
        codu = lista[19]
    if letra == 'V':
        codu = lista[20]
    if letra == 'W':
        codu = lista[21] 
    if letra == 'X':
        codu = lista[22]
    if letra == 'Y':
        codu = lista[23]
    if letra == 'Z':
        codu = lista[24] 
    codi = codi + codu + ' '
for letra in codi:
    if letra == '/':
        p_espaco.append(letra)
        del p_espaco[i-1]
    else:
        p_espaco.append(letra)
        i = i+1
for letra in p_espaco:
    codi_final += letra
if botao:
    with st.spinner('Carregando...'):
        time.sleep(5)
    st.text(codi_final)
st.divider()



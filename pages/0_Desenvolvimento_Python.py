import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Desenvolmento Python',
    page_icon='https://cdn.iconscout.com/icon/free/png-256/free-python-3521655-2945099.png', # Esse é um URL como Favicon, pode ser um emoji ou outra imagem.
)


st.header("Desenvolvimento Python")
st.write("Nesta pagina você irá ver alguns dos meus dotes no python. Projetos e joguinhos não estão de fora. Se divirta e veja se gosta de como eu escrevo meus códigos!!!")
st.divider
st.title("Tap Code Translate")
st.write("Código que traduz português para uma codifição chamada Tap Code. obs: não use acentos!!!")
code = '''

code = ['.','..','...','....','.....', 'print']
code1 = ['.','..','...','....','.....', 'print']
codem = ['']
abc = [' ','A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tradu = ''
texto = ''
codu = ''
codi = ''
i = 0
abc2 =['. .','. ..','. ...','. ....','. .....','.. .','.. ..','.. ...','.. ....','.. .....','... .','... ..','... ...','... ....', '... .....','.... .','.... ..','.... ...','.... ....', '.... .....','..... .','..... ..', '..... ...','..... ....','..... .....']
lista = ['. .','. ..','. ...','. ....','. .....','.. .','.. ..','.. ...','.. ....','.. .....','... .','... ..','... ...','... ....', '... .....','.... .','.... ..','.... ...','.... ....', '.... .....','..... .','..... ..', '..... ...','..... ....','..... .....']
bra = [' ']

while True:
  ##### Começamos fazendo o menu #####
  print ("\nBem vindo ao tradutor de Tap Code")
  print ("\nO que quer fazer?", "\n[1] Traduzir de Tap Code para palavras", "\n[2] Traduzir de palavras para Tap Code", "\n[3] Instruções", "\n[4] O que é Tap Code?", "\n[5] Sair")
  menu = int(input())
  if menu == 1:
    ##### Aqui começa o tradutor de Tap Code para palavras #####
    for i in range(1,241):
      i += 1
      texto = texto + tradu
      print ("##########################","\n##  Tap Code Translate  ##","\n##########################", "\n### [0][1][2][3][4][5] ###","\n### [1](A)(B)(C)(D)(E) ###", "\n### [2](F)(G)(H)(I)(J) ###", "\n### [3](L)(M)(N)(O)(P) ###","\n### [4](Q)(R)(S)(T)(U) ###","\n### [5](V)(W)(X)(Y)(Z) ###","\n##########################")
      codigo = str(input("Digite seu código: "))
      x, y = (str(cod) for cod in codigo.split(' '))
      if (x == '/') and (y == '/'):
        tradu = abc[0]
      if (x == code[0]) and (y == code1[0]):
        trad = x + y
        tradu = abc[1]
      if (x == code[0]) and (y == code[1]):
        trad = x + y
        tradu = abc[2]
      if (x == code[0]) and (y == code[2]):
        trad = x + y
        tradu = abc[3]
      if (x == code[0]) and (y == code[3]):
        trad = x + y
        tradu = abc[4]
      if (x == code[0]) and (y == code[4]):
        trad = x + y
        tradu = abc[5]
      if (x == code[1]) and (y == code[0]):
        trad = x + y
        tradu = abc[6]
      if (x == code[1]) and (y == code[1]):
        trad = x + y
        tradu = abc[7]
      if (x == code[1]) and (y == code[2]):
        trad = x + y
        tradu = abc[8]
      if (x == code[1]) and (y == code[3]):
        trad = x + y
        tradu = abc[9]
      if (x == code[1]) and (y == code[4]):
        trad = x + y
        tradu = abc[10]
      if (x == code[2]) and (y == code[0]):
        trad = x + y
        tradu = abc[11]
      if (x == code[2]) and (y == code[1]):
        trad = x + y
        tradu = abc[12]
      if (x == code[2]) and (y == code[2]):
        trad = x + y
        tradu = abc[13]
      if (x == code[2]) and (y == code[3]):
        trad = x + y
        tradu = abc[14]
      if (x == code[2]) and (y == code[4]):
        trad = x + y
        tradu = abc[15]
      if (x == code[3]) and (y == code[0]):
        trad = x + y
        tradu = abc[16]
      if (x == code[3]) and (y == code[1]):
        trad = x + y
        tradu = abc[17]
      if (x == code[3]) and (y == code[2]):
        trad = x + y
        tradu = abc[18]
      if (x == code[3]) and (y == code[3]):
        trad = x + y
        tradu = abc[19]
      if (x == code[3]) and (y == code[4]):
        trad = x + y
        tradu = abc[20]
      if (x == code[4]) and (y == code[0]):
        trad = x + y
        tradu = abc[21]
      if (x == code[4]) and (y == code[1]):
        trad = x + y
        tradu = abc[22]
      if (x == code[4]) and (y == code[2]):
        trad = x + y
        tradu = abc[23]
      if (x == code[4]) and (y == code[3]):
        trad = x + y
        tradu = abc[24]
      if (x == code[4]) and (y == code[4]):
        trad = x + y
        tradu = abc[25]
      if (x == code[5]) or (y == code[5]):
        print ("\nA codificação em Tap Code traduzida para palavra é: ",texto)
        break
  if menu == 2:
   while True:
    print ("\nDigite uma frase ('Sair' para sair): ")
    frase = str(input())
    if frase == 'Sair':
      break
    elif frase == 'Delete':
      codi = ''
    else:
      for letra in frase:
        lista.append(letra)
        if letra == ' ':
         codu = bra[0] + ' '
        if letra == 'A':
         codu = lista[0] + ' '
        if letra == 'B':
         codu = lista[1] + ' '
        if letra == 'C':
         codu = lista[2] + ' '
        if letra == 'D':
         codu = lista[3] + ' '
        if letra == 'E':
         codu = lista[4] + ' '
        if letra == 'F':
         codu = lista[5] + ' '
        if letra == 'G':
         codu = lista[6] + ' '
        if letra == 'H':
         codu = lista[7] + ' '
        if letra == 'I':
         codu = lista[8] + ' '
        if letra == 'J':
         codu = lista[9] + ' '
        if letra == 'L':
         codu = lista[10] + ' '
        if letra == 'M':
         codu = lista[11] + ' '
        if letra == 'N':
         codu = lista[12] + ' '
        if letra == 'O':
         codu = lista[13] + ' '
        if letra == 'P':
         codu = lista[14] + ' '
        if letra == 'Q':
         codu = lista[15] + ' '
        if letra == 'R':
         codu = lista[16] + ' '
        if letra == 'S':
         codu = lista[17] + ' '
        if letra == 'T':
         codu = lista[18] + ' '
        if letra == 'U':
         codu = lista[19] + ' '
        if letra == 'V':
         codu = lista[20] + ' '
        if letra == 'W':
         codu = lista[21] + ' '
        if letra == 'X':
         codu = lista[22] + ' '
        if letra == 'Y':
         codu = lista[23] + ' '
        if letra == 'Z':
         codu = lista[24] + ' '
        if frase == "print":
         print ("\nA sua frase/palavra traduzida em Tap Code é: ",codi)
         break
        codi = codi + codu + " "

  if menu == 3:
    while True:
     print ("\nQuais instruções?")
     print ("[1] Instruções para 'Traduzir de Tap Code para palavras'", "\n[2] Instruções para 'Traduzir de palavras para Tap Code'", "\n[3] Sair")
     ins = int(input())
     if ins == 1:
      print ("##########################","\n##  Tap Code Translate  ##","\n##########################", "\n### [0][1][2][3][4][5] ###","\n### [1](A)(B)(C)(D)(E) ###", "\n### [2](F)(G)(H)(I)(J) ###", "\n### [3](L)(M)(N)(O)(P) ###","\n### [4](Q)(R)(S)(T)(U) ###","\n### [5](V)(W)(X)(Y)(Z) ###","\n##########################")
      print ("O Tap Code é escrito por você e lido pelo nosso programa da seguinte forma: ", "\n\n(1) Você começa pela horizontal e depois para a vertical. Exemplo: A letra 'G' se encontra em 2 (horizontal) e 2 (vertical) ", "\n(2) Você utiliza pontos espaçados para se comunicar ao invés dos números. Exemplo: A letra 'E' se encontra em: . .....","\n(3) No nosso tradutor, você escreve uma letra por vez. Exemplo: para escrever a palavra 'ANA', você tem que escrever '. .', enter, '... ...', enter, '. .', enter.","\n(4) Usamos a '/ /' para darmos espaços e 'print print' para a palavra ser escrita.")
     if ins == 2:
      print ("A palavra é escrita por você e lida pelo nosso programa da seguinte forma: ", "\n(1) Você escreve a palavra com todas as letras maiúsculas","\n(2) Você digita 'Sair' para sair do tradutor e ir pro menu", "\n(3) Você escreve 'Delete' para deletar a ultima coisa escrita após o print.","\n(4) Você escreve 'print' para traduzir a frase em Tap Code.")
     if ins == 3:
      break
  if menu == 4:
    print ("\nO Tap Code, às vezes chamado de código de batida, é uma forma de codificar mensagens de texto letra por letra de uma forma muito simples. \nA mensagem é transmitida por meio de uma série de sons de toque, daí seu nome.\nO código de escuta tem sido comumente usado por prisioneiros para se comunicarem entre si.\nO método de comunicação geralmente é bater nas barras de metal, nos tubos ou nas paredes dentro de uma cela.\n(Wikipédia)")
  if menu == 5:
    print ("\nObrigada por testar nosso tradutor ^^")
    break
        
        '''
st.code(code, language='python')

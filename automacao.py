import pyautogui
import time

# clicar - pyautogui.click
# escrever - pyautogui.write
# apertar tecla - pyautogui.press
# apertar  - pyautogui.hotkey
# scroll (roplar) - pyautogui.scroll

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

#ENTRAR NO SISTEMA

pyautogui.PAUSE = 1

pyautogui.press('win')

pyautogui.write('chrome')

pyautogui.press('enter')    

pyautogui.write(link) 

pyautogui.press('enter')

time.sleep(2)

# FAZER LOGIN NO SISTEMA

pyautogui.click(x=1096, y=372)

pyautogui.write('Wadson@gmail.com')

pyautogui.press('tab')

pyautogui.write('123456')

pyautogui.click(x=1275, y=538)

time.sleep(1)

# FAZER REGISTRO DE PRODUTOS

pyautogui.press('esc')

import pandas as pd 

produtos = pd.read_csv('produtos.csv')

for linha in produtos.index:

    pyautogui.click(x=1072, y=255)

    codigo = produtos.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = produtos.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = produtos.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')


    categoria = produtos.loc[linha, 'categoria']  
    pyautogui.write(str(categoria))
    pyautogui.press('tab')


    preco_unitario = produtos.loc[linha, 'preco_unitario']  
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')


    custo = produtos.loc[linha, 'custo']  
    pyautogui.write(str(custo))
    pyautogui.press('tab')


    obs = produtos.loc[linha,'obs']
    if not pd.isna(obs):
        pyautogui.write(obs)


    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)




import pyautogui
import time
import pandas as pd 

produtos = pd.read_csv('produtos.csv')

time.sleep(5)

print(pyautogui.position())

print(produtos)
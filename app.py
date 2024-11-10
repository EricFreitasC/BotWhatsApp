import pyautogui
import webbrowser
from time import sleep


# Passando os telefones
# telefones = [XXXXXXXX,XXXXXXXX,XXXXXXXX]

 # Lendo o arquivo de texto com os numeros
 
telefones = []

with open('fones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)
    

for telefone in telefones:
    webbrowser.open(f' https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(1058,252,duration=1)
    pyautogui.click(1777,20,duration=2)
    pyautogui.click(636,990,duration=2)
    sleep(15)
    pyautogui.write('Testando Boot do zap')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)

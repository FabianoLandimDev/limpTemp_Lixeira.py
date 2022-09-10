import pyautogui as ag
import time as t


# Nome_do _programa: limpTemp_Lixeira.py
#
# site: https://github.com/FabianoLandimDev//limpTemp_Lixeira.py/blob/main/Arquivos/main.py
#
# Autor: Fabiano Landim <landimfabiano01@gmail.com>
#
# Manutenção: Fabiano Landim <landimfabiano01@gmail.com>
#
# ESCOPO:
# O Programa automatiza uma limpeza nas pastas temp, %temp% e Lixeira de forma sequencial.
#
# Histórico:
#
# v1.0 2022-09-06, Fabiano Landim:
# - Versão Inicial do Programa.
#
# Licença: MIT.


ag.PAUSE = 2 # 2 segundos para cada ação...
ag.alert('Confirme a execução do programa e não mexa na máquina até o término...')


#Inputando o comando executar no Windowns e procurando pela pasta temp...
ag.hotkey('win', 'r')
ag.write('temp')
ag.press('enter')

#selecionando todo o conteúdo e deletando definitivamente os arquivos...
ag.hotkey('ctrl', 'a')
ag.hotkey('shift', 'del')
ag.press('enter')
ag.press(['right', 'right'])
ag.press('enter')
ag.hotkey('alt', 'F4')

#Inputando o comando executar no Windowns e procurando pela pasta %temp%...
ag.hotkey('win', 'r')
ag.write('%temp%')
ag.press('enter')

#selecionando todo o conteúdo e deletando definitivamente os arquivos...
ag.hotkey('ctrl', 'a')
ag.hotkey('shift', 'del')
ag.press('enter')
ag.press(['right', 'right'])
ag.press('enter')
ag.hotkey('alt', 'F4')

#Localizando a pasta referemte à Lixeira...
ag.hotkey('win')
ag.write('Lixeira')
ag.press('backspace')
ag.press('enter')
t.sleep(2)

#selecionando todo o conteúdo e deletando definitivamente os arquivos...
ag.hotkey('ctrl', 'a')
ag.hotkey('shift', 'del')
ag.press('enter')
ag.hotkey('alt', 'F4')

#Fechando o Programa...
ag.alert('Programa executado com SUCESSO!!!')
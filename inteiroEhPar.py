from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkRed1')
layout = [
    [sg.Text('Insira o número'), sg.Input(key='numero',size=(20,1))],
    [sg.Button('verificar')],
    [],
    [sg.Text('Resultado'), sg.Output(key='ehpar')]
]

janela = sg.Window('inteiroEhPar', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'verificar': 
        num = int(valores['numero'])
        resto = num % 2

        if resto == 0:
            print('O Número é par')
        else:
            print('O Número é impar')    

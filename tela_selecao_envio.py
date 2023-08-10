import PySimpleGUI as sg

layout = [
    [sg.Text('Selecionar Avatar')],
    [sg.InputText()],
    [sg.Checkbox('Avatar 1')],
    [sg.Checkbox('Avatar 2')],
    [sg.Drop("Grupo 1, Grupo 2")],
    [sg.Button('Disparar')],
]

janela = sg.Window("Selecionar Avatar", layout)

while True:
    evento, valores = janela.read()
    if evento != sg.WIN_CLOSED:
        pass
    else:
        break
janela.close()

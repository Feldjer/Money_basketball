from money_basketball import money_basketball
from launch_parsing_games import pars_games

import PySimpleGUI as sg
import threading
import os

# Global interface with cryptographic protection

def startProgramm():
    moneyBasketball(game, bet, crypto_file, crypto_key)

programm = threading.Timer(0.0, startProgramm)

file_types_crypto_data = [("Cryptodata (*.crypto)", "*.crypto"), ("All files (*.*)", "*.*")]
file_types_crypto_key = [("Cryptokey (*.key)", "*.key"), ("All files (*.*)", "*.*")]

crypto_file = ''
crypto_key = ''
game = ''
bet = 0
games = pars_games()

sg.ChangeLookAndFeel('BrownBlue')

layout = [
    [sg.Text('Выбор игры'), sg.InputCombo((games), size=(70,1), key='-INPUT-'), sg.Text('Сумма ставки '),
     sg.InputCombo(('20₽', '30₽', '40₽', '50₽'), default_value="20₽", key='-BET-', size=(3, 4), tooltip=('Подсказка')), sg.Button('Применить')],
    [sg.T('               '), sg.Text('Криптофайл', size=(9, 1)), sg.InputText('Файл с данными авторизации', key="-CRYPTOFILE-"),
     sg.FileBrowse(button_text = 'Выбрать', file_types=file_types_crypto_data), sg.Button('Загрузить криптофайл')],
    [sg.T('               '), sg.Text('Криптоключ', size=(9, 1)), sg.InputText('Файл с криптоключом', key="-CRYPTOKEY-"),
     sg.FileBrowse(button_text = 'Выбрать', file_types=file_types_crypto_key), sg.Button('Загрузить криптоключ')],
    [sg.T('                                                                                '),
     sg.Button("Старт", button_color=("white", "green"), size=(8, 2)),
    sg.Button("Выход", button_color=("white", "red"), size=(8, 2)),
    sg.Button("Тест", button_color=("white", "DeepSkyBlue4"), size=(8, 2))],
    [sg.Output(size=(110, 20))]
]

window = sg.Window('MoneyBasketball', layout)
while True:
    event, values = window.read()
    if event is None or event == 'Выход':
        break
    if event == 'Применить':
        game = values['-INPUT-']
        bet = values['-BET-']
        if game != '':
            if bet != '':                
                sg.popup('Игра: ' + game + '\n' + 'Сумма ставки на игру: ' + bet)
                game = game.split('—')[0][::-1][1:][::-1]
                bet = int(bet[0:2])
            else:
                sg.popup('Не введена сумма ставки!')
        else:
            sg.popup('Не введена игра!')
    if event == 'Старт':
        if game != '':
            if bet != '':
                if crypto_file != '' and '/' in crypto_file:
                    if crypto_key != '' and '/' in crypto_key:
                        if programm.start() == 'restart':
                            print("Проверьте введенные данные и запутите программу заново!")
                    else:
                        sg.popup('Не выбран криптоключ!')
                else:
                    sg.popup('Не выбран криптофайл!')
            else:
                sg.popup('Не введена сумма ставки!')
        else:
            sg.popup('Не введена игра!')
    elif event == 'Загрузить криптофайл':
        crypto_file = values["-CRYPTOFILE-"]
    elif event == 'Загрузить криптоключ':
        crypto_key = values["-CRYPTOKEY-"]

window.close()

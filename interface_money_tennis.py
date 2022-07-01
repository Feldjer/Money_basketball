from launch_dynamic_link_search import dynamic_link_search
from launch_parsing_live import definition_live
from money_basketball import money_basketball
from launch_analysis_bet import issuing_bet
from launch_parsing_games import pars_games
import PySimpleGUI as sg

import urllib.request
import requests
import random
import psutil
import time

# Global Interface

game = ''
bet = 0
games = pars_games()

sg.ChangeLookAndFeel('BrownBlue')

layout = [
    [sg.Text('MONEY BASKETBALL', size=(92,1), font='ComicSansMS', justification = 'center')], [sg.HorizontalSeparator(color = 'black')],
    [sg.Text('Выбор игры'), sg.InputCombo((games), size=(70,1), key='-INPUT-'), sg.Text('Сумма ставки '),
     sg.InputCombo(('20₽', '30₽', '40₽', '50₽'), default_value="20₽", key='-BET-', size=(3, 4)), sg.Button('Применить')],
    [sg.Text('—'*25), sg.Button("Старт", button_color=("white", "green"), size=(8, 2)), sg.Button("Выход", button_color=("white", "red"), size=(8, 2)),
     sg.Text('—'*25)], [sg.Output(size=(115, 20))]
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
                time = game[game.find('Время')+7:]
                game = game[:game.find('Время')-2]
                fourth = game[game.find('Четверть')+10:]
                game = game[:game.find('Четверть')-2]
                sg.popup('Игра: ' + game + '\nЧетверть: ' + fourth + '\nВремя: ' + time + '\nСумма ставки на игру: ' + bet)
                game = game.split('—')[0][::-1][1:][::-1]
                bet = int(bet[0:2])
            else:
                sg.popup('Не введена сумма ставки!')
        else:
            sg.popup('Не введена игра!')
    if event == 'Старт':
        if game != '':
            if bet != '':
                print('Запуск программы!')
                money_basketball(game, bet)
            else:
                sg.popup('Не введена сумма ставки!')
        else:
            sg.popup('Не введена игра!')

window.close()

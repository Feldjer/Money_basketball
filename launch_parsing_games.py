from bs4 import BeautifulSoup

import requests

# Parsing games for output to the interface

def pars_games():
    
    def name_search(info, indexSearch):
        indexSearch = info.find('<span class="n" title=', indexSearch)
        infoNew = info[indexSearch+23:]

        indexSearch = infoNew.find('">')
        infoNew_n = infoNew[:indexSearch]

        infoNew_n = infoNew_n.replace(' с ОТ ', '')
        infoNew_n = infoNew_n[::-1][1:][::-1]

        infoTime = infoNew[infoNew.find('<div class="c-events__time">')+35:]
        if 'class="c-events__overtime">' in infoTime[0:35]:
            infoTime = "Неизвестно"
        else:
            infoTime = infoTime[:infoTime.find('</span>')]
        return infoNew, infoNew_n, infoTime, indexSearch

    def definition_of_fourth(time):

        if time == 'Неизвестно':
            fourth = 'Неизвестно'
            return fourth
        
        time = int(time[0:2])
        if time <= 10:
            fourth = '1'
        elif (time > 10) and (time <= 20):
            fourth = '2'
        elif (time > 20) and (time <= 30):
            fourth = '3'
        elif (time > 30) and (time <= 40):
            fourth = '4'
        else:
            fourth = 'Овертайм'
        return fourth

    url = 'https://1xstavka.ru/live/Basketball/'
    r = requests.get(url)
    with open('test.txt', 'w', encoding='utf-8') as output_file:
      output_file.write(r.text)

    mas = []
    info = ''
    soup = BeautifulSoup(open('test.txt', encoding='utf-8'), 'html.parser')
    for i in soup.find_all("div", class_='c-events-scoreboard__item'):
        info += str(i)


    index = 0
    while True:
        info, indexer, time, index = name_search(info, index)
        if index == -1:
            break
        else:
            if '<' in indexer or '_' in indexer or len(indexer) < 10 or not '—' in indexer or 'Статистика игроко' in indexer:
                pass
            elif 'мест' in indexer:
                indexer = indexer.replace('мест', 'место')
            else:
                if not 'class="c-events__overtime">' in time:
                    mas.append(indexer + ' | Четверть: ' + definition_of_fourth(time) + ' | Время: ' + time)
    return mas

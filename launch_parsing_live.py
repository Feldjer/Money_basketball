from bs4 import BeautifulSoup

import urllib.request

# Determination of time and quarter

def invoice_processing(score):
    total = ''
    number = 0
    for i in range(0, len(score)):
        if score[i] == '1' or score[i] == '2' or score[i] == '3' or score[i] == '4' or score[i] == '5' or score[i] == '6' or score[i] == '7' or score[i] == '8' or score[i] == '9' or score[i] == '0':
            number += 1
            if number == 2:
                total += score[i-1:i+1]
                number = 0
        else:
            if number == 1:
                total += '*' + score[i-1]
                number = 0

    total = total.replace('*', ' ')
    return total

def definition_live():
    flagDuplicate, minute_12, live = False, False, False
    flagFourth, totalAll, name = True, True, True
    liveFourth, liveTime = '', ''
    information, score = '', ''
    total = ''
    
    soup = BeautifulSoup(open('html_code_live_1x.txt', encoding='utf-8'), 'html.parser')
    for i in soup.find_all("a", class_='c-tablo__text'):
        if ("-я Четверть" in i.text):
            information += str(i.text)
            name = False
        elif not name:
            information += str(i.text)
    information = information.replace('\n', '')
            
    if 'Перерыв' in information:
        flagDuplicate = True
        
    for i in range(0, len(information)):
        if information[i] == '1' or information[i] == '2' or information[i] == '3' or information[i] == '4' or information[i] == '5' or information[i] == '6' or information[i] == '7' or information[i] == '8' or information[i] == '9' or information[i] == '0':
            if flagFourth:
                liveFourth += information[i]
                flagFourth = False
            else:
                liveTime += information[i]
            if flagDuplicate:
                liveTime += information[i]
                flagDuplicate = False

    f = open('additionally.txt', 'r')
    minute = f.read()
    f.close()

    if minute == '+':
        minute_12 = True

    if minute_12:
        if liveFourth == '4':
                if int(liveTime) > 3600:
                    print('Конец парсинга!')
                    total = '########'
                    return live, total
        if ((liveFourth == '1') and (liveTime == '1200')) or ((liveFourth == '2') and (liveTime == '1200')) or ((liveFourth == '2') and (liveTime == '2400')) or ((liveFourth == '3') and (liveTime == '2400')) or ((liveFourth == '3') and (liveTime == '3600')) or ((liveFourth == '4') and (liveTime == '3600')):
            
            live = True

            for i in soup.find_all(class_='c-tablo-count'):
                if totalAll == True:
                    totalAll = False
                else:
                    score += str(i.text)
            score = score.replace('\n', '')
            total = invoice_processing(score)
        
    else:
        if liveFourth == '4':
                if int(liveTime) > 3000:
                    print('Конец парсинга!')
                    total = '########'
                    return live, total
                    
        if ((liveFourth == '1') and (liveTime == '1000')) or ((liveFourth == '2') and (liveTime == '1000')) or ((liveFourth == '2') and (liveTime == '2000')) or ((liveFourth == '3') and (liveTime == '2000')) or ((liveFourth == '3') and (liveTime == '3000')) or ((liveFourth == '4') and (liveTime == '3000')):

            live = True

            for i in soup.find_all(class_='c-tablo-count'):
                if totalAll == True:
                    totalAll = False
                else:
                    score += str(i.text)
            score = score.replace('\n', '')
            total = invoice_processing(score)

    if minute_12:
        print('Идет: ' + liveFourth + '-я четверть')
        print('Время: ' + liveTime[0:2] + ':' + liveTime[2:4])
        print('Четверть длится: 12 минут')
        if total != '':
            print('Счет: ' + total)
    else:
        print('Идет: ' + liveFourth + '-я четверть')
        print('Время: ' + liveTime[0:2] + ':' + liveTime[2:4])
        print('Четверть длится: 10 минут')
        if total != '':
            print('Счет: ' + total)
            
    return live, total

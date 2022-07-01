from launch_dynamic_link_search import dynamic_link_search
from launch_parsing_live import definition_live
from launch_analysis_bet import issuing_bet
from selenium import webdriver
from bs4 import BeautifulSoup

import urllib.request
import requests
import random
import psutil
import time

# The main program

def money_basketball(game, betSum):

    phone = ''      # Information is hidden for privacy purposes
    password = ''   # Information is hidden for privacy purposes
    
    fourthAdditionalLine = '-я Четверть'
    fourthNumber = 0
    liveLast = None

    deliveredBet = ''
    lastFourth = ''

    global_prog = 'True'

    driver = webdriver.Firefox()                                                            # Starting the process
    driver.get('https://1xstavka.ru/live/Basketball/')
    time.sleep(4)

    try:
        driver.find_element_by_xpath('//*[@id="loginout"]/div/div/div/div[1]').click()      # Authorization
    except Exception:
        driver.find_element_by_xpath('//*[@id="loginout"]/div/div/div/div[1]').click()      # Authorization
        while Exception:
            driver.find_element_by_xpath('//*[@id="loginout"]/div/div/div/div[1]').click()  # Authorization
    time.sleep(random.uniform(4,5))
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div/div[2]/div/form/div[1]/div/button').click() # Change to phone
    time.sleep(random.uniform(4,5))
    time.sleep(random.uniform(0,1))

    page_source = driver.page_source                                                        # Saving an html page
    f = open('html_code_dinamical_number.txt', mode='w', encoding='utf8')
    f.write(page_source)
    f.close()

    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/div[2]').click()
    time.sleep(4)
    driver.find_element_by_xpath(dynamic_link_search()).send_keys(phone)                    # Entering a phone number
    driver.find_element_by_xpath('//*[@id="auth-form-password"]').send_keys(password)       # Entering a password
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="loginout"]/div/div/div/div[2]/div/form/button').click() # Authorized
    time.sleep(20)
    try:
        driver.find_element_by_partial_link_text(game).click()                              # Game search
    except Exception:
        print("Игра не найдена!")
        time.sleep(1)
        for proc in psutil.process_iter():                                                  # Closing the process 
            if proc.name() == 'firefox.exe': 
                proc.kill()
    time.sleep(10)
    page_source = driver.page_source                                                        # Saving an html page
    f = open('html_code_live_1x.txt', mode='w', encoding='utf8')
    f.write(page_source)
    f.close()

    while global_prog == 'True':

        page_source = driver.page_source                                                    # Saving an html page
        f = open('html_code_live_1x.txt', mode='w', encoding='utf8')
        f.write(page_source)
        f.close()

        live, total = definition_live()
        print("live:", live)
        if total != '':
            print("total:", total)
        elif total == '######' and not live:
            global_prog = 'False'
            f = open('global_prog.txt', 'w')
            f.write('False')
            f.close()
            print('4-я четверть! Парсинг закончен!')
            f = open('additionally.txt', 'w')
            f.write('')
            f.close()
            driver.close()
            time.sleep(1)
            exit()
        time.sleep(0.5)
            
        if live:

            live = False
            
            if total != '':
                if total[-4:] == " 0 0":
                    total = total[:-4]
                    if len(total) % 4 == 0:
                        fourthNumber = (len(total) // 4) + 1
                        fourthString = str(fourthNumber) + fourthAdditionalLine
                    else:
                        print('Счет маленький!/Некорректный счет!')
                        break
            else:
                print('Счет не получен!')
                break

            f = open('flag_bet.txt', 'r')
            lastFourth = f.read()
            f.close()

            if lastFourth == fourthNumber:
                pass
            else:            
                driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div/div/div[3]/div/div/div/div[1]/div[3]/div/div[1]/div[1]/div/div[2]/span').click() # выбираем основу
                time.sleep(1)
                countOfLink = 0
                while countOfLink < 4:
                    print('Ссылка на:', driver.find_elements_by_class_name('multiselect__element')[i].text)
                    print('Ищем:', fourthString)
                    if driver.find_elements_by_class_name('multiselect__element')[i].text == fourthString:
                        bet_type = driver.find_elements_by_class_name('multiselect__element')[i].click()
                        print('Найдено!')
                        break
                    countOfLink += 1
                time.sleep(2)

                bet = issuing_bet(total)
                if bet == 'Матч закончен!':
                    global_prog == 'False'
                    break
                elif bet == 'Некорректный счет!':
                    pass
                else:
                    i = 3
                    ch = 0
                    flag_bet = False
                    acceptedBet = False
                    minGrapBet = False
                    min = driver.find_elements_by_class_name('bet_type')[3].text
                    if min[0:2] == 'Не':
                        time.sleep(1)
                        exit()
                    else:
                        min_ = min[0:2]
                        min = int(min[0:2])
                        if (min - int(bet[0:2])) <= 4:
                            flag_bet = True
                        while True:
                            print(driver.find_elements_by_class_name('bet_type')[i].text)
                            if driver.find_elements_by_class_name('bet_type')[i].text == bet:
                                ch = i
                                bet_type = driver.find_elements_by_class_name('bet_type')[i].click()
                                deliveredBet = driver.find_elements_by_class_name('bet_type')[i].text
                                acceptedBet = True
                                break
                            elif (('-' in driver.find_elements_by_class_name('bet_type')[i].text) == True):
                                if flag_bet == True:
                                    bet_type = driver.find_elements_by_class_name('bet_type')[3].click()
                                    deliveredBet = driver.find_elements_by_class_name('bet_type')[3].text
                                    minGrapBet = True
                                    break
                                else:
                                    print('Разрыв сильно большой от выданной и возможной ставки! Ставка не поставлена!')
                                    f = open('flag_bet.txt', 'w')
                                    f.write(str(fourthNumber))
                                    f.close()
                                    time.sleep(1)
                                    exit()
                            i += 1

                        try:
                            driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div/input').send_keys(BET_SUM)
                        except Exception:
                            if acceptedBet:
                                try:
                                    bet_type = driver.find_elements_by_class_name('bet_type')[i].click()
                                    deliveredBet = driver.find_elements_by_class_name('bet_type')[i].text
                                except Exception:
                                    while Exception:
                                        bet_type = driver.find_elements_by_class_name('bet_type')[i].click()
                                        deliveredBet = driver.find_elements_by_class_name('bet_type')[i].text
                                driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div/input').send_keys(BET_SUM)
                            elif minGrapBet:
                                try:
                                    bet_type = driver.find_elements_by_class_name('bet_type')[3].click()
                                    deliveredBet = driver.find_elements_by_class_name('bet_type')[3].text
                                except Exception:
                                    while Exception:
                                        bet_type = driver.find_elements_by_class_name('bet_type')[3].click()
                                        deliveredBet = driver.find_elements_by_class_name('bet_type')[3].text
                                driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div/input').send_keys(BET_SUM)

                        if acceptedBet:
                            print('Поставлена ставка:', deliveredBet)
                        elif minGrapBet:
                            print('Поставлена минимальная ставка с позволительным разрывом:', deliveredBet)

                        f = open('flag_bet.txt', 'w')
                        f.write(str(fourthNumber))
                        f.close()

        return None

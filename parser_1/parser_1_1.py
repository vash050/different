# import json
import dataset
import sqlite3
import time

import requests
from bs4 import BeautifulSoup

db = dataset.connect('sqlite:///name_birds.sqlite3')
table = db['names']


def get_next_page(page):
    try:
        next_page = page.find("li", class_="next")
        print(next_page)
        return str(next_page.a['href'])
    except Exception as err:
        print(err)
        return None


def date_optim(list_clear_date):
    """функция оптимизирует данные"""
    tmp = []
    try:
        count_letter_in_name = list_clear_date.index('лат.')
        tmp.extend([" ".join(list_clear_date[:count_letter_in_name])])
        if 'анг.' in list_clear_date:
            count_letter_in_name_lat = list_clear_date.index('анг.')
            tmp.extend([" ".join(list_clear_date[count_letter_in_name:count_letter_in_name_lat])])
            tmp.extend([" ".join(list_clear_date[count_letter_in_name_lat:])])
        else:
            tmp.extend([" ".join(list_clear_date[count_letter_in_name:])])
        return tmp
    except Exception as e:
        print(e)


flag = True
adress = '/opredelitel-ptic'

while flag:
    adress_page = f'http://onbird.ru{adress}'
    print(adress_page)
    r = requests.get(adress_page)
    print(r.status_code)

    soup = BeautifulSoup(r.text, features="html.parser")
    groups = soup.find_all("div", class_="pull-left second")

    date_list = None
    resalt_data_dict = {'name': None, 'lat_name': None, 'eng_name': None}
    for group in groups:
        try:
            a = ' '.join(group.get_text().split()).split()
            date_list = [elem for elem in a if
                         (elem not in ('Фото', '|', 'Голос', '|', 'Видео', '-', 'см', 'размах', 'крыльев')
                          and len(elem) > 3
                          and not elem[0].isdigit()
                          and elem[0] != '(')]
            resalt = date_optim(date_list)
            # print(resalt)
            resalt_data_dict['name'] = resalt[0]
            resalt_data_dict['lat_name'] = resalt[1][5:]
            resalt_data_dict['eng_name'] = ''
            if len(resalt) == 3:
                resalt_data_dict['eng_name'] = resalt[2][5:]
            table.insert(resalt_data_dict)

        except Exception as e:
            print(e)
            continue

    adress = get_next_page(soup)
    print(adress)
    if adress is None:
        flag = False
        print(flag)
    # time.sleep(1)
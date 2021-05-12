from functools import reduce

import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url)
        print(r.status_code)
        return r.text
    except Exception as e:
        print(e)


def get_data(html):
    soup = BeautifulSoup(html, features="html.parser")
    ul = soup.find('ul').text
    return ul


def get_res(row_data):
    return_list = []
    tmp = []
    list_rez = row_data.split('\n')
    for idx, el in enumerate(list_rez[:]):
        el = el.replace(',', '')
        if el != '':
            if el[0:3] == 'Тип':
                if idx != 1:
                    if not tmp:
                        continue
                    return_list.append(tmp)
                    return_list.append('\n')
                    tmp = []
            tmp.append(el.strip())

    return return_list


def main():
    url_site = 'http://ecosystema.ru/08nature/w-invert/'
    a = get_res(get_data(get_html(url_site)))

    a = map(lambda x: ','.join(x), a)
    a = list(map(str, a))

    with open('file_2.csv', 'w', encoding='utf8') as f:
        f.writelines(a)


if __name__ == '__main__':
    main()

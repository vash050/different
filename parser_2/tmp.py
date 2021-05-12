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
    list_url = []
    soup = BeautifulSoup(html, features="lxml")
    links = soup.find('div', class_="brand-images").find_all('a')
    for link in links:
        list_url.append(link.get("href")[11:])
        return list_url


def get_url_page_elem_catalog(html_page_catalog):
    """функция получает адрес страницы каталога"""
    list_url = []
    soup = BeautifulSoup(html_page_catalog, features="lxml")
    for div in soup.find_all("div", class_="catalog-item with-long-title"):
        list_url.append(div.find("a").get("href")[11:])
        return list_url


def get_url_page_catalog_list(url_page):
    """принимает список страниц,
     вызывает функцию get_html(url) и функцию get_data_page(html) для каждой странице
     возвращяет словарь, где ключ url страницы с каталога, а значение список url товаров
    """
    url_all_dist = {}
    b = url_page[0]
    url_all_dist.setdefault(str(b), [])
    url_page_tmp = f'https://www.oboilux.ru/wallpapers{b}'
    a = get_url_page_elem_catalog(get_html(url_page_tmp))
    url_all_dist[b].extend(a)
    return url_all_dist


def get_data_good_from_page(html_page_good):
    """принимает html страницы и парсит данные товара"""
    soup = BeautifulSoup(html_page_good, features="lxml")
    link_to_photo = soup.find("div", class_="big-image-image-wrapper").find('img').get('src')
    country = soup.find("div", class_="col-right-right ci-description").find("div", class_="three-head").text
    brand = soup.find("div", class_="col-right-right ci-description").find("p").find("a").text
    collection = soup.find("div", class_="col-right-right ci-description").find("p").find_all("a")[1].text
    article = soup.find("div", class_="col-right-right ci-description").find("p").find("span").text
    price = soup.find("div", class_="col-right-right ci-description").find("div", class_="ci-price").find("span").text
    view = soup.find("div", class_="ci-type-wallpaper").find("span", class_="pic-inroll pic-img-type").text
    fastness_to_light = soup.find("div", class_="ci-type-wallpaper").find("span",class_="pic-inroll pic-img-light").text
    resistance_to_friction = soup.find("div", class_="ci-type-wallpaper").find("span",class_="pic-inroll pic-img-wash").text
    width = soup.find("div", class_="ci-type-wallpaper").find("span",class_="pic-inroll pic-img-width").text
    repeat_drawing = soup.find("div", class_="ci-type-wallpaper").find("span",class_="pic-inroll pic-img-repeat").text
    length = soup.find("div", class_="ci-type-wallpaper").find("span",class_="pic-inroll pic-img-length").text
    description = soup.find("div", class_="small-12 medium-12 large-12 column").text



def get_data_goods(dist_url_page_all):
    """получает словарь со всеми адресами страниц каталога
       вызывает функцию get_html(url) и функцию get_data_goods_from_page(html) для каждой странице,
       и вызывает функцию записи в бд
    """

    for el in dist_url_page_all['/17patterns']:
        link = f'https://www.oboilux.ru/wallpapers{el}'
        data_good = get_data_good_from_page(get_html(link))




def main():
    url_site_pige_start = 'https://www.oboilux.ru/wallpapers'
    url_next_page_lists = get_data(get_html(url_site_pige_start))
    print(url_next_page_lists)
    url_page_catalog = get_url_page_catalog_list(url_next_page_lists)
    print(url_page_catalog)
    get_data_goods(url_page_catalog)
main()

# find("div", class_="col-right").find("div", class_="special-row")

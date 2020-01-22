#! python3
"""Pobiera stronę xkcd.com i ściąga z niej obrazki. Po ściągnięciu, cofa się o jedną stronę, by pobrać kolejny obraz"""

import requests
import bs4
import os

url = 'http://xkcd.com'
folder = r'D:\Py\099_XKCD_Comics_Download\XKCD'
os.makedirs(folder, exist_ok=True)
counter = 0
while not (url.endswith('#')) and (counter < 5):
    print(f'pobieranie strony {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # Ustalenie adresu URL pliku obrazu komiksu
    comicElem = soup.select('#comic img')
    if not comicElem:
        print(f'Nie udało sie pobrać pliku obrazu komiksu.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Pobranie obrazu
        print(f'Pobieranie obrazu {comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Zapis obrazu w katalogu
        imgFile = open(os.path.join(folder, os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()
    counter += 1

    # Pobranie adresu URL w przycisku PREV
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Gotowe')

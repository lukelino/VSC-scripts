#! python3
""" Przykład użycia BeautifulSoup """

import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.coreyms.com'

csv_file = open(r'F:\VSCPython\cms_scrape.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

status = True
while status:
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    for article in soup.find_all('article'):
        headline = article.h2.a.text
        print(headline)
        summary = article.find('div', class_='entry-content').p.text
        try:
            vid_src = article.find('iframe', class_='youtube-player')['src']
            vid_id = vid_src.split('/')
            vid_id = vid_id[4].split('?')
            vid_id = vid_id[0]
            youtube_links = f'https://www.youtube.com/watch?v={vid_id}'
        except Exception as exce:
            youtube_links = None
            print(f'brak linku youtube')
        #print(f'pobieranie strony {url}')
        csv_writer.writerow([headline, summary, youtube_links])
    print()
    try:
        prevLink = soup.find('li', class_='pagination-next').a['href']
        url = prevLink
    except AttributeError as identifier:
        print('Koniec')
        status = False
    
    print(url)
    print()
csv_file.close()

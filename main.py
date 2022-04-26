import os
import requests
from bs4 import BeautifulSoup
from pathlib import Path


url = 'https://www.irmaosgoncalves.com.br/ofertas/'
citys = [
    'jaru',
    'porto-velho',
    'ariquemes',
    'cacoal',
    'ji-parana',
    'rolim-de-moura',
    'vilhena',
    'guajara-mirim',
    'ouro-preto',
    'pimenta-bueno',
]


for city in citys:
    city = '?cidade=' + city

    page = requests.get(os.path.join(url, city))
    soup = BeautifulSoup(page.text, 'html.parser')

    Path('IMAGES/' + city.split('=')[1]).mkdir(parents=True, exist_ok=True)


    for img in soup.find_all('img',
            class_ = 'img-responsive img-fluid d-inline'
            ):

        img['src'] = img['src'].replace('./', '')
        name_img = img['src'].split('/')[-1]

        folder = os.path.join('IMAGES', city.split('=')[1], name_img)

        with open(folder, 'wb') as f:
            page = requests.get(os.path.join(url, img['src']), stream=True)
            for chunck in page.iter_content(1024):
                f.write(chunck)

import requests
from bs4 import BeautifulSoup

url = 'https://www.bithumb.com/'
request = requests.get(url).text
soup = BeautifulSoup(request, 'html.parser')
coins = soup.select('.coin_list tr')  # class 가 coin_list 인 것에서 tr 태그들

with open('bithumb.csv', 'w', encoding='utf-8') as f:
    for coin in coins:
        # td:nth-child(1) p a strong: td 태그 중 첫번째에서 p태그, a태그, strong 태그 찾기
        name = coin.select_one('td:nth-child(1) p a strong').text.strip()
        price = coin.select_one('td:nth-child(2) strong').text.replace(',', '')
        f.write(f'{name},{price}\n')

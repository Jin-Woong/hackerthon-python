# naver 에서  html 파일을 가지고 온다.
# BeautifulSoup 를 이용하여 parsing 한다.
# 실시간 검색어 10위까지 출력한다.

import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'
request = requests.get(url).text
# print(type(request))
soup = BeautifulSoup(request, 'html.parser')

# result = soup.find_all('ul', {'data-list':'1to10'})
result = soup.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
index = 0
for test in result.find_all('span', {'class': 'ah_k'}):
    index = index + 1
    print(f'{index}. {test.get_text()}')




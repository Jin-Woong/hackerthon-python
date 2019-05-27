# naver 에서  html 파일을 가지고 온다.
# BeautifulSoup 를 이용하여 parsing 한다.
# 실시간 검색어 10위까지 출력한다.

import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'
request = requests.get(url).text
soup = BeautifulSoup(request, 'html.parser')

# div 태그 중 class 이름이 ah_roll_area PM_CL_realtimeKeyword_rolling 인것을 찾아라 (최초 1개만 찾음)
results = soup.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})


index = 0
# 위에서 찾은 results 내에 span 태그 중 class 이름이 ah_k 인 것 모두
for result in results.find_all('span', {'class': 'ah_k'}):
    index = index + 1
    print(f'{index}. {result.text }')

# css select id는 #id, class 는 .class 로 선택  , span.ah_k => span 태그의 ah_k 이라는 class
# class 이름 사이에 띄어쓰기 되있는 것은 .으로 바꿔주어 해당 class 에 속한다고 표현해준다.
results = soup.select('.ah_roll_area.PM_CL_realtimeKeyword_rolling span.ah_k')

index = 0
for result in results:
    index = index + 1
    print(index, result.text)


import requests  # 웹사이트에 요청하는 내용이 들어있는 라이브러리
from bs4 import BeautifulSoup  # 응답받은 내용들을 parsing하기 위한 라이브러리

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=QaGapZXPV5DTM72fy6lrf3hJnrJxhila1UVkPlUCo0N0g0F0RZ9WEngT8RkNjNo4IF%2BikV%2BthQLze39nK4IQjA%3D%3D&numOfRows=10&pageSize=10&pageNo=3&startPage=3&sidoName=%EC%84%9C%EC%9A%B8&ver=1.6'
request = requests.get(url).text
# print(type(request))
soup = BeautifulSoup(request, 'xml')
# print(type(soup))
gangnam = soup('item')[7]
location = gangnam.stationName.text
time = gangnam.dataTime.text
dust = int(gangnam.pm10Value.text)

# dust 변수에 들어 있는 내용을 출력해보세요.
# print('{0} 기준 {1}의 미세먼지 농도는 {2}입니다.'.format(time,location,dust))
print(f'{time} 기준 {location}의 미세먼지 농도는 {dust}입니다.')

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해부세요.
if 150 < dust:
    print('매우나쁨')
elif 80 < dust <= 150:
    print('나쁨')
elif 30 < dust <= 80:
    print('보통')
else:
    print('좋음')

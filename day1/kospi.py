#0. requests 패키지를 불러온다 // pip install requests
# pip install bs4 : 문서를 찾기 편하게 바꿔주는 패키지(파싱)
import requests
from bs4 import BeautifulSoup
#1. url로 요청(requsts.get)을 보내고, response에 저장한다.
url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
#2. 파이썬이 찾기 편한 형식으로 문서를 변경한다.
soup =BeautifulSoup(response,'html.parser')
print(soup)
print(type(response))
print(type(soup))
#3. KOSPI 값을 찾는다. KOSPI_now
kospi = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(kospi)

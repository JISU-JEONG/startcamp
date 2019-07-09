from bs4 import BeautifulSoup
import requests

url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
response = requests.get(url).text


soup = BeautifulSoup(response, 'html.parser')

exchange = soup.select('body > div > table > tbody > tr')
for tr in exchange:
    print((tr.select('td.tit')[0].text).strip(),':',tr.select_one('td.sale').text)

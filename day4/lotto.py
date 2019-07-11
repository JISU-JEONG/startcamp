import random
import requests
import pprint
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=864'
# 1. 요청
# json ->
# 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
# 응답 (HTML, XML, JSON)
response = requests.get(url).json()
pprint.pprint(response)
print(type(response))


drwtNo=[]
win = [0,0,0,0,0,0]
for i in range(1,7):
    drwtNo.append(response['drwtNo{}'.format(i)])

print('당첨 번호는 {} {} {} {} {} {} bonus {} 입니다.'.format(*drwtNo,response['bnusNo']))
for j in range(10000000):
    my_lotto = random.sample(range(1,46),6)
   # my_lotto.sort()

#print('나의 로또 번호는 {} {} {} {} {} {}'.format(*my_lotto))
    count = 0
    # for num in my_lotto:
    #     if num in drwtNo:
    #         count += 1

    count = len(set(my_lotto) & set(drwtNo))

    if count == 6:
       # print('대박 1등 입니다!!!!')
        win[0] += 1
    elif count == 5 and response['bnusNo'] in my_lotto:
      #  print('축하드립니다. 2등 입니다.')
        win[1] += 1
    elif count == 5:
      #  print('축하드립니다. 3등 입니다.')
        win[2] += 1
    elif count == 4:
       # print('4등 5만원 입니다.')
        win[3] += 1
    elif count == 3:
      #  print('5등 입니다.')
        win[4] += 1
    else:
       # print('꽝')
        win[5] += 1
    print(win, end = '\r')

print('끝')
print(win)
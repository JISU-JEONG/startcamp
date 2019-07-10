'''
# 1.solution
string = input('문자를 입력하세요: ')
print('{} {}'.format(string[0],string[-1])) # -1 인덱스 접근은 가장 마지막 이다.
#str형은 string[0] = b 와 같은 할당을 할수 없다.
'''

'''
# 2.solution
num = int(input())

for i in range(num):
    print(i+1)
'''

'''
# 3.solution
num = int(input())

if num % 2:
    print('홀수 입니다.')
else:
    print('짝수 입니다.')
'''

'''
# 4.solution
a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

if a >= 90 and b > 80 and c >85 and d >=80:
    print('True')
else:
    print('False')
'''

'''
prices = input('물품 가격을 입력하세요: ').split(';')

# 1. 반복문
int_price = []
for ch in 

# 2. list comprehension
int_price2 = [int(price) for price in prices]

# 3. map : 첫번째 인자의 함수를 두번째 인자를 반복하며 적용.
# 반복 가능한 객체에 함수를 각각 적용.
prices = list(map(int,prices))
prices.sort(reverse = True)

for ch in prices:
    print(ch)
'''
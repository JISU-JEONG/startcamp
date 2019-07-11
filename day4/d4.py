"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
sum_n = 0
count_n = 0
for key, value in score.items():
    sum_n += value
    count_n += 1
# sum = sum(score.values()) 더 효육적인 방법
# count_n = len(score) 더 효율적인 방법
print(sum_n/count_n)



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

sum_n = 0
count_n = 0
for score in scores.values():
    for point in score.values():
        sum_n += point
        count_n += 1

print(sum_n/count_n)


# 3. 도시별 최근 3일의 온도입니다.
citys = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')

for city in citys:
    sum_n = 0
    count_t = 0
    for value in citys[city]:
        sum_n += value
        count_t += 1
    print('{} : {:.2f}'.format(city, sum_n/count_t))

for name, temp in citys.items():
    avg = sum(temp) / len(temp)
    print(f'{name} : {avg:.2f}')


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
temp_list=[]

for city in citys:
    for value in citys[city]:
        temp_list.append(value)

for city in citys:
    if max(temp_list) in citys[city]:
        print('가장 더웠던 곳은 : {}'.format(city))
    if min(temp_list) in citys[city]:
        print('가장 추웠던 곳은 : {}'.format(city))




# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in citys['서울']:
    print('Yes')
else:
    print('No')

with open('ssafy_with.txt', 'r', encoding='euc-kr') as f:
    # readlines는 라인을 각각 리스트의 원소로 가지고 온다.
    lines = f.readlines()

for line in lines:
    print(line.strip())


with open('ssafy.txt', 'r') as f:
    txt = f.read()

print(txt)
print(type(txt))
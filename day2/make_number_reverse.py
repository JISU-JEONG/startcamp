with open('numbers.txt', 'r') as f:
    # readlines는 라인을 각각 리스트의 원소로 가지고 온다.
    lines = f.readlines()

lines.reverse()
print(lines)

with open('numbers_reverse.txt', 'w') as f:
    for i in lines:
        f.write(i)
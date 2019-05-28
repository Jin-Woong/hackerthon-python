# numbers.txt 의 내용을 뒤집어서 저장한다.

# 1. line 불러오기
with open('numbers.txt', 'r') as f:
    lines = f.readlines()

# 2. list 뒤집기
lines.reverse()

with open('numbers.txt', 'w') as f:
    for line in lines:
        f.write(line.rstrip() + '\n')
        # String.strip() 문자열의 처음와 끝의 공백 제거
        # rstrip() 오른쪽 공백 제거, lstrip() 왼쪽 공백 제거


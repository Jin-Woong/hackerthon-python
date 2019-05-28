# 1~45의 숫자 중에서 중복되지 않는 랜덤 6개의 숫자를 뽑아서 출력
import random

numbers = list(range(1,46))

lotto = random.sample(numbers, 6)

print(f'행운의 숫자는 {sorted(lotto)} 입니다!')

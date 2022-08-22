""" 1부터 100까지 임의의 수를 생성하고 생성된 임의의 수를 맞추는 게임 프로그램
숫자를 하나 입력하면 임의로 생성된 수보다 높은지 낮은지 정답인지 알려준다.
정답을 맞힌 경우 정답을 몇 번 만에 맞추었는지 그 결과로 게임의 승부를 알 수 있다. """

import random

random_num = random.randint(1,100)

#print(random_num)

cnt = 1

while True:
    try:
        my_num = int(input('1부터 100 사이의 숫자를 입력하세요.:'))
        if my_num > random_num:
            print('다운')
        elif my_num < random_num:
            print('업')
        else:
            print(f'축하합니다. {cnt}회 만에 맞추었습니다.')
            break
        cnt += 1
    except:
        print('에러가 발생했습니다. 숫자를 입력하세요')
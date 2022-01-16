# 슬롯머신 만들기
import random

while True:
    print("[Slot Machine Game]")
    a = int(input("1=게임시작 // 2=나가기 >>"))

    if a == 1:
        while True:
            b = int(input("1=코인 넣기 // 2=그냥 가기"))
            if b == 1:
                print("게임을 시작합니다")
                A = random.randint(33, 39)
                B = random.randint(33, 39)
                C = random.randint(33, 39)
                print("-------------")
                print("| %c | %c | %c |" %(A, B, C))
                print("-------------")
                if A == B == C:
                    print('축하합니다!')

                else:
                    print("아쉽네요 ㅠㅠ \n")

            elif b == 2:
                print("잘가요~ 다음에 다시만나요\n")
                break

            else:
                print('다시 입력해주세요')

    elif a == 2:
        print("게임을 종료합니다.")
        break

    else:
        print("잘못입력했습니다.")






# print('%c' %33)






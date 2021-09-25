# Ai반 2기 - 4주차 정규수업(16:30~18:00) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[3주차 활동내용]
1. 문자열 입출력 Mission
2. 변수와 자료형
3. 연산(1) - 산술연산
'''

# [연산(1) 이어서...]
## 문자열연산: + *
## mission1>> 해시태그1,2,3를 변수로 받고 +연산을 사용하여 이를 한 문장으로 만들어
## 출력해보자

'''
tag1 = "#안녕"
tag2 = "#잘가"
string = tag1 + tag2
print(string)
'''

## mission2>> *연산을 활용하여 같은 문장이 반복되는 문자열을 출력해보자

'''
string = "오정윤"*100
print(string)
'''


## mission>> 복함할당연산자를 연산을 하고, 그 연산이 무엇을 줄인 식인지 주석으로 적어보자.

'''
a = 100     # a = a + 30
a += 30
print(a)      
a -= 20
print(a)       # a = a- 10
a *= 10
print(a)       # a = a * 20
a /= 20
print(a)        # a = a / 20
a //= 50
print(a)       # a = a // 50
a %= 20
print(a)      # a = a % 20
a **= 20
print(a)      # a = a ** 20
'''


# [연산(2)]
## 비교연산: 2개 이상의 수를 비교하는 연산, 결과는 True or False
## mission>> <, > <=, >=, ==, != 연산을 하고 그 결과 예측(주석)하고 결과 확인하기

'''
print(5>8)      # False
print(3<8)      # True
print(10>=7)    # True
print(200>=751) # False
print(5==11)    # False
print(5!=5)     # False
print("3.141592653589793" == "3.141592653589783")                                # False
print("illIIilil|IIIIIilllllIIIlilil" != "illIIilil|IIIIIilllllIIIIlilil")       # True
'''

## 논리연산: and, or, not 연산, 결과는 True or False
## mission>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기

'''
print((4<6) and (10 >= 10))                                                  # True and True = True
print("LoskArk" != "LostArk" or "League of Legend" == "League of Legends")   # True or False = True
print(not 5==5)                                                              # not True = False
'''

## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## mission>> 멤버십 연산자를 활용하여 결과를 주석으로 달기

'''
print("Z" in "The Legend of Zelda")             # True
print("l" not in "A Dance of Fire and Ice")     # True
'''

# [입력과 자료형 변환]
## mission1>> input()함수 활용하여 변수 x,y에 숫자를 입력하고
## 이 숫자를 더하여 정수들의 합에 대한 결과를 출력해보자
'''
x = int(input("x를 입력하세요"))
y = int(input("y를 입력하세요"))
Sum = x + y
print(Sum)
'''

## mission2>> mission1에서 제대로 된 값이 나오도록 코드를 수정해보자.

## mission3>> 출생년도를 입력하고 나이를 출력해보자.

'''
born = int(input("당신의 출생년도를 입력해주세요"))
year = 2021
result = year - born + 1
print(result)
'''

# [조건문]
## 조건문이란?: 조건에 따라 명령이 달라지는 제어문,
## 제어문 및 함수의 주요 특징!: 제어문에 포함된 문장은 "띄어쓰기"로 구분한다.
## if문: 조건의 시작. if에 걸린 조건이 참일 경우, 포함된 문장들 실행
## else문: 조건이 거짓(False)인 경우, 포함된 문장을 실행
## elif문: if문의 조건이 거짓인 경우 중에서 elif문의 조건이 참일 때, 포함된 문장 실행
## mission1>> 구독자수를 입력받고 수익창출이 되는지 여부를 판단해보자


## mission2>> 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력하는 프로그램
## 20000원 이상: 오늘 저녁은 치킨이닭!
## 10000원 이상: 이제는 고오급 음식인 떡볶이 ㅎㅎ
## 2000원 이상: 그래도 굶지는 않는 편의점 삼각김밥!
## 2000원 미만: 없다고 못먹는건 아니다. 친구에게 "한입만!"을 외쳐보자


## mission3>> 국어, 영어, 수학 점수를 입력받고 합계와 평균를 출력한 뒤.
## - 평균이 60점이 넘을 경우: "보충 대상자가 아닙니다. 즐거운 방학보내세요"
## - 퍙균이 60점이 넘지 않을 경우: "보충 대상자입니다. 당신의 방학은 이제 제껍니다 ㅎㅎ"
## 를 출력하는 프로그램을 만들어 보자


# [리스트 자료형]
## 리스트를 사용하는 이유?: 여러개의 데이터를 한 번에 저장하기 위해서
## 문법: 리스트이름 = [데이터, 데이터, ... ,데이터]
## 연습문제>> 내가 자주보는 유투버 이름 각자 1개씩 카톡방(혹은 채팅방)에 올리고
## 이 이름들을 list로 만들기
'''
youtuber = []
print(youtuber)

## 리스트 제어하기1: 데이터 추가
## 방법: 리스트이름.append('추가할문자열')
## 연습문제>> 문자열에 수진썜이 좋아하는 유튜버 "승우아빠"를 추가해보자.
<명령입력>
print(youtuber)

## 리스트 제어하기2: 인덱싱
## 방법: 리스트이름[인덱스 번호], 여기서 인덱스 번호는 0부터 시작에 주의!
## python의 순서를 가진 것들은 기본 0부터 시작!!
## 연습문제>> 만들어진 유투버 리스트에서 내가 가장 좋아하는 유튜버만 출력해보자
print(<명령입력>)

## 리스트 제어하기3: 데이터 수정하기
## 방법: 리스트이름[인덱스 번호] = '새로넣을 문자열'
## 연습문제>> 내가 가장 좋아하는 유투버의 이름을 2번째로 좋아하는 유튜버의 이름으로 바꿔보자
<명령입력>
print(youtuber)

## 리스트 제어하기4: 데이터 삭제하기
## 방법: del 리스트이름[삭제할인덱스번호]
## 연습문제>> 아쉽지만(ㅎㅎ) 선생님이 추가한 유투버를 리스트에서 삭제해보자.
<명령입력>
print(youtuber)

## 리스트 제어하기5: 리스트 슬라이싱
## 방법: 리스트이름[처음:끝+1]
## 연습문제>> 처음~3번쨰, 2번째~끝, 3번째~4번째에 위치한 유투버들만, 그리고(':'를 활용하여) 리스트 전체을 출력해보자.
print(youtuber[:5])

## 리스트 제어하기6: 리스트 길이 구하기
## 방법: len(리스트이름)
## 연습문제>> 현재 리스트에 포함된 데이터의 개수를 구해보자
print(<명령입력>)

## 리스트 제어하기7: 리스트 정렬하기
## 방법1: 리스트이름.sort()  <- 오름차순 정렬
## 방법2: 리스트이름.sort(reverse=True)  <- 내림차순 정렬
## 연습문제>> 유투버들을 오름차순과 내림차순으로 정렬한 결과를 각각 출력해보자
<명령입력>
print(youtuber)
<명령입력>
print(youtuber)
'''

## 리스트 mission1
## :RGB 색상(red, green,blue)을 리스트에 저장하고
##  turtle 모듈을 활용하여 색상이 서로 다른 직선을 그려보자
##  (설정: 굵기(30), 선 길이(200))
'''
import turtle

# 작성1: 리스트 color 선언하기 
win = turtle.Screen()
win.setup(600, 600)
t = turtle.Turtle('turtle')
t.pensize(30)

t.penup()
t.pencolor(<작성부분1>)
t.pendown()
t.fd(200)

t.penup()
t.setpos(0, <이동좌표>)
t.pencolor(<작성부분2>)
t.pendown()
t.fd(200)

t.penup()
t.setpos(0, <이동좌표>)
t.pencolor(<작성부분3>)
t.pendown()
t.fd(200)

win.mainloop()
'''

## 리스트 mission2
## 다음은 1번~5번 학생의 1분간 턱걸이 개수이다
'''
pull_up = [3, 16, 2, 5, 10, 7]
## 1번 문제: 7번째 학생의 턱걸이 개수가 9라고 할 때, 이를 리스트에 추가해보자
<명령입력>
print(pull_up)
## 2번 문제: 2번 학생의 재측정 결과 20개의 턱걸이를 하였다. 리스트에 데이터를 수정해보자
<명령입력>
print(pull_up)
## 3번 문제: 3~7번까지의 학생의 턱걸이 갯수만을 뽑아 temp 변수에 저장하고 출력해보자
<명령입력>
print(temp)
## 4번 문제: 학생들의 턱걸이 횟수 데이터를 오름차순으로 정렬
<명령입력>
print(pull_up)
'''
# Ai반 2기 - 3주차 정규수업(16:30~18:00) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[2주차 활동내용]
1. 환경설정 마무리
2. python 소개와 활용 프로그램의 용도 설명
3. 문자열 입출력
'''

# [문자열 입출력]
## 문자열 입출력 Mission
'''
name = input("이름을 입력하세요")
string  = input("지금 하고싶은 말은?")
print (f'{name}은 {string}이라고 말했다.')
'''

# [자료형]
# ※ 참고: 모두의 파이썬 68p
## 숫자형 1) 정수형(integer, int)
## : 소수점이 없는 숫자의 형태
## mission>> 정수형인 숫자를 출력하고 type() 함수를 활용하여
## 자료형을 주석으로 적기

'''
print(12234,4,5,6)
print(type(5))      #int
'''

## 숫자형 2) 실수형(float)
## : 소수점이 있는 숫자의 형태
## mission>> 실수형인 숫자를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기

'''
print(0.344,0.4456,3.445)
print(type(0.344))      #float
'''

## 문자열
## : 문자를 나열한 형태의 자료형
## mission1>> ""와 ''를 활용하여 내가 지금 하고 싶은 말을 문자열로 출력하기

'''
print("야호")
print("사랑해")
print(type("사랑해"))       #str
'''

## mission2>> 문자열로 인용구호('') 출력하기

'''
print('"나는 배가고프다!"라고 소리쳤다.')
print("'야'라고 생각했다")
'''


## mission3>> sep과 end를 활용하여 print() 용법 익히기
## sep: ,로 출력이 구분된 문자열 사이 출력 설정 // end: print문의 끝났을 때의 문자열 출력 설정

'''
print(1,2,3,4,5,6,7, sep='응애', end='애옹')
'''

## - 불린형(참/거짓)
## : 참(True)/거짓(False) 형태의 자료형
## mission>> 불린형의 True와 False를 출력하고 type() 함수를 활용하여
## 자료형을 주석으로 적기

'''
print(True)
print(False)
print(type(True))   # bool
'''

# ※ 변수와 연산자 참고: 모두의 파이썬 35p
# [변수]
## 변수란?: 데이터를 저장할 공간. 할당연산자(=)를 활용.
## 특징: "언제든지 데이터를 변경"할 수 있다.
## 문법: 변수이름 = 데이터
## mission>> 내가 좋아하는 게임의 캐릭터 혹은 재밋게 본 책의 정보, 하드웨어 스펙, 게임 정보 등 어떤것도 상관 없음.
## 변수로 저장하고 출력해보자.
## 예시) LOL 챔피언 정보: https://lol.inven.co.kr/dataninfo/champion/compare.php

'''
game = 'league of legends'
name = '케이틀린'
attack = 510
reach = 650
speed = 325

print(f'게임:{game}')
print(f'이름:{name}')
print(f'공격력:{attack}')
print(f'이동속도:{speed}')
print(f'사거리:{reach}')
'''

## 변수 Mission: input()응용하기, 속으로 10초를 세어 맞히는 프로그램 (교재 71p)

'''
import time

input("Enter를 누르고 속으로 10초를 다 세는 게임입니다. Enter를 누르면 시작합니다!")
start =  time.time()

input("10초를 다 세셨다면 Enter를 눌러 Stop!")
end = time.time()

et = end-start
print(f'실제시간: {et}초')
print(f'차이:{abs(et-10)}초')
'''

# [연산(1)]
## 연산이란?: 수나 식을 일정한 '규칙'에 따라 계산하는 것
## 대입연산: 할당연산자(=)를 활용하여 데이터를 변수에 대입하는 연산자

'''
number = 234
'''

## 숫자산술연산: + - * / 와 같은 수의 계산에 대한 연산자
## mission>> 7과 3에 대해서 + - * / // % **의 결과를 출력하기

'''
print(7+3)   #10
print(7-3)   #4
print(7*3)   #21
print(7/3)   #2.3333333
print(7//3)  #2
print(7%3)   #1
print(7**3)  #343
'''

## 문자열연산: + *
## mission1>> 해시태그1,2,3를 변수로 받고 +연산을 사용하여 이를 한 문장으로 만들어
## 출력해보자


## mission2>> *연산을 활용하여 같은 문장이 반복되는 문자열을 출력해보자


## mission>> 복함할당연산자를 연산을 하고, 그 연산이 무엇을 줄인 식인지 주석으로 적어보자.


# [연산(2)]
## 비교연산: 2개 이상의 수를 비교하는 연산, 결과는 True or False
## mission>> <, > <=, >=, ==, != 연산을 하고 그 결과 예측(주석)하고 결과 확인하기
'''
print(5>8)      
print(3<8)      
print(10>=7)    
print(200>=751) 
print(5==11)    
print(5!=5)    
print("3.141592653589793" == "3.141592653589783")           
print("illIIilil|IIIIIilllllIIIlilil" != "illIIilil|IIIIIilllllIIIIlilil")  
'''

## 논리연산: and, or, not 연산, 결과는 True or False
## mission>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기
'''
print((4<6) and (10 >= 10))     
print("LoskArk" != "LostArk" or "League of Legend" == "League of Legends")   
print(not 5==5)     
'''
## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## mission>> 멤버십 연산자를 활용하여 결과를 주석으로 달기
'''
print("Z" in "The Legend of Zelda")             
print("l" not in "A Dance of Fire and Ice")     
'''
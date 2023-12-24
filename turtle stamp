
import turtle as t
import random

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()  # r: random.random(): 0~1상이의 랜덤한 값 할당
    g = random.random()  # g
    b = random.random()  # b
    return r, g, b          # return

# leftClick 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def turtleStamp(x, y):
    t.hideturtle()      # 거북이 숨기기
    t.setposition(x, y)  # (x,y)좌표로 거북이 이동
    t.setheading(random.randint(0,360)) # 랜덤하게 거북이의 머리 방향 지정(0~360도)
    t.shapesize(random.randint(1,10))   # 랜덤하게 거북이의 크기 설정(1~10)
    r, g, b = randomColor() # 랜덤 r,g,b 값 가져오기(randomColor 함수 사용하기)
    t.fillcolor(r, g, b)      # 스템프 색상 설정(랜덤 r,g,b 값 넣기)
    t.pencolor(r, g, b)       # 스템프 테두리 색성 설정(랜덤 r,g,b 값 넣기)
    t.stamp()                 # 스템프 찍기 명령

# rightClick 이벤트 핸들링 함수: 화면을 초기화하는 함수
def rightClick(x, y):

    t.clear()

    # 화면 초기화

t.title('거북이 마우스 이벤트 처리 프로그램')  # 프로그램 제목 지정
t.shape('turtle')                        # 도장 모양을 turtle으로 설정
t.speed(0)                               # 속도 설정
t.penup()                                # 펜 들기

t.onscreenclick(turtleStamp, 1)       # 이벤트 설정: onscreenclick
# <오른쪽 클릭 이벤트 설정>
t.onscreenclick(rightClick, 3)
t.mainloop()

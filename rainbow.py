
import turtle

# 변수 및 객체 선언
win = turtle.Screen()
t = turtle.Turtle('turtle')
rainbow_size = 500         # 무지개 크기(너비)
pen_size = 30              # 펜 굵기
rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']      # 활용할 색상 지정
t.speed(0)                # 거북이 속도 설정

# 펜 초기 설정
t.pensize(pen_size)

# for 반복문 실행(무지개 그리기)

for i in range(7):
    t.setheading(90)
    t.penup()
    t.setpos(rainbow_size-(pen_size*i), -10)
    t.pencolor(rainbow_color[i])
    t.pendown()
    t.circle(rainbow_size-(pen_size*i), 180)
turtle.mainloop()

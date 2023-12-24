
import turtle as t

n = 360
t.bgcolor('black')
color = ['sky blue', 'blue','navy','purple']
t.speed(0)

for i in range(n):
    t.pencolor(color[i % len(color)])
    t.circle(200)
    t.left(360/n)
t.mainloop()

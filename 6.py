import turtle as t

t.shape('turtle')
n = input("Введите n")
n=int(n)
a=0
t.goto(0,0)
while a < 360:
 t.right(360/n)
 t.forward(100)
 t.stamp()
 t.penup()
 t.goto(0,0)
 t.pendown()

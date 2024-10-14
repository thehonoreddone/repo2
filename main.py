import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor('light blue')
turtle_screen.title("oyun")

turtle_instance8=turtle.Turtle()

def turtle_forward():
    turtle_instance8.forward(100)

def turtle_left():
    turtle_instance8.setheading(turtle_instance8.heading()-10)


def turtle_right():
    turtle_instance8.setheading(turtle_instance8.heading()+10)

def clear_screen():
    turtle_instance8.clear()

def return_home():
    turtle_instance8.penup()   # kalemi kaldırır çizmeyi bırakır
    turtle_instance8.home() #başladıgı yere geri döner
    turtle_instance8.pendown()  #kalemi indirir cizmeye devam

turtle_screen.listen()
turtle_screen.onkey(turtle_forward,' space ') #fonksiyonu çalıştır olarak çağırmayız sadece referans w'ye basınca onu çalıştır.
turtle_screen.onkey(turtle_left,'Up')
turtle_screen.onkey(turtle_right,'Down')
turtle_screen.onkey(clear_screen,'c')
turtle_screen.onkey(return_home,'h')

turtle.done()    # turtle_screen.mainloop()

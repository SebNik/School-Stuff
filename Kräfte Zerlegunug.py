def cal_res_Kraft(alpha, force_one, force_two):
    # diese Funktion berechente die resultierende Kraft
    # alle einheiten sollten in Newton angegben werden
    # der Winkel wird in Grad angegeben
    # es werden nur integer benutzt
    import math
    return math.sqrt(force_one ** 2 + force_two ** 2 + 2 * force_one * force_two * math.cos(math.radians(alpha)))


def draw_forces(alpha, f1, f2, speed=1):
    # hier kann das ganze gedoens aufgezeichnet werden
    # mit dem turle modul
    breite = 1200
    hoehe = 800
    import turtle
    t = turtle.Turtle()
    s = turtle.getscreen()
    s.setup(breite, hoehe)
    # berechnung der Skalierung
    if f1 > f2:
        f1_scale = 350
        f2_scale = (f2 * 350) / f1
    else:
        f2_scale = 350
        f1_scale = (f1 * 350) / f2
    # nun sind die sklaierten Kraefte festgelegt
    # moege das Zeichen beginnen!
    t.shape("turtle")
    t.reset()
    t.penup()
    turtle.title("Copyright Niklas Abraham")
    t.fillcolor("red")
    t.speed(speed)
    t.goto(-300, 0)
    t.clear()
    t.clearstamps()
    t.pendown()
    t.pensize(5)
    t.pencolor('red')
    t.pendown()
    t.right(alpha / 2)
    t.forward(f1_scale)
    t.shape("arrow")
    t.stamp()
    t.shape("turtle")
    pos_1 = t.pos()
    t.penup()
    t.goto(-300, 0)
    t.left(alpha)
    t.pendown()
    t.pencolor('blue')
    t.fillcolor("blue")
    t.forward(f2_scale)
    t.shape("arrow")
    t.stamp()
    t.shape("turtle")
    t.pencolor('red')
    t.fillcolor("red")
    t.right(alpha)
    t.forward(f1_scale)
    t.shape("arrow")
    t.stamp()
    t.shape("turtle")
    t.penup()
    t.goto(pos_1[0], pos_1[1])
    t.shape("arrow")
    t.stamp()
    t.shape("turtle")
    t.pencolor('blue')
    t.fillcolor("blue")
    t.pendown()
    t.left(alpha)
    t.forward(f2_scale)
    t.shape("arrow")
    t.stamp()
    t.shape("turtle")
    t.penup()
    pos_2 = t.pos()
    t.goto(-300, 0)
    t.pencolor('green')
    t.fillcolor("green")
    t.right(alpha)
    t.pendown()
    t.goto(pos_2[0], pos_2[1])
    print('Die resultierende Kraft ist:', cal_res_Kraft(alpha, f1, f2))


draw_forces(80, 5, 15, 1)

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
# Added some icons
colorTiles = ["❤", "✰", "☀", "✄", "✌", "☢", "✼", "♕",
              "☮", "☘", "☃", "☎", "☻", "♘", "♤", "♧",
              "⚠", "✧", "❑", "❦", "⬟", "✜", "✥", "✎",
              "✈", "⛾", "⛱", "⛩", "⛟", "⛏", "⚑", "☠"]
colorTiles = [val for val in colorTiles for _ in (0, 1)]

state = {'mark': None}
hide = [True] * 64
tap_number = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    global tap_number

    if mark is None or mark == spot or colorTiles[mark] != colorTiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    tap_number += 1

def allTilesRevealed():
    for tile in hide:
        if tile:
            return False
    return True

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 8)
        color('black')
        write(colorTiles[mark], align="center", font=('Arial', 30, 'normal'))
    
    if allTilesRevealed():
        goto(-110,-30)
        color('white')
        write("Has Ganado",False, font=('Arial', 35, 'normal'))

    up()
    goto(x = -212, y = 198)
    write(tap_number, False, font = ('Arial', 10, 'normal'))
    update()
    ontimer(draw, 100)

shuffle(colorTiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
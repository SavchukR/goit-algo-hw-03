import turtle
import argparse
# debug only
from collections import namedtuple 

def parse_args():
    parser = argparse.ArgumentParser(description='Сніжинка Коха.')
    parser.add_argument('level', type=int, help='Рівень рекурсії')
    return parser.parse_args()

# debug
# def parse_args():
#     Args = namedtuple('parseargs', ['level']) 
#     arg = Args(4)
#     return  arg

def draw(t, length, level):
    for item in range(3):
        curve(t, length, level)
        t.right(120)
        
def curve(t, length, level):
    
    if level == 0:
        t.forward(length)
        return
    
    length /= 4.0
    
    curve(t, length, level-1)
    t.left(60)
    
    curve(t, length, level-1)
    t.right(120)
    
    curve(t, length, level-1)
    t.left(60)
    
    curve(t, length, level-1)


def main():
    args = parse_args()
    level = args.level

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title(f'Рівень рекурсії {level}')

    # draw
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-100, 100)
    t.pendown()

    draw(t, 400, level)

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()

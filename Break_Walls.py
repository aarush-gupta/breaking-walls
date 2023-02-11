# Tkinter
"""import tkinter as label
"""
import pygame
import turtle
import random
from pygame.locals import *

# Turtle
t=turtle.Turtle()

color = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
turtle.Screen().bgcolor("black")
t.speed(0)
# turtle.bgpic("image/background (1).jpg"\)
t = turtle.Turtle()

for x in range(20):
    t.pencolor(color[x % 6])
    t.circle(x)
    t.left(15)

turtle.clear()
t.shape("square")
t.shapesize(5)
t.penup()
t.setposition(-400, 300)
t.fillcolor("red")
t.stamp()
t.fillcolor("orange")
t.setposition(-250, 300)
t.stamp()
t.fillcolor("yellow")
t.setposition(-100, 300)
t.stamp()
t.fillcolor("green")
t.setposition(50, 300)
t.stamp()
t.fillcolor("cyan")
t.setposition(200, 300)
t.stamp()
t.fillcolor("blue")
t.setposition(350, 300)
t.stamp()
t.fillcolor("white")

t.shape("circle")
for x in range(10):
    t.goto(random.randint(-400, 400), random.randint(-300, 300))


t.clear()

"""t.write("", move=False, align="left", font=("Arial", 8, "normal"))
"""
t.setposition(0, 0)
t.hideturtle()
t.clear()

"""t.__sizeof__()
t.turtlesize(10)"""
t.write("NotblueGames \nClick here to start", font=("Arial", 50, "normal"), align="left")


# Tkinter


def start_pygame(x,y):
    turtle.Screen().bye()
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Breakin' Walls")
    #bat
    bat = pygame.image.load('paddle.png')
    bat = bat.convert_alpha()
    bat_rect = bat.get_rect()
    bat_rect[1]=screen.get_height()-100

    #ball
    ball= pygame.image.load('football.png')
    ball = bat.convert_alpha()
    ball_rect = bat.get_rect()
    ball_start = (200, 200)
    ball_speed = 3.0, 3.0
    ball_served = False
    sx, sy = ball_speed
    ball_rect.topleft = ball_start
    # brick
    brick = pygame.image.load('brick.png')
    brick = brick.convert_alpha()
    brick_rect = brick.get_rect()
    bricks = []
    brick_rows = 5
    brick_gap = 10
    brick_cols = screen.get_width()//(brick_rect[2]+brick_gap)
    side_gap = (screen.get_width()-(brick_rect[2]+brick_gap)*brick_cols+brick_gap)//2
    for y in range(brick_rows):
        brickY = y*(brick_rect[3]+brick_gap)
        for x in range(brick_cols):
            brickX = x*(brick_rect[2]+brick_gap)+side_gap
            bricks.append((brickX, brickY))
    clock = pygame.time.Clock()
    x = 0
    is_running = False
    while not is_running:
        dt = clock.tick(50)
        # Event iteration
        screen.fill((0, 0, 0))
        for b in bricks:
            screen.blit(brick, b)
        screen.blit(bat, bat_rect)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                is_running = True
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            x -= 0.5*dt
        if pressed[K_RIGHT]:
            x += 0.5*dt
        bat_rect[0] = x
        pygame.display.update()
turtle.Screen().onscreenclick(start_pygame , 1)
turtle.Screen().mainloop()

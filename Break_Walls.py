# Tkinter
"""import tkinter as label
"""
import pygame
import turtle

# Turtle
color = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
turtle.getscreen()
turtle.bgcolor("Gray")
# turtle.bgpic("image/background (1).jpg"\)
t = turtle.Turtle()
for x in range(7):
    t.shapesize(2)
    t.pencolor(color[x % 6])
    t.circle(50*x)
    t.left(10)
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

t.setposition(-400, 100)
t.fillcolor("red")
t.stamp()
t.fillcolor("orange")
t.setposition(-250, 100)
t.stamp()
t.fillcolor("yellow")
t.setposition(-100, 100)
t.stamp()
t.fillcolor("green")
t.setposition(50, 100)
t.stamp()
t.fillcolor("cyan")
t.setposition(200, 100)
t.stamp()
t.fillcolor("blue")
t.setposition(350, 100)
t.stamp()

t.setposition(-400, -100)
t.fillcolor("red")
t.stamp()
t.fillcolor("orange")
t.setposition(-250, -100)
t.stamp()
t.fillcolor("yellow")
t.setposition(-100, -100)
t.stamp()
t.fillcolor("green")
t.setposition(50, -100)
t.stamp()
t.fillcolor("cyan")
t.setposition(200, -100)
t.stamp()
t.fillcolor("blue")
t.setposition(350, -100)
t.stamp()

t.shape("square")
t.shapesize(5)
t.penup()
t.setposition(-400, -300)
t.fillcolor("red")
t.stamp()
t.fillcolor("orange")
t.setposition(-250, -300)
t.stamp()
t.fillcolor("yellow")
t.setposition(-100, -300)
t.stamp()
t.fillcolor("green")
t.setposition(50, -300)
t.stamp()
t.fillcolor("cyan")
t.setposition(200, -300)
t.stamp()
t.fillcolor("blue")
t.setposition(350, -300)
t.stamp()
t.clear()
"""t.write("", move=False, align="left", font=("Arial", 8, "normal"))
"""
t.setposition(0, 0)
t.hideturtle()

t.__sizeof__()
t.turtlesize(10)
t.write("NotblueGames \n Click here to start the game")

t.clear()
"""t.write("Click here to start the game")
"""
# Tkinter
"""root = label()
root.geometry("15x15")
root.title(" Search ")"""


# Pygame


def start_pygame(x, y):
    turtle.Screen().bye()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("⚽️Breaking walls🧱")
    img_bg = pygame.image.load("image/background (1).jpg")
    screen.blit(img_bg, (0, 0))
    bat = pygame.image.load("paddle.png")
    bat = bat.convert_alpha()
    bat_rect = bat.get_rect()
    ball = pygame.image.load("football.png")
    ball = ball.convert_alpha()
    ball_rect = ball.get_rect()
    brick = pygame.image.load("brick.png")
    brick = brick.convert_alpha()
    brick_rect = brick.get_rect()
    bricks = []
    brick_rows = 5
    brick_cols = screen.get_width()//(brick_rect[2])
    brick_gap = 10
    # side_gap = (screen.get_width()-(brick.rect[2] + brick_gap) + brick_cols)//2
    for y in range(brick_rows):
        brickY = y*(brick_rect[3] + 5)
        for x in range(brick_cols):
            brickX = x*(brick_rect[2] + 5)
            bricks.append((brickX, brickY))
    still_going = True
    while still_going:
        screen.fill((0, 0, 0))
        screen.blit(img_bg, (0, 0))
        for b in bricks:
            screen.blit(brick, b)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                still_going = False
        pygame.display.update()
    pygame.quit()


turtle.Screen().onscreenclick(start_pygame, 1)
turtle.Screen().mainloop()

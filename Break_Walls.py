# Tkinter
"""import tkinter as label
"""
import pygame
import turtle
import random
from pygame.locals import *
timey = 0
# Turtle
t = turtle.Turtle()
color = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
turtle.Screen().bgcolor("gray")
t.speed(0)
# turtle.bgpic("image/background (1).jpg"\)
t = turtle.Turtle()

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
s = turtle.Turtle()
t.shape("circle")
for x in range(5):
    t.goto(random.randint(-400, 400), random.randint(-300, 300))


t.clear()

"""t.write("", move=False, align="left", font=("Arial", 8, "normal"))
"""
s.setposition(0, 0)
t.hideturtle()
t.clear()

"""t.__sizeof__()"""
s.write("NotblueGames \nClick here to start", font=("Arial", 50, "normal"), align="right")

# Tkinter
white = [200, 200, 200]
ball_speed = (10.0, 10.0)

def start_pygame(x, y):
    timey = 2500
    life = 3
    lava = pygame.image.load('rectangle.png')
    more_lava = pygame.image.load('rectangle.png')
    even_more_lava = pygame.image.load('rectangle.png')
    score = 0
    pygame.display.set_caption("⚽️Break walls🧱")
    turtle.Screen().bye()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    # bat
    bat = pygame.image.load('paddle.png')
    bat = bat.convert_alpha()
    bat_rect = bat.get_rect()
    bat_rect[1] = screen.get_height()-50

    ball = pygame.image.load('football.png')
    ball = ball.convert_alpha()
    ball_rect = ball.get_rect()
    ball_start = (200, 200)
    ball_speed = (10.0,  10.0)
    ball_served = False
    sx, sy = ball_speed
    ball_rect.topleft = ball_start



    ball_rect.topleft = ball_start
    # brick
    brick = pygame.image.load('brick.png')
    brick = brick.convert_alpha()
    brick_rect = brick.get_rect()
    bricks = []
    brick_rows = 6
    brick_gap = 7
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
        screen.fill((0, 0, 10))
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score), bool(1), white)
        more_text = font.render("Time: " + str(timey), bool(1), white)
        even_more_text = font.render("Lives❤️: " + str(life), bool(1), white)


        screen.blit(text, (10, 10))
        for b in bricks:
            screen.blit(brick, b)
        screen.blit(lava, (175, 475))
        screen.blit(more_lava, (-100, 475))
        screen.blit(even_more_lava, (500, 475))

        screen.blit(bat, bat_rect)
        screen.blit(ball, ball_rect)
        screen.blit(text, (10, 10))
        screen.blit(more_text, (625, 10))
        screen.blit(even_more_text, (312, 10))



        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                is_running = True
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            x -= 0.5*dt
        if pressed[K_RIGHT]:
            x += 0.5*dt

        ball_served = True

        if bat_rect[0] + bat_rect.width >= ball_rect[0] and \
            ball_rect[1] + ball_rect.height >= bat_rect[1] and \
            sy > 0:
            sy *= -1
            sx *= 1.01
            sy *= 1.01
            continue

        delete_brick = None
        for b in bricks:
            bx, by = b
            if bx <= ball_rect[0] <= bx + brick_rect.width and \
                    by <= ball_rect[1] <= by + brick_rect.height:
                delete_brick = b
        if delete_brick is not None:
            bricks.remove(delete_brick)
            score += random.randint(1, 15)
            timey += 5
            ___random___ = random.randint(0, 3)
            if ___random___ == 0:
                sy *= -1.01
            if ___random___ == 1:
                sy *= 1.01
            if ___random___ == 2:
                sx *= -1.01
            if ___random___ == 3:
                sx *= 1.01
            # while sy == sy*-1 or sy == sy*1 and sx == sx*-1 or sx == sx*1:

            # sx *= 1.01
            # sy *= 1.01

        if ball_rect[1] <= 0:
            ball_rect[1] = 0
            sy *= -1
            score += random.randint(1, 15)
        if ball_rect[0] <= 0:
            ball_rect[0] = 0
            sx *= -1
            score += random.randint(1, 15)
        if ball_rect[1] >= screen.get_height() - ball_rect.height:
            ball_rect[1] = screen.get_height() - ball_rect.height
            sy *= -1
            life -= 1

        if ball_rect[0] >= screen.get_width() - ball_rect.width:
            ball_rect[0] = screen.get_width() - ball_rect.width
            sx *= -1
            score += random.randint(1, 15)

        bat_rect[0] = x
        if ball_served:
            ball_rect[0] += sx
            ball_rect[1] += sy

        if x <= 0:
            x = 35
        elif x >= 736:
            x = 675
        if life <= 0:
            print("Final score = ", score)
            quit()
        if score >= 300 and  score <= 700:
            ball_speed = (10, 10)
        elif score >= 700 and score <= 1000:
            ball_speed = (13, 13)
        elif score >= 1000 and score <= 1250:
            ball_speed = (15, 15)
        elif score >= 1250:
            ball_speed = (20, 20)
        else:
            ball_speed = (7, 7)

        timey -= 1
        if timey <= 0:
            print("Final score: ", score + 250)
            quit()
        pygame.display.update()
        bat_rect[0] = x

turtle.Screen().onscreenclick(start_pygame , 1)
turtle.Screen().mainloop()

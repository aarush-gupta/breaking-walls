import pygame

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
brick_cols = 3
for y in range(brick_rows):
    brickY = y*brick_rect[3]
    for x in range(brick_cols):
        brickX = x*brick_rect[2]
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

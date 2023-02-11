import pygame

# Initialize pygame
pygame.init()

# Set the display size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Label Example")

# Create the label's text and font
font_name = pygame.font.get_default_font()
font = pygame.font.Font(font_name, 32)
text = "Hello, World!"

# Render the text as an image
label = font.render(text, True, (255, 255, 255))

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the label on the screen
    screen.blit(label, (250, 250))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()

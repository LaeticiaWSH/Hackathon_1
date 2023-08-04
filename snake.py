import pygame

pygame.init() #It's mandatory to initialize the import pygame.

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # pygame.display.set_mode, it  sets the screen to be displayed.
pygame.display.set_caption("Game")
run = True

while run: #A statement that will keep the screen open .
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark green")

    # flip() the display to put your work on screen
    pygame.display.update()

pygame.quit() # The function that will close the screen.


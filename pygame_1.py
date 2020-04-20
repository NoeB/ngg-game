import pygame
import random
#Initialize pygame
pygame.init()
# Set the screen size of our game
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
#Main Event loop
done = False
#Game loop
game_over = False
# Variable to store all the snake rectangles
green=(76, 235, 52)
red=(255, 0, 0)
#A rectangle at the position: left/y: 30, top/x: 30, width: 20, height:20
snake = pygame.Rect(40, 40, 20, 20)


#pygame clock to control the refresh rate of our game
clock = pygame.time.Clock()

while not done:
    #Set the backgroudn color to black
    screen.fill((0, 0, 0))
    #Close the game if someone clicks the X top right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        pygame.draw.rect(screen,green, snake)

        pygame.display.flip()
        #Define the frame rate = how many times per second the screen schould refresh and the snake move
        clock.tick(5)

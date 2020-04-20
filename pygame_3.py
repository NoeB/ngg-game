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
#List of all snake rectangles
snake_segments = [pygame.Rect(40, 40, 20, 20)]

#generate start version of the snake
for x in range(9):
    #Copy the last item and add the y-axis/top value +20
    y = snake_segments[-1].y
    y += 20
    snake_segments.append(pygame.Rect(40, y, 20, 20))

#Start Speed
x_change = 20
y_change = 0

#pygame clock to control the refresh rate of our game
clock = pygame.time.Clock()

while not done:
    #Set the backgroudn color to black
    screen.fill((0, 0, 0))
    #Close the game if someone clicks the X top right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #Keyboard input arrow keys
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        x_change = 0
        y_change = -20
    if pressed[pygame.K_DOWN]:
        x_change = 0
        y_change = 20
    if pressed[pygame.K_LEFT]:
        x_change = -20
        y_change = 0
    if pressed[pygame.K_RIGHT]:
        x_change = 20
        y_change = 0
        

    x = snake_segments[0].x + x_change
    y = snake_segments[0].y + y_change

    #Remove the last element so the snake will move and remains the same lenght 
    snake_segments.pop()   
    #Append the moved part a the new position
    snake_segments.insert(0, pygame.Rect(x, y, 20, 20))

    #Draw all parts of the snake
    for segment in snake_segments:
        pygame.draw.rect(screen, green, segment)


    pygame.display.flip()
    #Define the frame rate = how many times per second the screen schould refresh and the snake move
    clock.tick(5)

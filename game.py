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
#Generate the Apple rectangle random
apple = pygame.Rect(random.randint(0, screen_width /20) *20,
                    random.randint(0, screen_height /20) *20, 20, 20)
#Start Speed
x_change = 20
y_change = 0
#Score
Score = 0
#generate start version of the snake
for x in range(9):
    #Copy the last item and add the y-axis/top value +20
    y = snake_segments[-1].y
    y += 20
    snake_segments.append(pygame.Rect(40, y, 20, 20))

#pygame clock to control the refresh rate of our game
clock = pygame.time.Clock()

while not done:
    #Set the backgroudn color to black
    screen.fill((0, 0, 0))
    #Close the game if someone clicks the X top right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not game_over:
        #Keyboard input
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
        #Check if the snake collides with the apple if so add 1 point to the score, add one rectangle to the snake and generate a new apple
        if snake_segments[0].colliderect(apple):
            Score += 1
            # Add new snake element

            # place new apple and check if position is empty
            generating_place = True
            while(generating_place):
                apple = pygame.Rect(random.randint(2, (screen_width -20)/20) *20,
                    random.randint(2, (screen_height -20)/20) *20, 20, 20)
                #Check that the apple is not overlapped with the snake
                if apple.collidelistall(snake_segments) != [0]:
                    generating_place = False
        else:
            #Remove the last element so the snake will move and remains the same lenght 
            snake_segments.pop()

        x = snake_segments[0].x + x_change
        y = snake_segments[0].y + y_change
        #Check if the snake is not out of the screen if so Game Over.
        if(x > screen_width or x < 0 or y > screen_height or y < 0):
            game_over = True
        #Check if the snake runs into istelf if so = Game Over
        if snake_segments[0].collidelistall(snake_segments) != [0]:
            game_over = True    
        #Append the moved part a the new position
        snake_segments.insert(0, pygame.Rect(x, y, 20, 20))

        #Draw all parts of the snake
        for segment in snake_segments:
            pygame.draw.rect(screen, green, segment)

        #If the Game is over write: Game Over in the middle of the Screen    
        if game_over:
            font = pygame.font.Font(None, 90)
            text = font.render("Game Over ..", 1, (255, 255, 255))
            screen.blit(text, (int(screen_width / 4), int(screen_height / 2)))
        
        # draw the apple
        pygame.draw.rect(screen, red, apple)
        # draw the score
        font = pygame.font.Font(None, 30)
        text = font.render("Score: " + str(Score), 1, (255, 255, 255))
        screen.blit(text, (650, 10))

        pygame.display.flip()
        #Define the frame rate = how many times per second the screen schould refresh and the snake move
        clock.tick(5)

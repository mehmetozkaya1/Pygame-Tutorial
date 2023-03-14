# Keyboard input
# jump and gravity
# floor

import pygame
from sys import exit

pygame.init() # Starts pygame and loads all of the stuffs
screen = pygame.display.set_mode((800,400)) # Creating a screen
pygame.display.set_caption("Runner") # Setting the caption of the game.
clock = pygame.time.Clock() # We have created a clock to adjust FPS
test_font = pygame.font.Font(r'ClearCode\font\Pixeltype.ttf',50) # We have created a font object fot texts. (first parameter is font type and the second is font size). We have imported our custom font with its folder.

sky_surface = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/Pygame/ClearCode/graphics/Sky.png").convert() # We have imported an image(change the slashes) We are converting the images to use them easily in pygame
ground_surface = pygame.image.load("ClearCode\graphics\ground.png").convert() # We imported our ground. We are converting the images to use them easily in pygame

score_surf = test_font.render("My Game", False, (64,64,64)) # We created a text surface. render takes 3 argument (1. Text, 2. AA(anti alise),3. color) (anti alise will make your text's edges smooth. So if you dont use any pixel font you should use it.) (red,green,blue)
score_rect = score_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load("ClearCode\graphics\snail\snail1.png").convert_alpha() # We created a snail surface. We are converting the images to use them easily in pygame
snail_rect = snail_surface.get_rect(bottomright = (600,300)) # We have created a rectangle around snail.

player_surf = pygame.image.load('ClearCode\graphics\Player\player_walk_1.png').convert_alpha() # We created a player surface. And converted it.
player_rect = player_surf.get_rect(midbottom = (80,300)) # get_rect() method gets the plater surface and draws aa rectangle around it. And adjusted its position. rectangle's parametre is the point of drawing.

while True: # It will run the game forever.

    for event in pygame.event.get(): # Every event that player can do in a for loop
        if event.type == pygame.QUIT: # If player quit the game.
            pygame.quit() # Quit the game.
            exit() # This method will break the loop bcs we can't run other codes after we close the game.
        
        # if event.type == pygame.MOUSEMOTION:

        #     if player_rect.collidepoint(event.pos): # If the mouse collides with the player.

        #         print("collision")

        # Keyboard input

        if event.type == pygame.KEYDOWN: # We check if one of the button of the keyboard is pushed down.
            if event.key == pygame.K_SPACE:
                print("jump")
        
        if event.type == pygame.KEYUP: # We check if we release one of the button of the keyboard.
            print("key up")

    screen.blit(sky_surface, (0,0)) # We replaced it in our display surface 
    screen.blit(ground_surface, (0,300)) # We replaced our ground.

    # Drawing a line:

    # pygame.draw.line(screen, "Gold", (0,0), pygame.mouse.get_pos(), 10)

    # Drawing a circle:

    # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100)) # We have created a new rect inside the method and drawed a circle.

    # Score's background color:

    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect,6) # We are drawing something with draw method. Then we specify what kind of thing we draw.
    # rect(where are we drawing, what is the colr, which rect, line width, border radius(round border.))
    screen.blit(score_surf, score_rect) # We have replaced our text and rectangle.
    
    snail_rect.x -= 4 # We make our char move left.

    if snail_rect.right <= 0: # If the char's rectangle's right side is below zero which means our char has left the screen, we can reset its rectangle's left position to 800 which is the width of our screen.

        snail_rect.left = 800

    screen.blit(snail_surface, snail_rect) # We replaced our snail.
    # player_rect.left += 1 # We can make our character move right with rectangle.
    # print(player_rect) # We can measure something with this code.
    screen.blit(player_surf, player_rect) # We replaced our character and its rectangle.

    # Key Input

    # 1. way

    # keys = pygame.key.get_pressed() # returns all the buttons and current state.
    # if keys[pygame.K_SPACE]: # If the player hits the space button, it will return 1.

    #     print("jump")

    # Mouse operations.

    mouse_pos = pygame.mouse.get_pos() # It gets the mouse position.

    pygame.display.update()
    clock.tick(60) # We adjusted FPS. This code will control the game not to run so fast(more than 60 FPS)
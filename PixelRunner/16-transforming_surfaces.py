# how to rotate or scale etc surface.
# We have different scale methods in pygame
# pygame.transform.scale/rotozoom/scale2x/smoothscale

"""
if game_active: # We draw everything
    current game
else: # draws something else
    game_over
"""

import pygame
from sys import exit

def display_score(): # We are creating a func that will get the time after ve started the game.

    current_time = int(pygame.time.get_ticks()/1000) - start_time # It gets current time.
    score_surf = test_font.render(f"Score: {current_time}",False,(64,64,64)) # we have created the score surface. It needs a string value so we convert it to str.
    score_rect = score_surf.get_rect(center= (400,50))
    screen.blit(score_surf,score_rect)
    return current_time # We are returning current time to show the score after the game finishes

    

pygame.init() # Starts pygame and loads all of the stuffs
screen = pygame.display.set_mode((800,400)) # Creating a screen
pygame.display.set_caption("Runner") # Setting the caption of the game.
clock = pygame.time.Clock() # We have created a clock to adjust FPS
test_font = pygame.font.Font(r'ClearCode\font\Pixeltype.ttf',50) # We have created a font object fot texts. (first parameter is font type and the second is font size). We have imported our custom font with its folder.
game_active = False # We have created a game statement variable. We made it False to see intro screen at first.
start_time = 0 # We have created a starting time
score = 0

sky_surface = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/Pygame/ClearCode/graphics/Sky.png").convert() # We have imported an image(change the slashes) We are converting the images to use them easily in pygame
ground_surface = pygame.image.load("ClearCode\graphics\ground.png").convert() # We imported our ground. We are converting the images to use them easily in pygame

# score_surf = test_font.render("My Game", False, (64,64,64)) # We created a text surface. render takes 3 argument (1. Text, 2. AA(anti alise),3. color) (anti alise will make your text's edges smooth. So if you dont use any pixel font you should use it.) (red,green,blue)
# score_rect = score_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load("ClearCode\graphics\snail\snail1.png").convert_alpha() # We created a snail surface. We are converting the images to use them easily in pygame
snail_rect = snail_surface.get_rect(bottomright = (600,300)) # We have created a rectangle around snail.

player_surf = pygame.image.load('ClearCode\graphics\Player\player_walk_1.png').convert_alpha() # We created a player surface. And converted it.
player_rect = player_surf.get_rect(midbottom = (80,300)) # get_rect() method gets the plater surface and draws aa rectangle around it. And adjusted its position. rectangle's parametre is the point of drawing.
player_gravity = 0 # We have created player's gravity.

# Intro Screen
player_stand = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/Pygame/ClearCode/graphics/Player/player_stand.png").convert_alpha() # We are loading our image and converting it to alpha.
# player_stand = pygame.transform.scale(player_stand,(200,400)) # We scaled the image (surface, sizes)
# player_stand = pygame.transform.scale(player_stand,(200,400)) # We scaled the image (surface)
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) # We scaled the image (surface, angle, scale) angle is the rotation
player_stand_rect = player_stand.get_rect(center=(400,200)) # We created a player_stand rect

game_name = test_font.render("Pixel Runner",False,(111,196,169)) # we have created the title surface. 
game_name_rect = game_name.get_rect(center= (400,70)) # and its rect

game_message = test_font.render("Press space to start the game...",False,(111,196,169)) # we have created the game message surface.
game_message_rect = game_message.get_rect(center= (400,350)) # and its rect

while True: # It will run the game forever.

    for event in pygame.event.get(): # Every event that player can do in a for loop
        if event.type == pygame.QUIT: # If player quit the game.
            pygame.quit() # Quit the game.
            exit() # This method will break the loop bcs we can't run other codes after we close the game.
        
        if game_active: # If the game is running
            if event.type == pygame.MOUSEBUTTONDOWN: # We are checking if we clicked the mouse button.

                if player_rect.collidepoint(event.pos): # And also if the mouse collides with the player.
                    
                    if player_rect.bottom == 300: # Player can only jump if the player touches the ground.
                        player_gravity = -20 # we set player_gravity to -20

            # Keyboard input

            if event.type == pygame.KEYDOWN: # We check if one of the button of the keyboard is pushed down.
                if event.key == pygame.K_SPACE: # If we are pushing the space button.
                    if player_rect.bottom == 300: # Player can only jump if the player touches the ground.
                        player_gravity = -20 # When we hit the space button player_gravity will be -20
        
        else: # If the game_active = False
            if event.type == pygame.KEYDOWN: # We check if one of the button of the keyboard is pushed down.
                if event.key == pygame.K_SPACE: # If we are pushing the space button.
                    game_active = True # Set game_active to True
                    snail_rect.left = 800 # And reposition the snail position.
                    start_time = int(pygame.time.get_ticks()/1000) # We are setting the starting time to pygame.get_ticks()

        # if event.type == pygame.KEYUP: # We check if we release one of the button of the keyboard.
        #     print("key up")

    if game_active: # If the game is active

        screen.blit(sky_surface, (0,0)) # We replaced it in our display surface 
        screen.blit(ground_surface, (0,300)) # We replaced our ground.

        # Drawing a line:

        # pygame.draw.line(screen, "Gold", (0,0), pygame.mouse.get_pos(), 10)

        # Drawing a circle:

        # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100)) # We have created a new rect inside the method and drawed a circle.

        # Score's background color:

        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect,6) # We are drawing something with draw method. Then we specify what kind of thing we draw.
        # # rect(where are we drawing, what is the colr, which rect, line width, border radius(round border.))
        # screen.blit(score_surf, score_rect) # We have replaced our text and rectangle.
        
        score = display_score() # display_score() returns current_time and it is our score.

        snail_rect.x -= 4 # We make our char move left.

        if snail_rect.right <= 0: # If the char's rectangle's right side is below zero which means our char has left the screen, we can reset its rectangle's left position to 800 which is the width of our screen.

            snail_rect.left = 800

        screen.blit(snail_surface, snail_rect) # We replaced our snail.
        # player_rect.left += 1 # We can make our character move right with rectangle.
        # print(player_rect) # We can measure something with this code.

        # Player
        player_gravity += 1 # We are increasing the gravity every cycle.
        player_rect.y += player_gravity

        # Floor Operations

        if player_rect.bottom >= 300: # If the player's bottom rect is above or equal to 300
            player_rect.bottom = 300 # We set its bottom rect to 300

        # collisions

        if snail_rect.colliderect(player_rect): # If the player collides with snail
            game_active = False # We setted game_active = False and stopped everything

        screen.blit(player_surf, player_rect) # We replaced our character and its rectangle.

        # Key Input

        # 1. way

        # keys = pygame.key.get_pressed() # returns all the buttons and current state.
        # if keys[pygame.K_SPACE]: # If the player hits the space button, it will return 1.

        #     print("jump")

        # Mouse operations.

        # mouse_pos = pygame.mouse.get_pos() # It gets the mouse position.

    else: # If the game_active = False (we collided with snail), the screen wil bee covered with yellow
        screen.fill((94,129,162)) # We filled the screen
        screen.blit(player_stand,player_stand_rect) # We replaced our image

        score_message = test_font.render(f'Your Score: {score}',False,(111,196,169)) # we crated our score surface
        score_message_rect = score_message.get_rect(center=(400,330)) # and its rect

        screen.blit(game_name,game_name_rect) # we show it in intro part

        if score == 0: # If we are starting the game our score is 0 we wont see our score.

            screen.blit(game_message,game_message_rect) # we show it in intro part.

        else: # If our score is different from zero, which means we played the game, we can see our score.
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60) # We adjusted FPS. This code will control the game not to run so fast(more than 60 FPS)
# We create our new custom event (obstacle_timer)
# everytime the timer triggers we add a new rect to list
# We move every rectangle in that list to the left on every frame
# We delete rect if they are too far left

"""
if game_active: # We draw everything
    current game
else: # draws something else
    game_over
"""

import pygame
from sys import exit
from random import randint

def display_score(): # We are creating a func that will get the time after ve started the game.

    current_time = int(pygame.time.get_ticks()/1000) - start_time # It gets current time.
    score_surf = test_font.render(f"Score: {current_time}",False,(64,64,64)) # we have created the score surface. It needs a string value so we convert it to str.
    score_rect = score_surf.get_rect(center= (400,50))
    screen.blit(score_surf,score_rect)
    return current_time # We are returning current time to show the score after the game finishes

def obstacle_movement(obstacle_list): # We are creating a func which moves the obstacles.

    if obstacle_list: # If python finds an empty list is going to evaluate that to false.
        for obstacle_rect in obstacle_list: # for every rect in the list
            obstacle_rect.x -= 5 # We will move them to the left for every cycle of the game.

            if obstacle_rect.bottom == 300: # If rect's bottom pos is 300, which means it is a snail then draw a snail.
                screen.blit(snail_surface,obstacle_rect)
            else: # If bottom of the rect is different from 300 which means it is a fly then we draw fly.
                screen.blit(fly_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] # If the obstacle's x pos is greater than -100 we are copying it to a new list

        return obstacle_list # We need global variables so we are returning new list.

    else: # If the list is empty (at first)
        return [] # return empty list.

def collisions(player,obstacles):

    if obstacles: # these codes are local and we want to adjust the game_active to False. But we cant do it in the func so we are returning False if we collide with some rect.
        for obstacle_rect in obstacles:
            if player_rect.colliderect(obstacle_rect):
                return False # If there is a collision return Flase.
    return True # If there is no collision return True


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

# Obstacles
snail_surface = pygame.image.load("ClearCode\graphics\snail\snail1.png").convert_alpha() # We created a snail surface. We are converting the images to use them easily in pygame

fly_surf = pygame.image.load("ClearCode\graphics\Fly\Fly1.png").convert_alpha() # We created our fly's surface. # We dont need to create a rect here. We will create it in the func.

obstacle_rect_list = [] # We have created our list.

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

# Timer

obstacle_timer = pygame.USEREVENT + 1 # We are adding our custom event and plus 1.
pygame.time.set_timer(obstacle_timer,1500) # set_timer takes 2 argument. First one is what do you want to trigger and second one is how often you want to trigger


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
                    start_time = int(pygame.time.get_ticks()/1000) # We are setting the starting time to pygame.get_ticks()

        if event.type == obstacle_timer and game_active: # If our event is obstacle_timer which is triggered every 900 ms and game is active.
            if randint(0,2): # It will give us 0 or 1. If true it will give us a snail. If it is false it will give us a fly
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300))) # Every time the timer triggers we are adding a new snail rect to the list with random coordinates.
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))

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

        # We disabled snail movement bcs we will change it.
        # snail_rect.x -= 4 # We make our char move left.

        # if snail_rect.right <= 0: # If the char's rectangle's right side is below zero which means our char has left the screen, we can reset its rectangle's left position to 800 which is the width of our screen.

        #     snail_rect.left = 800

        # screen.blit(snail_surface, snail_rect) # We replaced our snail.
        # player_rect.left += 1 # We can make our character move right with rectangle.
        # print(player_rect) # We can measure something with this code.

        # Player
        player_gravity += 1 # We are increasing the gravity every cycle.
        player_rect.y += player_gravity

        # Floor Operations

        if player_rect.bottom >= 300: # If the player's bottom rect is above or equal to 300
            player_rect.bottom = 300 # We set its bottom rect to 300

        # collisions we have commented it bcs now we dont need it

        # if snail_rect.colliderect(player_rect): # If the player collides with snail
        #     game_active = False # We setted game_active = False and stopped everything

        # new collisions

        game_active = collisions(player_rect,obstacle_rect_list)

        screen.blit(player_surf, player_rect) # We replaced our character and its rectangle.

        # Obstacle movement

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

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

        obstacle_rect_list.clear() # We are clearing the list and remove all the enemies not to collide with again and again with the enemies.
        player_rect.midbottom = (80,300) # We are drawing our character at the bottom bcs if the jump at the end of the game we can start from the ground again.
        player_gravity = 0 # To make the game cleaner.

        score_message = test_font.render(f'Your Score: {score}',False,(111,196,169)) # we crated our score surface
        score_message_rect = score_message.get_rect(center=(400,330)) # and its rect

        screen.blit(game_name,game_name_rect) # we show it in intro part

        if score == 0: # If we are starting the game our score is 0 we wont see our score.

            screen.blit(game_message,game_message_rect) # we show it in intro part.

        else: # If our score is different from zero, which means we played the game, we can see our score.
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60) # We adjusted FPS. This code will control the game not to run so fast(more than 60 FPS)
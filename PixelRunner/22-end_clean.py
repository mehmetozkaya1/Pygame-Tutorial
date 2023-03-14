import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite): # It has a Sprite inheritance.

    def __init__(self):
        super().__init__() # We are initilazing the sprite class inside this function.
        
        player_walk1 = pygame.image.load('C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Player/player_walk_1.png').convert_alpha() # We loaded our images.
        player_walk2 = pygame.image.load('C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Player/player_walk_2.png').convert_alpha() # We loaded our images.
        self.player_walk = [player_walk1,player_walk2] # We created a list from these 2 pngs.
        self.player_index = 0 # The index that help us to choose the png.
        self.player_jump = pygame.image.load('C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Player/jump.png').convert_alpha() # And we loaded our jump animations.
        
        self.image = self.player_walk[self.player_index] # We are choosing one of the image from the list with the player index.
        self.rect = self.image.get_rect(midbottom = (90,300)) # We have created the image's rectangle
        self.gravity = 0 # We assigned the player's gravity.

        self.jump_sound= pygame.mixer.Sound("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/audio/jump.mp3")
        self.jump_sound.set_volume(0.8) # We are setting the volume 0 = Mute 1 = Loudest Sound

    def player_input(self):
        keys = pygame.key.get_pressed() # All the possible key inputs in keyboard.
        if keys[pygame.K_SPACE] and self.rect.bottom >=300: # If the key is space and the player rect is more than 300 we can jump.
            self.gravity = -20 # Assign the player's gravity to -20
            self.jump_sound.play()

    def apply_gravity(self): # We are applying the gravity
        self.gravity += 1 # We are increasing the gravity +1
        self.rect.y += self.gravity # and changes the rect of the player.

        if self.rect.bottom >= 300: # We are controlling if the player is getting out of the screen
            self.rect.bottom = 300
        
    def animation_state(self): # This method wil allow us to control the player's animation.
       
        if self.rect.bottom < 300: # if player's rect is smaller than 300, it means the player is jumping
            # jump
            self.image = self.player_jump # player's image is should be self.player_jump image
        else: # which means it is walking
            #walk
            self.player_index += 0.1 # it slowly increases and when the player index == 1 it will show walk2.
            if self.player_index >= len(self.player_walk): # we have 0,1 indexes so it cant be higher.
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)] # It regularly shows the images, which creates the animation.
    
    def update(self): # This update method automatically call these 2 methods.
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):

    def __init__(self,type): # We are also creating a type var because we want to declare if it is a snail or a fly.
        super().__init__() # We are initializing sprite class in this class.
        
        if type == "fly":
            fly_1 = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Fly/fly1.png").convert_alpha() # We created our fly's surface. # We dont need to create a rect here. We will create it in the func.
            fly_2 = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Fly/fly2.png").convert_alpha() # We created our fly's surface. # We dont need to create a rect here. We will create it in the func.
            self.frames = [fly_1,fly_2]
            y_pos = 210 # We are also declaring the y pos of the snail bcs it has to be higher.

        else: # Which means it is a snail.
            snail_1 = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/snail/snail1.png").convert_alpha() # We created a snail surface. We are converting the images to use them easily in pygame
            snail_2 = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/snail/snail2.png").convert_alpha() # We created a snail surface. We are converting the images to use them easily in pygame
            self.frames = [snail_1,snail_2]
            y_pos = 300 # Snail's y pos is should be 300

        self.animation_index = 0 # We have created a animation index for both of the obstacles.

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

    def animation_state(self): # obstacles animation function
        self.animation_index += 0.1 # We are continiously increasing the index

        if self.animation_index >= len(self.frames): # if the index is higher than the len(self.frames) we are reassign is to 0
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)] # and the image is repeatedly changing by the change of the animation index.
    
    def obstacle_movement(self): # The func which moves the obstacles left.
        self.rect.x -= 6
    
    def destroy(self): # This method will delete the obstacle sprite if it is too left.
        if self.rect.x <= -100:
            self.kill() # This kill method will delete the obstacle sprite if the x pos of the rect is lower than -100

    def update(self): # We have creted our update func
        self.animation_state()
        self.obstacle_movement()
        self.destroy()

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
                screen.blit(snail_surf,obstacle_rect)
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

def collision_sprite():
    # It will return a list, if there is not a collision it will return an empty list.
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False): # We are calling the player sprite inside the player group, and the obstacle group, if the third parameter is True, everytime our player collides with obstacles, that obstacle will be deleted, if it is False the obstacle wouldn't be deleted.
    # If the list is not empty, it will return True:
        obstacle_group.empty() # And we are cleaning the obstacle group not to crash the game
        return False
    else: # If the list is empty
        return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300: # if it is smaller than 300, the player is jumping
        # jump
        player_surf = player_jump
    else:
        #walk
        player_index += 0.1 # it slowly increases and when the player index == 1 it will show walk2.
        if player_index >= len(player_walk): # we have 0,1 indexes so it cant be higher.
            player_index = 0
        player_surf = player_walk[int(player_index)]
    # play walking animation if the player is on floor
    # display the jump surface when player is not on the floor

pygame.init() # Starts pygame and loads all of the stuffs
screen = pygame.display.set_mode((800,400)) # Creating a screen
pygame.display.set_caption("Runner") # Setting the caption of the game.
clock = pygame.time.Clock() # We have created a clock to adjust FPS
test_font = pygame.font.Font(r'ClearCode\font\Pixeltype.ttf',50) # We have created a font object fot texts. (first parameter is font type and the second is font size). We have imported our custom font with its folder.
game_active = False # We have created a game statement variable. We made it False to see intro screen at first.
start_time = 0 # We have created a starting time
score = 0
bg_music = pygame.mixer.Sound("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/audio/music.wav")
bg_music.play(loops=-1) # -1 means play this music forever.

# We are creating sprite groups.
# The player and the obstacles have to be in different groups bcs we want to check if they collide.

# Groups
# Player Group
player = pygame.sprite.GroupSingle() # We created a single group for the player.
player.add(Player()) # And we are adding a Player instance into this single group

# Obstacle Group
# We will add obstacles to this group when the timer ticks. (below)

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Sky.png").convert() # We have imported an image(change the slashes) We are converting the images to use them easily in pygame
ground_surface = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/ground.png").convert() # We imported our ground. We are converting the images to use them easily in pygame

# Obstacles

# Snail
snail_frame_1 = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/snail/snail1.png").convert_alpha() # We created a snail surface. We are converting the images to use them easily in pygame
snail_frame_2 = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/snail/snail2.png").convert_alpha() # We created a snail surface. We are converting the images to use them easily in pygame
snail_frames = [snail_frame_1,snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

# Fly
fly_frame_1 = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Fly/fly1.png").convert_alpha() # We created our fly's surface. # We dont need to create a rect here. We will create it in the func.
fly_frame_2 = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Fly/fly2.png").convert_alpha() # We created our fly's surface. # We dont need to create a rect here. We will create it in the func.
fly_frames = [fly_frame_1,fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = [] # We have created our list.

player_walk1 = pygame.image.load('C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Player/player_walk_1.png').convert_alpha() # We loaded our images.
player_walk2 = pygame.image.load('C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Player/player_walk_2.png').convert_alpha() # We loaded our images.
player_walk = [player_walk1,player_walk2] # We created a list from these 2 pngs.
player_index = 0 # The index that help us to choose the png.
player_jump = pygame.image.load('C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Player/jump.png').convert_alpha() # And we loaded our jump animations.
        

player_surf = player_walk[player_index] # We selected with the index one or two walking png.
player_rect = player_surf.get_rect(midbottom = (80,300)) # get_rect() method gets the plater surface and draws aa rectangle around it. And adjusted its position. rectangle's parametre is the point of drawing.
player_gravity = 0 # We have created player's gravity.

# Intro Screen
player_stand = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/SoftwareLessons/Apps/Pygame/ClearCode/graphics/Player/player_stand.png").convert_alpha() # We are loading our image and converting it to alpha.

player_stand = pygame.transform.rotozoom(player_stand, 0, 2) # We scaled the image (surface, angle, scale) angle is the rotation
player_stand_rect = player_stand.get_rect(center=(400,200)) # We created a player_stand rect

game_name = test_font.render("Pixel Runner",False,(111,196,169)) # we have created the title surface. 
game_name_rect = game_name.get_rect(center= (400,70)) # and its rect

game_message = test_font.render("Press space to start the game...",False,(111,196,169)) # we have created the game message surface.
game_message_rect = game_message.get_rect(center= (400,350)) # and its rect

# Timer

obstacle_timer = pygame.USEREVENT + 1 # We are adding our custom event and plus 1.
pygame.time.set_timer(obstacle_timer,1500) # set_timer takes 2 argument. First one is what do you want to trigger and second one is how often you want to trigger

snail_animation_timer = pygame.USEREVENT + 2 # We crated a custom event for the snail animation
pygame.time.set_timer(snail_animation_timer,500) # It is 500 ms

fly_animation_timer = pygame.USEREVENT + 3 # We created a custom event for the fly animation
pygame.time.set_timer(fly_animation_timer,200) # It is 200 ms

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
        
        if game_active: # If the game is active, I check all timers at the same time.
            if event.type == obstacle_timer: # If our event is obstacle_timer which is triggered every 900 ms and game is active.
                obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail']))) # We are choosing one of them but mostly snail.
                
            if event.type == snail_animation_timer: # We adjusted the timer every 500 ms.
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer: # We adjusted the timer every 500 ms.
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active: # If the game is active
        
        screen.blit(sky_surface, (0,0)) # We replaced it in our display surface 
        screen.blit(ground_surface, (0,300)) # We replaced our ground.
        
        score = display_score() # display_score() returns current_time and it is our score.

        player.draw(screen) # We are drawing our character in the screen.
        player.update() # We draw our character and now we are updating its pos or sth.

        obstacle_group.draw(screen)
        obstacle_group.update()

        # new collisions

        game_active = collision_sprite() # The method which returns False if we collides with an obstacle.

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
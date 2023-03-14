# We can create endless regular surfaces and make them visiable.
# Regular surfaces only be displayed when we reached them.

import pygame
from sys import exit

pygame.init() # Starts pygame and loads all of the stuffs
screen = pygame.display.set_mode((800,400)) # Creating a screen
pygame.display.set_caption("Runner") # Setting the caption of the game.
clock = pygame.time.Clock() # We have created a clock to adjust FPS
test_font = pygame.font.Font(r'ClearCode\font\Pixeltype.ttf',50) # We have created a font object fot texts. (first parameter is font type and the second is font size). We have imported our custom font with its folder.

sky_surface = pygame.image.load("C:/Users/PANTHER/OneDrive/Masaüstü/Pygame/ClearCode/graphics/Sky.png") # We have imported an image(change the slashes)
ground_surface = pygame.image.load("ClearCode\graphics\ground.png") # We imported our ground
text_surface = test_font.render("My Game", False, "Black") # We created a text surface. render takes 3 argument (1. Text, 2. AA(anti alise),3. color) (anti alise will make your text's edges smooth. So if you dont use any pixel font you should use it.)

while True: # It will run the game forever.

    for event in pygame.event.get(): # Every event that player can do in a for loop
        if event.type == pygame.QUIT: # If player quit the game.
            pygame.quit() # Quit the game.
            exit() # This method will break the loop bcs we can't run other codes after we close the game.
    
    screen.blit(sky_surface, (0,0)) # We replaced it in our display surface 
    screen.blit(ground_surface, (0,300)) # We replaced our ground.
    screen.blit(text_surface, (300,50)) # We have replaced our text.

    pygame.display.update()
    clock.tick(60) # We adjusted FPS. This code will control the game not to run so fast(more than 60 FPS)
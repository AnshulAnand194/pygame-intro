import pygame
from sys import exit

pygame.init() # strarting the engine. Just turn the key not neep to worry about the gears
screen = pygame.display.set_mode((800, 400)) # creating display surface


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    pygame.display.update() # update screen
    # if run now wont be able to close the window as it is not checking for user inputs. closing is also a user input

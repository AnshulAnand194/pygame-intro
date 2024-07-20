import pygame
from sys import exit

pygame.init() # strarting the engine. Just turn the key not neep to worry about the gears
screen = pygame.display.set_mode((800, 400)) # creating display surface
pygame.display.set_caption("Runner") # set window title
clock = pygame.time.Clock() # create clock object
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

 # test_surface = pygame.Surface((100, 200)) # create regular test surface

sky_surface = pygame.image.load('./graphics/Sky.png')
ground_surface = pygame.image.load('./graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init
            exit()
    # draw all our elements
    # update everything
    screen.blit(sky_surface,(0, 0)) # block image transfer / 1 surface on top of another
    screen.blit(ground_surface,(0, 300))
    screen.blit(text_surface,(300, 50))

    pygame.display.update() # update screen
    # if run now wont be able to close the window as it is not checking for user inputs. closing is also a user input
    clock.tick(60)
import pygame
from sys import exit

pygame.init() # strarting the engine. Just turn the key not neep to worry about the gears
screen = pygame.display.set_mode((800, 400)) # creating display surface
pygame.display.set_caption("Runner") # set window title
clock = pygame.time.Clock() # create clock object
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

 # test_surface = pygame.Surface((100, 200)) # create regular test surface

sky_surface = pygame.image.load('./graphics/Sky.png').convert()

ground_surface = pygame.image.load('./graphics/ground.png').convert()
ground_rect = ground_surface.get_rect(topleft = (0, 300))

text_surface = test_font.render('My Game', False, 'Black').convert()

snail_surface = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (600, 300))

player_surf = pygame.image.load('./graphics/Player/player_walk_1.png')
player_rect = player_surf.get_rect(bottomleft = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init
            exit()
    # draw all our elements
    # update everything
    screen.blit(sky_surface,(0, 0)) # block image transfer / 1 surface on top of another
    screen.blit(ground_surface,ground_rect)
    screen.blit(text_surface,(300, 50))
    snail_rect.left -= 4 
    if snail_rect.left < -100: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)
    
    player_rect.left += 1
    screen.blit(player_surf, player_rect)

    pygame.display.update() # update screen
    # if run now wont be able to close the window as it is not checking for user inputs. closing is also a user input
    clock.tick(60)
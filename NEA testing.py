import pygame
from sys import exit


class player:
    def __init__(self):
        self.pstartx = 350
        self.pstarty = 250
        self.pwidth = 50
        self.pheight = 50 


pygame.init()
#Building the screen and the tab name
width = 1200
height = 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Test")

clock = pygame.time.Clock()

#crating a basis font and text format
text_format = pygame.font.Font(None, 50)

p1 = player()
p1 = pygame.Rect((p1.pstartx,p1.pstarty,p1.pwidth,p1.pheight))

#creating a text surface for text
text_surface = text_format.render("My game", False, (0,0,255))


screen_rect = screen.get_rect()

while True:
    #builds the screen colour
    screen.fill((255,0,0))

    #builds the character
    pygame.draw.rect(screen, (0,0,255), p1)

    #Registering the key inputs for movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        p1.move_ip(-5,0)
    elif key[pygame.K_RIGHT]:
        p1.move_ip(5,0)
    elif key[pygame.K_UP]:
        p1.move_ip(0,-5)
    elif key[pygame.K_DOWN]:
        p1.move_ip(0,5)
    p1.clamp_ip(screen_rect)
    
    #Quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #puts the text surface on the screen
    screen.blit(text_surface,(525,50))

    pygame.display.update()
    clock.tick(60) 
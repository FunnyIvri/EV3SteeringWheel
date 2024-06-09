import pygame

root = pygame.display.set_mode((800,800))
pygame.init()
run = True
print(pygame.font.get_fonts())
while run:
    font1 = pygame.font.SysFont("arial", 100)
    text1 = font1.render("WAITING", True, (255,0,0))
    textrect = text1.get_rect()
    textrect.center = (400,400)
    root.blit(text1,textrect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pygame.display.update()
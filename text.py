import pygame


class Textcreator:
    def __init__(self, text: str, size: int, pos: (int, int), display_surface: pygame.display, color=(255, 255, 255),
                 font="freesanbold.ttf"):
        self.text = str(text)
        self.size = size
        self.pos = pos
        self.display_surface = display_surface
        self.color = color
        self.font = font

    def createText(self):
        # initializing pygame
        pygame.font.init()

        # check whether font is initialized
        # or not
        pygame.font.get_init()

        font1 = pygame.font.SysFont(self.font, self.size)
        text1 = font1.render(self.text, True, self.color)

        textRect1 = text1.get_rect()
        textRect1.center = self.pos

        self.display_surface.blit(text1, textRect1)

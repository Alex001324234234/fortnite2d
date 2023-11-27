import pygame

class Objects:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.is_looted = False

    def update(self):
       self.draw()
       keys= pygame.key.get_pressed()
       if self.rect.colliderect(self.game.player.rect) and keys[pygame.K_e]:
           self.is_looted = True


    def draw(self):
        pygame.draw.rect(self.game.window, "yellow", self.rect)

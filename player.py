import pygame 

class Player:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.surface = game.window
        self.rect = pygame.Rect(self.x, self.y, 32 , 32)
       

    def update(self):
       self.rect = pygame.Rect(self.x, self.y, 32, 32)
       self.movement()
       self.draw()


   
    def draw(self):
       pygame.draw.rect(self.surface, "red", (self.x , self.y, 32 ,32 ))

    def movement(self):
        keys= pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
           self.speed= 150
        else:
           self.speed= 100

        if keys[pygame.K_w]:
           self.y -= self.speed * self.game.delta_time

        elif keys[pygame.K_s]:
           self.y += self.speed * self.game.delta_time

        if keys[pygame.K_a]:
           self.x -= self.speed * self.game.delta_time

        elif keys[pygame.K_d]:
           self.x += self.speed * self.game.delta_time


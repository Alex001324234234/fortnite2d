import pygame
import objects
import player


class Game:
    def __init__(self):
        pygame.init()
        self.window_with= 800
        self.widnow_hight=600
        self.window = pygame.display.set_mode((self.window_with,self.widnow_hight))
        pygame.display.set_caption("für Fortnite")
        self.clock= pygame.time.Clock()

        self.player = player.Player(self, 32 , 32)
        self.objects = [objects.Objects(self, 150 ,150),
                        objects.Objects(self, 350 ,150),
                        objects.Objects(self, 150 ,250)
                        ]
        self.run()

    def run(self):
       running = True
       while running:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False 
               elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                   running = False

           self.delta_time = self.clock.tick(60) / 1000
           self.window.fill((25,25,25))
           self.player.update()
           for objects in self.objects:
               objects.update()
               if objects.is_looted :
                   self.objects.remove(objects)
           pygame.display.update()

    pygame.quit()



game = Game()
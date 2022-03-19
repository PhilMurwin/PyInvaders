import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,screen_height):
        super().__init__()
        laser_width = 4
        laser_height = 20
        self.laser_speed = speed
        self.image = pygame.Surface((laser_width,laser_height))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)
        self.height_y_constraint = screen_height

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.y += self.laser_speed
        self.destroy()
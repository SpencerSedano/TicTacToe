import pygame, sys


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,800))
second_surface = pygame.Surface([400,400])
second_surface.fill((255,255,255))
print(second_surface.get_rect())
first_line = pygame.draw.line(second_surface, (0,0,0), [0,133.3], [400,133.3])
second_line = pygame.draw.line(second_surface, (0,0,0), [0,266.6], [400,266.6])
third_line = pygame.draw.line(second_surface, (0,0,0), [133.3,0], [133.3, 400])
fourth_line = pygame.draw.line(second_surface, (0,0,0), [266.6,0], [266.6, 400])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    screen.blit(second_surface, (200,200))
    pygame.display.flip()
    clock.tick(60)
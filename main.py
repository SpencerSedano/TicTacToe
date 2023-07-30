import pygame, sys


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((400,400))
second_surface = pygame.Surface([400,400])
second_surface.fill((255,255,255))
print(second_surface.get_rect())
first_line = pygame.draw.line(second_surface, (0,0,0), [0,133.3], [400,133.3])
second_line = pygame.draw.line(second_surface, (0,0,0), [0,266.6], [400,266.6])
third_line = pygame.draw.line(second_surface, (0,0,0), [133.3,0], [133.3, 400])
fourth_line = pygame.draw.line(second_surface, (0,0,0), [266.6,0], [266.6, 400])

def draw_x():
        pygame.draw.line(second_surface, (50,205,50), (pos), (pos_x * 1.2, pos_y * 2), 2)
        pygame.draw.line(second_surface, (50,205,50), (pos_x * 2, pos_y), (pos_x, pos_y * 2), 2)

while True:
    pos = pygame.mouse.get_pos()
    pos_x = pos[0]
    pos_y = pos[1]
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Clicked")
            print(pos)
            print(pos[0])
            print(pos[1] / 2)
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                circle = pygame.draw.circle(second_surface, (50,205,50), pos, (40), 1 > 0)
            if mouse_presses[2]:
                draw_x()
                
        if event.type == pygame.MOUSEBUTTONUP:
            print("Released")
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    screen.blit(second_surface, (0,0))
    pygame.display.flip()
    clock.tick(60)
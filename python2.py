import sys
import pygame

color_rect = input()
color_circle = input()
pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
start_circle = 0
draw = False
start = 0
draw_circle = False
screen2 = pygame.Surface(screen.get_size())
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            draw = True
            start = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if draw:
                position = event.pos
                width = position[0] - start[0]
                height = position[1] - start[1]
                pygame.draw.rect(screen, color_rect, (start[0], start[1], width, height))
                screen2.blit(screen, (0, 0))
                screen.fill((0, 0, 0))
                screen.blit(screen2, (0, 0))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            draw = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            draw_circle = True
            start_circle = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if draw_circle:
                position = event.pos
                radius = position[0] - start_circle[0] + position[1] - start_circle[1]
                pygame.draw.circle(screen, color_circle, (start_circle[0], start_circle[1]), radius)
                screen2.blit(screen, (0, 0))
                screen.fill((0, 0, 0))
                screen.blit(screen2, (0, 0))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            draw_circle = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                screen.fill((0, 0, 0))

    pygame.display.update()
    clock.tick(30)

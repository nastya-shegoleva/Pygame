import pygame
import random

size = W, H = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
# Создаем второй холст
screen2 = pygame.Surface(screen.get_size())
x1 = W // 2
y1 = H // 2
drawing = False  # режим рисования выключен
v = random.randint(5, 60)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                drawing = True
                pygame.time.delay(v)
        if event.type == pygame.KEYUP:
            screen2.blit(screen, (0, 0))
            drawing = False
    # Рисуем на экране сохраненное на втором холсте
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing:
        pygame.draw.circle(screen, (0, 0, 255), (x1, y1), 30)
        x1 = random.random() * W % W
        y1 = random.random() * H % H
        clock.tick(v)
    pygame.display.flip()
pygame.quit()

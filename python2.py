import pygame


color_rect = input()
color_circle = input()
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Cube:
    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.square = pygame.Rect(self.x - 25, self.y - 25, 50, 50)

    def draw_rect(self):
        self.color = (100, 0, 255)
        pygame.draw.rect(screen, color_rect, self.square)


class Circle():
    def update(self):
        self.x, self.y = pygame.mouse.get_pos()

    def draw_circle(self):
        pygame.draw.circle(screen, color_circle, (self.x, self.y), 20)

def main():
    run = True
    cubeList = []
    circle_lst = []
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cube = Cube()
                cubeList.append(cube)
                cube.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    circle = Circle()
                    circle_lst.append(circle)
                    circle.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    screen.fill((0, 0, 255))
                    circle_lst.clear()
                    cubeList.clear()
        clock.tick(60)
        screen.fill((0, 0, 255))
        for x in cubeList:
            x.draw_rect()
        for x in circle_lst:
            x.draw_circle()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

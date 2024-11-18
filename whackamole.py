import pygame
import random
mole_image = "mole.png"

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x = 10000000
        y = 10000000
        newX = 0
        newY = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                

            screen.fill("light green")
            #draw grid
            for i in range(1, 20):
                pygame.draw.line(screen, "black", (i*32, 0),(i*32, 512))
                pygame.draw.line(screen, "black", (0, i*32), (640, i*32))

            screen.blit(mole_image, mole_image.get_rect(topleft=(newX*32, newY*32)))
            if newX == x//32 and newY == y//32:
                newX = random.randrange(0, 640) //32
                newY = random.randrange(0, 512) //32
                continue


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

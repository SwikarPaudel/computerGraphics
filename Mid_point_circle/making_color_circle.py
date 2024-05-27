import pygame
import sys

# Initialize Pygame
pygame.init()

#Set up the display
WIDTH,HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
def main():
    while True:
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        #Clear the screen
        screen.fill(BLACK)

        pygame.draw.circle(screen, GOLD,(500,400), 50)
       


        #Update the dislay
        pygame.display.flip()
       

if __name__ == "__main__":
    main()

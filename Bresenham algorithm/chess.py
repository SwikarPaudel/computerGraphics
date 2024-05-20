#Chess using bresenham algorithm

import pygame
import sys

# Initialize Pygame
pygame.init()

#Set up the display
WIDTH,HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))

# Function to draw a line using Bresenham algorithm
def draw_line_bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if(x2>x1):
        lx=1
    else:
        lx=-1
    if(y2>y1):
        ly=1
    else:
        ly=-1
    x=x1
    y=y1
    if(dx>dy):
        p=2*dy-dx
        while(x!=x2):
            if(p<0):
                x=x+lx
                y=y
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+2*dy-2*dx
            screen.set_at((x, y), WHITE)
    else:
        p=2*dx-dy
        while(y!=y2):
            if(p<0):
                x=x
                y=y+ly
                p=p+2*dx
            else:
                x=x+lx
                y=y+ly
                p=p+2*dx-2*dy
            screen.set_at((x, y), WHITE)

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        #Clear the screen
        screen.fill(BLACK)

        # Draw the chess board
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
                draw_rectangle(i * 100, j * 100, 100, 100, color)

        #Update the dislay
        pygame.display.flip()

if __name__ == "__main__":
    main()

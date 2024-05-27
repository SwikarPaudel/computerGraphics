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
GOLD = (255, 215, 0)

#Function to draw circle using mid point algorithm
def draw_circle(xc, yc, radius):
    x=0
    y=radius
    p=1-radius
    while x<=y:
        screen.set_at((x +xc, y+yc ), WHITE)
        screen.set_at((y +xc, x+yc ), WHITE)
        screen.set_at((y +xc, -x+yc ), WHITE)
        screen.set_at((x +xc, -y+yc ), WHITE)
        screen.set_at((-x +xc, -y+yc ), WHITE)
        screen.set_at((-y +xc, -x+yc ), WHITE)
        screen.set_at((-y +xc, x+yc ), WHITE)
        screen.set_at((-x +xc, y+yc ), WHITE)

        x=x+1
        if p<0:
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*x-2*y+1

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
            screen.set_at((x, y),GOLD)
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
            screen.set_at((x, y),GOLD)

        


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

        #draw circle using mid_point circle algorithm
        draw_circle(350,200,100)
        draw_circle(450,200,100)
        draw_circle(400,300,100)
        draw_circle(300,300,100)
        draw_circle(500,300,100)
        draw_circle(350,400,100)
        draw_circle(450,400,100)
        #draw_line_bresenham(300,300,500,300)
        draw_line_bresenham(350,400,450,400)
        draw_line_bresenham(350,200,450,200)
        draw_line_bresenham(300,300,350,400)
        draw_line_bresenham(300,300,350,200)
        draw_line_bresenham(450,200,500,300)
        draw_line_bresenham(450,400,500,300)


        #Update the dislay
        pygame.display.flip()
       

if __name__ == "__main__":
    main()

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
        #draw_circle(500,400,25)
        draw_circle(500,400,50)
        draw_circle(500,400,100)
        draw_circle(500,400,150)
        draw_circle(500,400,200)
        draw_circle(500,400,250)
        draw_circle(500,400,300)
        draw_circle(500,400,350)
        draw_circle(500,400,400)
        pygame.draw.circle(screen, GOLD,(500,400), 25)
        pygame.draw.circle(screen, GOLD,(550,400), 15)
        pygame.draw.circle(screen, GOLD,(560,320), 20)
        pygame.draw.circle(screen, GOLD,(460,255), 30)
        pygame.draw.circle(screen, GOLD,(325,300), 25)
        pygame.draw.circle(screen, GOLD,(250,400), 30)
        pygame.draw.circle(screen, GOLD,(225,520), 30)
        pygame.draw.circle(screen, GOLD,(300,680), 20)
        pygame.draw.circle(screen, GOLD,(350,770), 20)


        #Update the dislay
        pygame.display.flip()
       

if __name__ == "__main__":
    main()

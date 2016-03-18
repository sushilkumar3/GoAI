import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (20, 173, 224)

pygame.init()
# Set the width and height of the screen [width, height]
size = (760, 760)
screen = pygame.display.set_mode((size))  # , pygame.FULLSCREEN)
pygame.display.set_caption("GO!")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def trainerLines():
    for x in range(0, 950, 40):
        pygame.draw.line(screen, BLACK, [x, 0], [x, 950], 2)
    for y in range(0, 950, 40):
        pygame.draw.line(screen, BLACK, [0, y], [950, y], 2)


def drawCircle(x, y, colour):
        for i in range(1, len(blackX_list)):
            pygame.draw.circle(
                screen, BLACK, [blackX_list[i], blackY_list[i]], 15)

        for i in range(1, len(whiteX_list)):
            pygame.draw.circle(
                screen, WHITE, [whiteX_list[i], whiteY_list[i]], 15)


# vars
circle = False
blackX_list = []
blackY_list = []
whiteX_list = []
whiteY_list = []
colour = BLACK

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            circle = True

            if colour == BLACK:
                blackX_list.append(mouse_x)
                blackY_list.append(mouse_y)

            if colour == WHITE:
                whiteX_list.append(mouse_x)
                whiteY_list.append(mouse_y)

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    blackX_list = []
                    blackY_list = []
                    whiteX_list = []
                    whiteY_list = []
                if event.key == pygame.K_b:
                    colour = BLACK
                if event.key == pygame.K_w:
                    colour = WHITE

    pygame.mouse.set_visible(True)
    screen.fill(BLUE)

    if (circle is True):
        drawCircle(mouse_x, mouse_y, colour)

    trainerLines()
    pygame.display.flip()

    clock.tick(9999999999999999999999999999999999999999999999)

pygame.quit()

'''
sdfdsf
'''
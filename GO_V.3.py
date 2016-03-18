import pygame

red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
purple = (255,0,255)

unit=50
screen=pygame.display.set_mode((13*50,13*50))
done=False
clock=pygame.time.Clock()

grid=[] # where pieces are stored as integer values, blank spots are False
mode = 1 # determines player 

for i in range(13):
    grid.append([])
    for m in range(13):
        grid[i].append(False)

pygame.init()
while not done:
    screen.fill(red)
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            done=True
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_b: #black player
                mode = 1
            if e.key==pygame.K_w: #white player
                mode = 2
            if e.key==pygame.K_r: #reset
                for i in range(13):
                    grid.append([])
                    for m in range(13):
                        grid[i][m] = False
						
        elif e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            grid[int(pos[0]/unit)][int(pos[1]/unit)] = mode
    for i in range(len(grid)):
        for m in range(len(grid[i])):
            if grid[i][m] == 1:
                pygame.draw.rect(screen,black,[i*unit,m*unit,unit,unit],0)
            elif grid[i][m] == 2:
                pygame.draw.rect(screen,white,[i*unit,m*unit,unit,unit],0)
            pygame.draw.rect(screen,purple,[i*unit,m*unit,unit,unit],1)
    pygame.display.flip()
    clock.tick(300)
pygame.quit()
import pygame
import time
pygame.init()
screen=pygame.display.set_mode((305,305) )
pygame.display.set_caption("ball game")
# icon=pygame.image.load("ball.png")
# pygame.display.set_icon(icon)
r=True
x=25
y=25
while r:
     screen.fill((162, 132, 232))
     pygame.draw.circle(screen,(255,255,255),(x,y),25)
    #  screen.blit(ball,(x,y))
     pygame.display.update()
     for i in pygame.event.get():
        if i.type==pygame.QUIT:
            r=False
            pygame.quit()
        elif i.type==pygame.KEYDOWN:
            if i.key==pygame.K_RIGHT:
                x+=20
                if x>=280:
                   x=280
                   continue
            elif i.key==pygame.K_LEFT:
                x-=20
                if x<=25:
                    x=25
            elif i.key==pygame.K_DOWN:
                y+=20
                if y>=280:
                    y=280
            elif i.key==pygame.K_UP:
                y-=20
                if y<=25:
                    y=25
                   
               
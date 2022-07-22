import pygame
import random as rand

globalArea = (250,470)
globalPerim = (250,520)
activeBox = (250,0,0)
passiveBox = (0,0,0)

class Trapezoid: 
    def __init__(self, base1, base2, height, side):
        self.base1 = base1
        self.base2 = base2
        self.side = side
        self.height = height
        
    def trapArea(self):
        return (self.base1 + self.base2) * self.height * 0.5
    
    def trapPerim(self):
        return self.base1 + self.base2 + self.side + self.side
    
def question(scr):
    generate = rand.randint(1,2)
    if generate == 1:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawTrap(scr)
    if generate == 2:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawTrap(scr)

    
def drawTrap(scr):
    bigfont = pygame.font.SysFont('Corbel', 40)
    areaformula ='Area = h x 0.5 x (b1 + b2)'
    perimformula = 'Perimeter = b1 + b2 + 2l ' 
    
    base1 =rand.randint(1,10)
    base2 =rand.randint(1,10)
    if base2 == base1:
        base1 += 2
    side =rand.randint(1,10)
    height =rand.randint(1,10)
    
    #make help, new question, quit button
    helpbutton = pygame.draw.rect(scr, (100,100,100), [0, 0, 80 , 30],)
    help = bigfont.render('Help' , True , (0,0,0))
    scr.blit(help , (helpbutton.x+5,helpbutton.y))
    
    newbutton = pygame.draw.rect(scr, (0,255,0), [81, 0, 80 , 30],)
    new = bigfont.render('New' , True , (0,0,0))
    scr.blit(new , (newbutton.x+5,newbutton.y)) 
                 
    quitbutton = pygame.draw.rect(scr, (255,0,0), [720, 0, 80 , 30],)
    quit = bigfont.render('Quit' , True , (0,0,0))
    scr.blit(quit , (quitbutton.x+5,quitbutton.y))
    
    #if b1<b2 pizzahut if b1>b2 oppo else b2+=1
    dispB1 = bigfont.render(str(base1), True,(0,0,0))
    dispB2 = bigfont.render(str(base2), True,(0,0,0))
    dispSide = bigfont.render(str(side), True,(0,0,0))
    dispHeight = bigfont.render(str(height), True, (0,0,0))
    
    if base1<base2:
        pygame.draw.polygon(scr, (0,0,0), ((330,220),(470,220),(550,360),(250,360)),3)
        pygame.draw.lines(scr, (0,0,250), False, [(330,220), (330,360)])
        scr.blit(dispB1,(400,190)) 
        scr.blit(dispB2,(400,370))
        scr.blit(dispSide, (510,265))
        scr.blit(dispHeight,(335,275))
        pygame.display.flip()
    else:
        pygame.draw.polygon(scr, (0,0,0), ((330,360),(470,360),(550,220),(250,220)),3)
        pygame.draw.lines(scr, (0,0,250), False, [(330,220), (330,360)])
        scr.blit(dispB1,(390,190)) 
        scr.blit(dispB2,(390,370))
        scr.blit(dispSide, (515,285))
        scr.blit(dispHeight,(335,275))
        pygame.display.flip()
        
        
    #make area for responses
    a = 'Area = '
    p = 'Perimeter = '
    aResponse = bigfont.render(a, True,(0,0,0)) 
    pResponse = bigfont.render(p, True,(0,0,0))   
    scr.blit(aResponse,globalArea)
    scr.blit(pResponse,globalPerim)
    
    aText = ''
    pText = ''
    
    aRect = pygame.Rect(350,470,140,32)
    pRect = pygame.Rect(430,520,140,32)
    
    aSurface = bigfont.render(aText,True,(0,0,0))
    pSurface = bigfont.render(pText,True,(0,0,0))

    #actually doing the maths 
    trap = Trapezoid(base1,base2,height,side)
    areaVal = trap.trapArea()
    perimVal = trap.trapPerim()
    
    #when running
    running = True
    aActive = False
    pActive = False
    while running:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # For events that occur upon clicking the mouse (left click) 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mousePos[0] <= 80 and 0 <= mousePos[1] <= 30:
                    dispArea = bigfont.render(areaformula, True,(0,0,0)) 
                    dispPerim = bigfont.render(perimformula, True,(0,0,0))   
                    scr.blit(dispArea,(0,40))
                    scr.blit(dispPerim,(0,70))
                    pygame.display.flip()
                if 81 <= mousePos[0] <= 161 and 0 <= mousePos[1] <= 30:
                    question(scr)
  
                if 720 <= mousePos[0] <= 800 and 0 <= mousePos[1] <= 30:
                    running = False
                
                if aRect.collidepoint(event.pos):
                    aActive = True
                    pActive = False
                if pRect.collidepoint(event.pos):
                    pActive = True
                    aActive = False
            if event.type == pygame.KEYDOWN:
                if aActive:
                    aText += event.unicode
                    pygame.draw.rect(scr,(0,0,0),aRect,2)
                if pActive:
                    pText += event.unicode
                    pygame.draw.rect(scr,(0,0,0),pRect,2)
                    
                    #if backspace just clear and 
                if event.key == pygame.K_BACKSPACE and aActive:
                    aText = ''
                    pygame.draw.rect(scr,(250,250,250),aRect)
                    pygame.draw.rect(scr,aBox,aRect,2)
                if event.key == pygame.K_BACKSPACE and pActive:
                    pText = ''
                    pygame.draw.rect(scr,(250,250,250),pRect)
                    pygame.draw.rect(scr,aBox,pRect,2)
                           
                #checks if the solution was right             
                if event.key == pygame.K_RETURN and aActive:
                    if float(aText) == float(areaVal):
                        pygame.draw.rect(scr,(250,250,250),[500,475,100,40])
                        correctA = bigfont.render('Correct' , True , (0,250,0))
                        scr.blit(correctA , (500,475))
                    else:
                        aText = ''
                        pygame.draw.rect(scr,(250,250,250),aRect)
                        pygame.draw.rect(scr,aBox,aRect,2)
                        incorrectA = bigfont.render('Wrong' , True , (250,0,0))
                        scr.blit(incorrectA , (500,475))
                        
                if event.key == pygame.K_RETURN and pActive:
                    if float(pText) == float(perimVal):
                        pygame.draw.rect(scr,(250,250,250),[575,527,100,40])
                        correctP = bigfont.render('Correct' , True , (0,250,0))
                        scr.blit(correctP , (575,525))
                    else:
                        pText = ''
                        pygame.draw.rect(scr,(250,250,250),pRect)
                        pygame.draw.rect(scr,aBox,pRect,2)
                        incorrectP = bigfont.render('Wrong' , True , (250,0,0))
                        scr.blit(incorrectP , (575,525))
                        
        aBox = passiveBox
        pBox = passiveBox   
        if aActive:
            aBox = activeBox
            pBox = passiveBox
        if pActive:
            pBox = activeBox
            aBox = passiveBox    
        pygame.draw.rect(scr,aBox,aRect,2)
        pygame.draw.rect(scr,pBox,pRect,2)
        aSurface = bigfont.render(aText,True,(0,0,0))
        pSurface = bigfont.render(pText,True,(0,0,0))
        scr.blit(aSurface,(355,475))
        scr.blit(pSurface,(435,525))    
        
        pygame.display.flip()
                                
    pygame.quit()

def main():
    pygame.init()
    scr = pygame.display.set_mode((800,600))
    scr.fill((255,255,255))
    pygame.display.flip()
    drawTrap(scr)

main()
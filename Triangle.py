import pygame
import random as rand

globalArea = (250,470)
globalPerim = (250,520)
activeBox = (250,0,0)
passiveBox = (0,0,0)

class Triangle:
    def __init__(self, base, height, lengths):
        self.base = base
        self.height = height
        self.lengths = lengths
        
    def triArea(self):
        return self.base * self.height * 0.5
    
    def triPerim(self):
        return self.base + self.lengths + self.lengths

def question(scr):
    generate = rand.randint(1,2)
    if generate == 1:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawTri(scr)
    if generate == 2:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawTri(scr)  

def drawTri(scr):
    bigfont = pygame.font.SysFont('Corbel', 40)
    areaformula ='Area = 1/2 x b x h'
    perimformula = 'Perimeter = b + l1 + l2'  
    
    #draws initial rectangle and length/width text
    base = rand.randint(1,10)
    height = rand.randrange(2,11,2)
    lengths = rand.randint(1,10)
    
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
    
    #if len > wid then vertical, if wid > len, horizontal, else square
    dispLen = bigfont.render(str(lengths), True,(0,0,0))
    dispBase = bigfont.render(str(base), True,(0,0,0))
    dispHeight = bigfont.render(str(height), True,(0,0,0))
    if base>lengths:
        pygame.draw.polygon(scr, (0,0,0), ((240,325),(560,325),(400,225)),3)#(screen,color, triangle pts)
        pygame.draw.lines(scr, (0,0,0), False, [(400,225), (400,325)])
        scr.blit(dispLen,(260,260)) 
        scr.blit(dispLen,(530,260)) 
        scr.blit(dispHeight,(415,275))
        scr.blit(dispBase, (390,340)) 
        pygame.display.flip()
    elif base<lengths:
        pygame.draw.polygon(scr, (0,0,0), ((270,365),(490,365),(380,115)),3)#(screen,color, triangle pts)
        pygame.draw.lines(scr, (0,0,0), False, [(380,115), (380,365)]  )
        scr.blit(dispLen,(240,240)) 
        scr.blit(dispLen,(470,240)) 
        scr.blit(dispHeight,(385,275))
        scr.blit(dispBase, (370,370)) 
        pygame.display.flip()
    else:
        pygame.draw.polygon(scr, (0,0,0), ((250,365),(510,365),(380,139.8)),3)#(screen,color, triangle pts)
        pygame.draw.lines(scr, (0,0,0), False, [(380,139.8), (380,365)]  )
        scr.blit(dispLen,(260,240)) 
        scr.blit(dispLen,(470,240)) 
        scr.blit(dispHeight,(385,265))
        scr.blit(dispBase, (365,375)) 
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
    tri = Triangle(base,height, lengths)
    areaVal = tri.triArea()
    perimVal = tri.triPerim()
    
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
    drawTri(scr)

main()
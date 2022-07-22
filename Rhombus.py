import pygame
import random as rand
globalArea = (250,470)
globalPerim = (250,520)
activeBox = (250,0,0)
passiveBox = (0,0,0)

class Rhombus:
    def __init__(self, diagonal1, diagonal2, length):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.length = length
        
    def rhoArea(self):
        return self.diagonal1 * self.diagonal2 * 0.5
    
    def rhoPerim(self):
        return self.length * 4

def question(scr):
    generate = rand.randint(1,2)
    if generate == 1:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawRho(scr)
    if generate == 2:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawRho(scr)
        
def drawRho(scr):
    bigfont = pygame.font.SysFont('Corbel', 40)
    areaformula ='Area = d1 x d2 x 0.5'
    perimformula = 'Perimeter = 4l'  
    
    diagonal1 = rand.randint(1,10)
    diagonal2 = rand.randint(1,10)
    length = rand.randint(1,10)
    
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
    
    #if d1> d2 horz, if d1<d2 vert if d1=d2 square
    dispD1 = bigfont.render(str(diagonal1), True,(0,0,0))
    dispD2 = bigfont.render(str(diagonal2), True,(0,0,0))
    dispLen = bigfont.render(str(length), True,(0,0,0))
    if diagonal1>diagonal2:
        pygame.draw.polygon(scr, (0,0,0), ((220,295),(400,225),(580,295),(400,365)),3)
        pygame.draw.lines(scr, (0,0,250), False, [(220,295), (580,295)])
        pygame.draw.lines(scr, (0,0,250), False, [(400,225), (400,365)])
        scr.blit(dispLen,(477.5,337.5)) 
        scr.blit(dispD1,(305,300))
        scr.blit(dispD2, (405,250)) 
        pygame.display.flip()
    elif diagonal1<diagonal2:
        pygame.draw.polygon(scr, (0,0,0), ((380,100),(300,265),(380,430),(460,265)),3)
        pygame.draw.lines(scr, (0,0,250), False, [(300,265), (460,265)])
        pygame.draw.lines(scr, (0,0,250), False, [(380,100), (380,430)])
        scr.blit(dispLen,(435,330)) 
        scr.blit(dispD1,(325,265))
        scr.blit(dispD2, (385,205)) 
        pygame.display.flip()
    else:
        pygame.draw.polygon(scr, (0,0,0), ((500,290),(380,160),(260,290),(380,420)),3)
        pygame.draw.lines(scr, (0,0,250), False, [(500,290), (260,290)])
        pygame.draw.lines(scr, (0,0,250), False, [(380,160), (380,420)])
        scr.blit(dispLen,(447.5,352.5)) 
        scr.blit(dispD1,(320,297))
        scr.blit(dispD2, (385,235)) 
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
    rho = Rhombus(diagonal1,diagonal2,length)
    areaVal = rho.rhoArea()
    perimVal = rho.rhoPerim()
    
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
    drawRho(scr)

main()
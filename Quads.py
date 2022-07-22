import pygame
import random as rand

globalArea = (250,470)
globalPerim = (250,520)
activeBox = (250,0,0)
passiveBox = (0,0,0)

class Quadrilateral:    #For squares and rectangles
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def quadArea(self):
        return float(self.length * self.width)
    
    def quadPerim(self):
        return float((2*self.length) + (2*self.width))

def question(scr):
    generate = rand.randint(1,2)
    if generate == 1:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawQuad(scr)
    if generate == 2:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawQuad(scr)
    
def drawQuad(scr):
    bigfont = pygame.font.SysFont('Corbel', 40)
    areaformula ='Area = l x w'
    perimformula = 'Perimeter = 2l + 2w'  
    
    #draws initial rectangle and length/width text
    length = rand.randint(1,10)
    width = rand.randint(1,10)
    
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
    dispLen = bigfont.render(str(length), True,(0,0,0))
    dispWid = bigfont.render(str(width), True,(0,0,0))
    if length>width:
        pygame.draw.rect(scr, (0,0,0), pygame.Rect(325, 150, 150, 300),3)#(x,y,len,wid)
        scr.blit(dispLen,(280,280)) 
        scr.blit(dispWid,(375,120)) 
        pygame.display.flip()
    elif width>length:
        pygame.draw.rect(scr, (0,0,0), pygame.Rect(250, 200, 300, 150),3)#(x,y,len,wid)
        scr.blit(dispLen,(210,260)) 
        scr.blit(dispWid,(375,170)) 
        pygame.display.flip()
    else:
        pygame.draw.rect(scr, (0,0,0), pygame.Rect(275, 175, 250, 250),3)#(x,y,len,wid)
        scr.blit(dispLen,(230,280)) 
        scr.blit(dispWid,(375,140)) 
        pygame.display.flip()

    #actually doing the maths 
    quad = Quadrilateral(length,width)
    areaVal = quad.quadArea()
    perimVal = quad.quadPerim()
    
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
    drawQuad(scr)

main()
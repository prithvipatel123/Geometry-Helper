import pygame
import random as rand

globalArea = (250,470)
globalPerim = (250,520)
activeBox = (250,0,0)
passiveBox = (0,0,0)

def question(scr):
    generate = rand.randint(1,5)
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
        drawTri(scr)
    if generate == 3:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawCir(scr) 
    if generate == 4:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawRho(scr) 
    if generate == 5:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawTrap(scr) 

#=========================================================
class Quadrilateral:    #For squares and rectangles
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def quadArea(self):
        return float(self.length * self.width)
    
    def quadPerim(self):
        return float((2*self.length) + (2*self.width))
    
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

#=========================================================

class Triangle:
    def __init__(self, base, height, lengths):
        self.base = base
        self.height = height
        self.lengths = lengths
        
    def triArea(self):
        return self.base * self.height * 0.5
    
    def triPerim(self):
        return self.base + self.lengths + self.lengths

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
        pygame.draw.lines(scr, (0,0,250), False, [(400,225), (400,325)]  )
        scr.blit(dispLen,(260,260)) 
        scr.blit(dispLen,(530,260)) 
        scr.blit(dispHeight,(415,275))
        scr.blit(dispBase, (390,340)) 
        pygame.display.flip()
    elif base<lengths:
        pygame.draw.polygon(scr, (0,0,0), ((270,365),(490,365),(380,115)),3)#(screen,color, triangle pts)
        pygame.draw.lines(scr, (0,0,250), False, [(380,115), (380,365)]  )
        scr.blit(dispLen,(260,240)) 
        scr.blit(dispLen,(470,240)) 
        scr.blit(dispHeight,(385,275))
        scr.blit(dispBase, (370,370)) 
        pygame.display.flip()
    else:
        pygame.draw.polygon(scr, (0,0,0), ((250,365),(510,365),(380,139.8)),3)#(screen,color, triangle pts)
        pygame.draw.lines(scr, (0,0,250), False, [(380,139.8), (380,365)]  )
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

#=========================================================
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def cirArea(self):
        return float(self.radius * self.radius * 3.14)
    
    def cirPerim(self):
        return float(2 * 3.14 * self.radius)
    
def drawCir(scr):
    bigfont = pygame.font.SysFont('Corbel', 40)
    areaformula ='Area = pi x r x r'
    perimformula = 'Circumference = 2 x pi x r'  
    
    #draws initial rectangle and length/width text
    radius = rand.randint(1,10)
    
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
    
    #print out circle with radius
    pygame.draw.circle(scr, (0, 0, 0),[400, 300], 110, 3)
    pygame.draw.line(scr, (0,0,250),(400,300), (510,300),2)
    dispRad = bigfont.render(str(radius), True,(0,0,0))
    scr.blit(dispRad,(400,270))
    pygame.display.flip()
    
    #make area for responses
    a = 'Area = '
    p = 'Circumference = '
    aResponse = bigfont.render(a, True,(0,0,0)) 
    pResponse = bigfont.render(p, True,(0,0,0))   
    scr.blit(aResponse,globalArea)
    scr.blit(pResponse,(200,520))
    
    aText = ''
    pText = ''
    
    aRect = pygame.Rect(350,470,140,32)
    pRect = pygame.Rect(430,520,140,32)
    
    aSurface = bigfont.render(aText,True,(0,0,0))
    pSurface = bigfont.render(pText,True,(0,0,0))
    
    #actually doing the maths 
    cir = Circle(radius)
    areaVal = cir.cirArea()
    perimVal = cir.cirPerim()
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
                    if float(aText) == round(float(areaVal),2):
                        pygame.draw.rect(scr,(250,250,250),[500,475,100,40])
                        correctA = bigfont.render('Correct' , True , (0,250,0))
                        scr.blit(correctA , (500,475))
                    else:
                        print(float(areaVal))
                        aText = ''
                        pygame.draw.rect(scr,(250,250,250),aRect)
                        pygame.draw.rect(scr,aBox,aRect,2)
                        incorrectA = bigfont.render('Wrong' , True , (250,0,0))
                        scr.blit(incorrectA , (500,475))
                        
                if event.key == pygame.K_RETURN and pActive:
                    if float(pText) == round(float(perimVal),2):
                        pygame.draw.rect(scr,(250,250,250),[575,527,100,40])
                        correctP = bigfont.render('Correct' , True , (0,250,0))
                        scr.blit(correctP , (575,525))
                    else:
                        print(float(perimVal))
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
      
      
#=========================================================
class Rhombus:
    def __init__(self, diagonal1, diagonal2, length):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.length = length
        
    def rhoArea(self):
        return self.diagonal1 * self.diagonal2 * 0.5
    
    def rhoPerim(self):
        return self.length * 4
    
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
    
    
#=========================================================     
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
    generate = rand.randint(1,4)
    if generate == 1:
        print(generate)
        drawQuad(scr)
    if generate == 2:
        print(generate)
        drawTri(scr)
    if generate == 3:
        print(generate)
        drawCir(scr)
    if generate == 4:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawRho(scr)
    if generate == 5:
        print(generate)
        scr = pygame.display.set_mode((800,600))
        scr.fill((255,255,255))
        pygame.display.flip()
        drawTrap(scr)  


main()
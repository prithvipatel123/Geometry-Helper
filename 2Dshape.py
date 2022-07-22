import math
pi = math.pi
Aformulas = {"quad":"length x width", "tri":"1/2 x base x height", "cir":"pi x radius x radius", "rho":"diagonal 1 x diagonal 2 x 0.5", "tra": "height x 0.5 x (base1 + base2)"}

#defines classes for each of the shapes anc gets their necessary values
class Quadrilateral:    #For squares and rectangles
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def quadArea(self):
        return self.length * self.width
    
    def quadPerim(self):
        return (2*self.length) + (2*self.width)
    

class Triangle:
    def __init__(self, base, height, lengths):
        self.base = base
        self.height = height
        self.lengths = lengths
        
    def triArea(self):
        return self.base * self.height * 0.5
    
    def triPerim(self):
        return self.base + self.lengths + self.lengths

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def cirArea(self):
        return float(self.radius * self.radius * 3.14)
    
    def cirPerim(self):
        return float(2 * 3.14 * self.radius)

class Rhombus:
    def __init__(self, diagonal1, diagonal2, length):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.length = length
        
    def rhoArea(self):
        return self.diagonal1 * self.diagonal2 * 0.5
    
    def rhoPerim(self):
        return self.length * 4

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

def shapeChoice():
    
    choice = input("Shape Type: ")
    while choice != 'quadrilateral' or choice != 'triangle' or choice != 'circle' or choice != 'rhombus'  or choice != 'trapezoid':
        print("Please input valid shape")
        choice = input("Shape Type: ")
        
    if choice == 'quadrilateral':
        return 'qua'
    elif choice == 'triangle':
        return 'tri'
    elif choice == 'circle':
        return 'cir'
    elif choice == 'rhombus':
        return 'rho'
    elif choice == 'trapezoid':
        return 'tra'

        
    
def getPerameters():    #return the formula, and parameters
    choice = shapeChoice()
    if choice == 'qua':
        Farea = Aformulas["quad"]
        val1 = float(input("Length: "))
        val2 = float(input("Width: "))
        val3 = 1
        val4 = 1
        return Farea, val1,val2,val3, choice, val4
    
    if choice == 'tri':
        Farea = Aformulas["tri"]
        val1 = float(input("Base: "))
        val2 = float(input("Height: "))
        val3 = float(input("Side Lengths: "))
        val4 = 1
        return Farea,val1,val2,val3, choice, val4
    
    if choice == 'cir':
        Farea = Aformulas["cir"]
        val1 = float(input("Radius: "))
        val2 = 1
        val3 = 1
        val4 = 1
        return Farea,val1,val2,val3, choice
    if choice == 'rho':
        Farea = Aformulas["rho"]
        val1 = float(input("Diagonal 1: "))
        val2 = float(input("Diagonal 2: "))
        val3 = float(input("Side Length: "))
        val4 = 1
        return Farea, val1,val2, val3, choice, val4
    
    if choice == 'tra':
        Farea = Aformulas["tra"]
        val1 = float(input("Base 1: "))
        val2 = float(input("Base 2: "))
        val3 = float(input("Height: "))
        val4 = float(input("Side Length: "))
        return Farea, val1,val2,val3, choice, val4
        

    

        
        
#decides what shape and does the maths
def calculate():
    param = getPerameters()
    if param[4]=='qua':
        shape = Quadrilateral(param[1],param[2])    
        areaVal = shape.quadArea()
        perimVal = shape.quadPerim()
        return param[0], areaVal, perimVal, param[4]
    
    if param[4]=='tri':
        shape = Triangle(param[1],param[2], param[3])    
        areaVal = shape.triArea()
        perimVal = shape.triPerim()
        return param[0], areaVal, perimVal, param[4]
    
    if param[4]=='cir':
        shape = Circle(param[1])    
        areaVal = shape.cirArea()
        perimVal = shape.cirPerim()
        return param[0], areaVal, perimVal, param[4]   
    
    if param[4]=='rho':
        shape = Rhombus(param[1], param[2], param[3])    
        areaVal = shape.rhoArea()
        perimVal = shape.rhoPerim()
        return param[0], areaVal, perimVal, param[4]  
     
    if param[4]=='tra':
        shape = Trapezoid(param[1], param[2], param[3], param[5])    
        areaVal = shape.trapArea()
        perimVal = shape.trapPerim()
        return param[0], areaVal, perimVal, param[4]   

    
#main function that does terminal work    
def main():
    output = calculate()

    print("Area Formula: "+ output[0])
    if output[3] == 'cir':
        print("Perimeter Formula: 2 x pi x radius")
    else:
        print("Perimeter Formula: Add All Side Lengths")

    A_response = float(input("Area: "))
    while A_response != output[1]:      #output 1 should be areaVal
        print("Incorrect :(" + "\n")
        A_response = float(input("Area: "))
    print("Correct!" + "\n")

    P_response = float(input("Perimeter: "))
    while P_response != output[2]:      #output[2] should be perimVal
        print("Incorrect :(" + "\n")
        P_response = float(input("Perimeter: "))
    print("Correct!")

main()
class Coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
@property
def x(self):
    return float(self.x)
@property
def y(self):
    return float(self.y)
@x.setter
def x(self,x):
    if isistance(x,int) or isistance(x,float):
        self._x=x
    else:
        raise TypeError("the value must be a int/float")
@y.setter
def y(self,y):
    if isistance(y,int) or isistance(y,float):
        self._y=y
    else:
        raise TypeError("the value must be a int/float")
def __add__(self,other):
    return Coordinate(self.x+other.x,self.y+other.y)
def __sub__(self,other):
    return Coordinate(self.x-other.x,self.x-self.y)
def __len__(self):
    return int((self.x**2+self.y**2)**(1/2))
def __hash__(self):
    return int(len(self))
def __iter__(self):
    iter((self.x,self.y))
def __getattr__(self,attr):#Más eficiente diccionario pero yo paso de implementarlo,bueno eficiente no,más bonito
    if attr=="x" or attr=="_x":
        toret=self._x
    elif attr=="y" or attr=="_y":
        toret=self._y
    else:
        raise TypeError("the value must be consider as a atributte")
    return toret
def __setattr__(self,attr,mod):
    if attr=="x" or attr=="_x":
        self._x=x
    elif attr=="y" or attr=="_y":
        self._y=y
    else:
        raise TypeError("the value must be consider as a atributte")
def __repr__(self):#Deberíamos usar un StringBuilder
    return "("+str(self.x)+","+str(self.y)+")"
def __str__(self):#/Deberíamos usar un StringBuilder
    return "X="+str(self.x)+"\tY="+str(self)

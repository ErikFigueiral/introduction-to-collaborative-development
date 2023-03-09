class Coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    def x(self):
        return float(self._x)
    @property
    def y(self):
        return float(self._y)
    @x.setter
    def x(self,x):
        if not isinstance(x, (int, float)):
            raise TypeError("the value must be a int/float")
        self._x=x
    @y.setter
    def y(self,y):
        if isinstance(y,int) or isinstance(y,float):
            self._y=y
        else:
            raise TypeError("the value must be a int/float")
    def __add__(self,other):
        return Coordinate(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Coordinate(self.x-other.x,self.y-other.y)
    def __len__(self):
        return int((self.x**2+self.y**2)**(1/2))
    def __repr__(self):#Deberíamos usar un StringBuilder
        return "("+str(self.x)+","+str(self.y)+")"
    def __str__(self):#/Deberíamos usar un StringBuilder
        return "X="+str(self.x)+"\tY="+str(self)
    def distance_to_origin(self):#Se puede hacer más eficiente pero es una tonteria
        return ((self.x)**2+(self.y)**2)**(1/2)

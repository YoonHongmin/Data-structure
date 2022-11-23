class Car :
    def __init__(self,color,speed =0):
        self.color = color
        self.speed = speed
    def __eq__(self,B) :
        return self.color == B.color
    def SpeedUp(self) : self.speed += 10
    def isEqual(self,B) :
        return self.speed == B.speed
    def __str__(self) :
        return "color : %s , speed : %d "%(self.color,self.speed)

class SuperCar(Car) :
    def __init__(self,color,speed,Turbo=True) :
        super().__init__(color,speed)
        self.Turbo = Turbo
    def __str__(self) :
        if self.Turbo :
            return "[터보모드] color : %s, speed : %d"%(self.color,self.speed)
        else :
            return "[일반모드] color : %s, speed : %d"%(self.color,self.speed)
    def SpeedUp(self):
        if self.Turbo :
            self.speed += 50
        else :
            super().SpeedUp()

car1 = Car('yellow', 70)
car2 = Car('Black', 60)
print(car1==car2)
car2.SpeedUp()
print(car2.speed)
print(car1.isEqual(car2))
print("car1 : ", car1)

BMW = SuperCar('white', 200, True)
BMW.SpeedUp()
print("BMW : ", BMW)
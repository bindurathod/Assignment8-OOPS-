class Car:
 def __init__(self,model,brand,color):
     self.model=model
     self.brand=brand
     self.color=color
  
 def start(self):
     print('start')
 def move(self):
     print('move')
 def stop(self):
     print('stop')
  
  
class BMW(Car):
 def __init__(self,model,brand,color,price,number):
     super().__init__(model,brand,color)
     self.price=price
     self.number=number
 def Autopilot(self):
     print("Car")

 def Autogear(self):
     print("Model:",self.model)
     print("Brand:",self.brand)
     print("Color:",self.color)
     print("Price:",self.price)
d=BMW('Ritz', 'B6', 'white', 10000, 13)
d.start()
d.move()
d.stop()
d.Autopilot()
d.Autogear()

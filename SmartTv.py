class TV:
 def __init__(self,model,brand):
     self.model=model
     self.brand=brand
     
 def start(features):
     print('Features of TV')
 
class SmartTV(TV):
 def __init__(self,model,brand,screensize,price,resolution):
     super().__init__(model,brand)
     self.price=price
     self.screensize=screensize
     self.resolution=resolution
     
     
   

 def newFeatures(self):
     print("Model",self.model)
     print("Brand",self.brand)
     print("Screensize:",self.screensize)
     print("Price:",self.price)
     print("Resolution:",self.resolution)
    
d=SmartTV('45', 55000, 'HD','Samsung','B6')
d.start()
d.newFeatures()

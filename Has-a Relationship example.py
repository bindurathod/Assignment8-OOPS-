class Memory:
 def __init__(self,internal,secondary,ram):
  self.internal=internal
  self.secondary=secondary
  self.ram=ram
 def getinfo(self):
  print("Internal:{} , Secondary:{} and Ram:{}".format(self.name,self.model,self.color))

class Mobile:
 def __init__(self,model,brand,price,memory):
  self.model=model
  self.brand=brand
  self.price=price
  self.memory=memory
 
 def info(self):
  print("Mobile Model:",self.model)
  print("Mobile Brand:",self.brand)
  print("Mobile Price:",self.price)
  print("Mobile Memory info:",self.memory)
  

c=Memory("20GB","2GB","4GB")
e=Mobile('Samsung','B6', 49000, 23)
e.info()

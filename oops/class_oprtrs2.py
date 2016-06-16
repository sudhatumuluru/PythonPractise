class mycla():
     'This gives the declaration of the class'
     def __init__(self,var1,var2):
          self.var1=var1
          self.var2=var2
     def sum(self):
         print "sum is : ",self.var1+self.var2
     def subtract(self):
         print "diff is : ",self.var1-self.var2
obj=mycla(500,700)
obj=mycla(300,200)
obj.sum()
obj.subtract()
obj=mycla(600,400)
obj.sum()
obj.subtract()


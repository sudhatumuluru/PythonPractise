class mycla():
     'This gives the declaration of the class'
     def __init__(self,var1,var2):
          self.var1=var1
          self.var2=var2
     def dis(self):
         print "sum is : ",self.var1+self.var2
obj=mycla(500,700)
obj.dis()


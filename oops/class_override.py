class parent():
     'This gives the declaration of the parent class'
     def __init__(self,var1,var2):
         self.var1=var1
         self.var2=var2
     def ope(self):
         print "parent class sum : ",self.var1+self.var2
class child(parent):
     'This gives the declaration of the parent class'
     def __init__(self,var1,var2):
         self.var1=var1
         self.var2=var2
     def ope(self):
         print "child class sub : ",self.var1-self.var2
obj_c=child(300,500)
obj_c.ope()

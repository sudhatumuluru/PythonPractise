class mycla():
     'This gives the declaration of the class'
     var=100
     def __init__(self,var1):
         mycla.var=var1
     def dis(self):
         print "given class variable :",mycla.var
obj=mycla(1000)
obj.dis()

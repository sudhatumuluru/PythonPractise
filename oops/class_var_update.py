class mycla():
     'This gives the declaration of the class'
     var=100
     def __init__(self):
         mycla.var=200
     def dis(self):
         print "given class variable :",mycla.var
obj=mycla()
obj.dis()

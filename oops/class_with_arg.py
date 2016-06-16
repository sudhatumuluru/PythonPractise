class mycla():
     'This gives the declaration of the class'
     def __init__(self,var1):
          self.var1=var1
     def dis(self):
         print "my name: ",self.var1
obj=mycla("python")
obj.dis()
print "enter name: "
name=raw_input()
obj=mycla(name)
obj.dis()


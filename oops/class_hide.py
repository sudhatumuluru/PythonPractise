class mycla():
     'This gives the declaration of the class'
     var=100
     def secret(self):
         self.var*=10
         print "secret value :",self.var
obj=mycla()
obj.secret()
obj.secret()
obj.secret()

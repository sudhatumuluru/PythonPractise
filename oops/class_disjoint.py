class a():
     'This gives the declaration of the parent class'
     def disp(self):
         print " class 'a' calling"
class b():
     'This gives the declaration of the child class'
     def disc(self):
         print "class 'b' calling"
obj_p=a()
obj_c=b()
obj_p.disp()
obj_c.disc()

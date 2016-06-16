class parent():
     'This gives the declaration of the parent class'
     def disp(self):
         print "parent class calling"
class child(parent):
     'This gives the declaration of the child class'
     def disc(self):
         print "child class calling"
obj_p=parent()
obj_c=child()
obj_p.disp()
obj_c.disc()

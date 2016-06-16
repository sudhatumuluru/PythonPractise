print "enter var1"
var1=input()
print "enter var2"
var2=input()
print "enter var3"
var3=input()
if(var1>var2):
   if(var1>var3):
       print "Max is ", var1
   else:
       print "MAX is ", var3
elif(var2>var1):
   if(var2>var3):
       print "Maxi is ", var2
   else:
       print "MAX is ", var3
else:
   print "Max is", var3

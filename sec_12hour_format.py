import os
import sys
count=1
while(count<13):
     if(count==5):
          print "python"
     if(count==6):
          print "perl"
     if(count==7):
          print "shellscript"
     os.system("sleep 1")
     if(count==12):
          count=0
     print "count : ",count
     count=count+1

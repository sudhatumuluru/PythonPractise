import os
import sys
f=open('cmdline_file','a')
f.write("sno  name        id      sal     location             company  \n  ")
f.write("%s %s %s %s %s %s \n" %(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]))
f.close()

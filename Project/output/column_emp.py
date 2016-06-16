import os
import sys
print("bang empls")
os.system("awk '/bang/{print $0}' file > bang_emp")
os.system("awk '{print $2}' bang_emp")
print("hyd empls : ")
os.system("awk '/hyd/{print $0}' file > hyd_emp")
os.system("awk '{print $2}' hyd_emp")

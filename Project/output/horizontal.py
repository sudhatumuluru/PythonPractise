import os
import sys
os.system("awk '/bang/{print $0}' file > bang_emp")
os.system("awk '{print $2}' bang_emp>bang_emp1")
os.system("awk '/hyd/{print $0}' file > hyd_emp")
os.system("awk '{print $2}' hyd_emp>hyd_emp1")
os.system("echo bang_emp hyd_emp")
os.system("paste bang_emp1 hyd_emp1>horizontal_emp")

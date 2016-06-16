
import os
import sys
os.system("awk '/bang/{print $0}' file > bang_emp")
os.system("awk '{print $2}' bang_emp")

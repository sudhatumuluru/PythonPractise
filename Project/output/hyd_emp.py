import os
import sys
os.system("awk '/hyd/{print $0}' file > hyd_emp")
os.system("awk '{print $2}' hyd_emp")

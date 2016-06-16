import os
import sys 
os.system("awk '/hyd/{print $0}' file>hyd")
os.system("awk '{sum+=$4} END {print sum}' hyd")

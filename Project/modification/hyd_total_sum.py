import os
import sys 
os.system("awk '/hyd/{print $0}' file>hyd")
os.system("awk '{var=$4};{$4=$4*10};{$4=$4/100};{$4=var+$4};{print $4}' hyd>hyd_hike")
os.system("awk '{sum+=$1} END {print sum}' hyd_hike")

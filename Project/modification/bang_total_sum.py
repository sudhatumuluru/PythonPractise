import os
import sys 
os.system("awk '/bang/{print $0}' file>bang")
os.system("awk '{var=$4};{$4=$4*10};{$4=$4/100};{$4=var+$4};{print $4}' bang>bang_hike")
os.system("awk '{sum+=$1} END {print sum}' bang_hike")

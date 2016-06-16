import os
import sys
os.system("awk '{sum+=$4} END {print sum}' file")

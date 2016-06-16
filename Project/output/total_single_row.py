import os
import sys
os.system("cat bang_emp hyd_emp>add_text_single_file")
#os.system("paste -s add_text_single_file")
os.system("awk '{print $2}' add_text_single_file>total_emps")
os.system("paste -s -d'-' total_emps")

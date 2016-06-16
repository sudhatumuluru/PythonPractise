import os
import sys
os.system("awk '{print $2 \"->\" $3}' file>relation_emp_id_file")
os.system("awk '{print $2 \"->\" $4}' file>relation_emp_sal_file")

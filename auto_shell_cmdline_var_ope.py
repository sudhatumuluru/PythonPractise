f=open("var_cmdline_var_ope.sh","ab")
f.write("var1=$1\n")
f.write("var2=$2\n")
f.write("echo \"given vars : $var1 $var2\"\n")
f.write("((var3=var1+var2))\n")
f.write("echo \"sum : $var3\"\n")
f.close()

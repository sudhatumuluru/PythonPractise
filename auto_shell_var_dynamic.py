f=open("var_dynamic.sh","ab")
f.write("echo \"enter var : \"\n")
f.write("read var\n")
f.write("echo \"given var : $var\"")
f.close()
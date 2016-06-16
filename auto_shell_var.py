f=open("var.sh","ab")
f.write("var=100\n")

f.write("echo \"given var : $var\"")
f.close()

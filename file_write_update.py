f=open("f_write_update","ab")
print "enter name"
name=raw_input()
f.write("%s\n"%name)
f.close()

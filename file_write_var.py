f=open("f_write_var","wb")
print "enter name"
name=raw_input()
f.write("%s"%name)
f.close()

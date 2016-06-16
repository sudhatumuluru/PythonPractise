f=open("f_write","wb")
print "file name: ",f.name
print "file mode: ",f.mode
print "file closed: ",f.closed
print "file is attached to the filter: ",f.softspace
f.close()
print "file closed: ",f.closed


f=open('var_file','a')
f.write("sno  name        id      sal     location             company  \n  ")
print("enter sno : ")
sno=raw_input()
print("enter name : ")
name=raw_input()
print("enter id : ")
id=raw_input()
print("enter salary : ")
sal=raw_input()
print("enter location : ")
location=raw_input()
print("enter company : ")
company=raw_input()
f.write("%s %s %s %s %s %s \n" %(sno,name,id,sal,location,company))
f.close()



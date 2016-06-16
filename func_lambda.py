def fun_lambda(var1):
    return(var1)
sum=fun_lambda(100)
print "sum is ", sum
def fun_lambda1(var1):
    return(lambda var2:var1+var2) 
#calling a function in return
sum=fun_lambda1(100)
print "sum is", sum(200)


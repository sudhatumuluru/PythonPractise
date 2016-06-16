with open('example.csv','w') as fp:
   for x in range(1,10):
       full_line='{},{}\n'.format(str(x),x%3)
       fp.write(full_line)

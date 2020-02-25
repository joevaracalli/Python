inputnum = int(input("Enter a num greater than 1: "))
factor = 2
div  = factor/inputnum

while inputnum > 1:
 if div != None:
  print(div)
  inputnum = inputnum/factor

 else:
     factor = factor + 1

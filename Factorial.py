# ask for user input of factorial
inputfact = int(input("Enter a postive integer between 1 and 20: "))
# set fact  = 1 as base
fact = 1
# define a empty list to add the factorials to
list = []

# loop through each number to calculate the factorial then print its original number
# and its factoal while adding it to the list
for i in range(1,inputfact+1):
    fact =  fact * i
    print(' i = ',i, '\t',  i,' ! = ', fact)
    list.append(fact)

# print list    
print("List = ",list)

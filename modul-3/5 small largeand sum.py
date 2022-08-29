#create empty list 

mylist = []

number = int(input('How many elements to put in List: '))

for n in range(number):

    element = int(input('Enter element '))

    mylist.append(element)

print("Maximum element in the list is :", max(mylist))

print("Minimum element in the list is :", min(mylist))
print("the sum of list is:",sum(mylist))
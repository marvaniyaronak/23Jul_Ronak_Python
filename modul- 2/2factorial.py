# the pogram is factorial number
from math import factorial
num=int(input("enter the number: "))
factorial=1
if num < 0:
    print("the factorial is not exits ")
elif num == 0:
    print("the factorial is 0 is 1 ")
else:
    for i in range(1,num + 1):
        factorial=factorial+i
        print("the factorial of ",num,"is",factorial)
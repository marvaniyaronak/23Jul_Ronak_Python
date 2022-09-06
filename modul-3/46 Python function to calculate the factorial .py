def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
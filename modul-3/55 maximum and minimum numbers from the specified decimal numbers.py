from decimal import *
data = list(map(Decimal, '2.70 2.69 2.89 3.45 2.00 0.05 7.25'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))

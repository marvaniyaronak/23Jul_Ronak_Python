d=[{"ronak":"60"},{"raj":"45"},{"ramesh":"60"},{"priya":"80"},{"rajvi":"80"}]
print("original list:-",d)

u_value = set( val for dic in d for val in dic.values())

print("Unique Values: ",u_value)

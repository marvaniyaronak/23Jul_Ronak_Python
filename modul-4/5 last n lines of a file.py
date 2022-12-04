n = int(input("Enter Lines To Read : "))
f = open("test.txt","r")
for i in range(n):
	print(f.readline())
with open("test.txt") as f:
    list = f.readlines()

# remove new line characters
list = [x.strip() for x in list]
print(list)
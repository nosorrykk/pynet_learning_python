#Reading file with Context Manager#
with open("show_version.txt", mode ="r") as f:
    data = f.readlines()

print(data[0])

print(type(data))


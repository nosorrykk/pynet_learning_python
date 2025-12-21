#Reading file without Context Manager#
f = open("show_version.txt")
data = f.read()

print(data.splitlines()[0])

print(type(data))

f.close()


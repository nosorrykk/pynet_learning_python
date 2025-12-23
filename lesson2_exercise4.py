##from pprint import pprint
with open("show_arp.txt") as f:
    show_arp = f.readlines()

#4a solution - Print out the Python data type of 'show_arp' variable.

print(type(show_arp)) 

#4b solution - Print out the length of the 'show_arp' variable.

print(len(show_arp))

#4c solution - Print out the header line from the 'show_arp' variable.

print(show_arp[0])

#4d - Print out both the first and the last line of the tabular data from the 'show_arp' variable.

print(f"First line of tabular data:\n{show_arp[1]}")
print(f"Last line of tabular data:\n{show_arp[-1]}")

#4e - Split the header line into fields using the .split() method. Save this into a variable named fields. Print out this 'fields' variable.

fields = show_arp[0].split()
print(fields)

#4f - Print out the Python data type of this 'fields' variable.

print(type(fields))

#4g - Print out the current number of entries in the 'fields' variable.

print(len(fields))

#4h - Print out the first field and the last field.

print(f"First field:\n{fields[0]}")
print(f"Last field:\n{fields[-1]}")

#Modifications to the fields variable: 

fields.remove("(min)")
fields.remove("Hardware")
fields.remove("Addr")
Hardware_Addr = "Hardware" + "_" + "Addr"
fields.insert(3, f"{Hardware_Addr}")
print(f"Fields after modifications:\n{fields}")


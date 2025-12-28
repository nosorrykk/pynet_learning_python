# Create a Python program that reads the file named show_ip_int_brief.txt.
# Loop over the contents of this file (in some way).

with open("show_ip_int_brief.txt") as f:
    data = f.readlines()

#From this, create a list of all of the assigned IP addresses.
#Additionally, create a list of all the interfaces containing an IP address. 
#The order of these two lists should match. In other words, the first IP address
#should correspond to the first interface in the interfaces list.
#Print both of these lists out to standard output.

print("-" * 80)

for line in data:
    if "10." in line:
        line = line.split()
        print(f"Interface Name = {line[0]}, IP Address = {line[1]}")

print("-" * 80)

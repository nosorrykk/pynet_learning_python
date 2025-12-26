#Create a Python program that reads in the file named show_ip_int_brief.txt.

with open("show_ip_int_brief.txt") as f:
    data = f.readlines()

print("-" * 20)

for line in data:
    if "10.220" in line:
        line = line.split()
        intf_name = line[0]
        ip_addr = line[1]
        print(f"Interface = {intf_name}")
        print(f"Ip Addr = {ip_addr}")

print("-" * 20)


#Create a variable named 'intf' using the following string (from 'show ip interface brief' on a Cisco router):

intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"

#split() this variable into fields based on white-space and save this to a variable named intf_fields:

intf_fields = intf.split()

print(intf_fields)

#new variables from intf_fields:

intf_name = intf_fields[0]
intf_ip_addr = intf_fields[1]
intf_status = intf_fields[-2]
intf_protocol = intf_fields[-1]

print()
print("-" * 60)
print(f"intf_name = {intf_name}")
print(f"intf_ip_addr = {intf_ip_addr}")
print(f"intf_status = {intf_status}")
print(f"intf_protocol = {intf_protocol}")
print("-" * 60)
print()

#create booleans for line status and line protocol:

line_status = intf_status == "up"
line_protocol = intf_protocol == "up"

print()
print("-" * 60)
print(f"{line_status=}")
print(f"{line_protocol=}")
print("-" * 60)
print()
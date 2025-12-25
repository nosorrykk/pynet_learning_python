#Create a base address variable and set it to "192.168.254.". Prompt a user to enter a subnet prefix length that ranges
#between 25 to 30 (i.e. the netmask length of the subnets). Save this input as an integer.

base_addr = "192.168.254."
subnet_prefix_length = input("Enter prefix length between 25 to 30: ")
subnet_prefix_length = int(subnet_prefix_length)

#From the entered subnet prefix length, calculate the size of the subnet (the number of total IP addresses in the subnet). 
#Once we know the subnet size, we can calculate the number of hosts allowed in the subnet (subtract off the network number 
#and the broadcast address).Use a loop to print out all of the subnet network numbers. 

mask_max_length = 32
mask_base_length = 24

number_of_subnets = 2**(subnet_prefix_length - mask_base_length)
subnet_base = 2**(mask_max_length - subnet_prefix_length)
number_of_hosts = subnet_base - 2
base_subnet = 0

print("*" * 120)
print("Subnets:")
print(f"Number of subnets: {number_of_subnets}")
for n in range(number_of_subnets):
    print(f"Subnet Number: {base_addr}{base_subnet}")
    base_subnet+=subnet_base

print(f"The number of hosts in the Subnet = {number_of_hosts}")
print(f"First subnet first host = {base_addr}1, First subnet last host = {base_addr}{subnet_base-2}")
print("*" * 120)

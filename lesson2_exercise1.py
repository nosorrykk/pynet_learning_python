base_addr = "192.18.254."
subnet_prefix_length = input("Enter a prefix length between 25 to 30: ")
subnet_prefix_length = int(subnet_prefix_length)

max_mask_length = 32
mask_diff = max_mask_length - subnet_prefix_length

number_hosts_subnet = 2**mask_diff - 2

print(number_hosts_subnet)

network_subnet1 = f"{base_addr}0"
network_subnet2 = f"{base_addr}{2**mask_diff}"

print(network_subnet1, network_subnet2)

first_subnet_hostfirst = f"{base_addr}1"
first_subnet_hostlast = f"{base_addr}{2**mask_diff-2}"

print(first_subnet_hostfirst, first_subnet_hostlast)
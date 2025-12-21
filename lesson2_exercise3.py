#3a solution
ip_addr_list = ["10.10.10.1", "10.10.10.2", "10.10.10.3", "10.10.10.4", "10.10.10.5"]

print("List of Initial IP Addresses")
print("*" * 60)
print(f"{ip_addr_list}")
print("*" * 60)
print()

ip_addr_list.append("10.10.10.6")

#3b solution

ip_addr_list.extend(["10.10.10.7", "10.10.10.8"])

#3c solution

ip_addr_list = ip_addr_list + ["10.10.10.9", "10.10.10.10"]

#3d solution

print("Updated List of Ip Addresses")
print("*" * 90)
print(f"{ip_addr_list}")
print("*" * 90)
print()
print("First IP and Last IP on the List")
print("*" * 30)
print(f"{ip_addr_list[0], {ip_addr_list[-1]}}")
print("*" * 30)

#3e solution

ip_addr_list.pop(0)
ip_addr_list.pop(-1)

#3f solution
ip_addr_list.insert(0, "2.2.2.2")

print("Updated First IP Address")
print("*" * 10)
print(f"{ip_addr_list[0]}")
print("*" * 10)
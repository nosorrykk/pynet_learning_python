#Create a Python program that reads the file named junos_show_arp.txt.
#From this Junos ARP information, extract all of the IP address to MAC-address 
#bindings. Convert the MAC address format from '06:1a:97:b0:c4:89' to '06-1a-97-b0-c4-89'
#Print all of these pairings out to standard output.

with open("junos_show_arp.txt") as f:
    data = f.readlines()

print("*" * 50)
for line in data:
     if "172." in line or "128." in line:
        line = line.split()
        IP_Address = line[1]
        MAC_Address = line[0].split(":")
        print(f"{IP_Address:13} : {"-".join(MAC_Address)}")

print("*" * 50)
print()

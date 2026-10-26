import ipaddress

ip = input("Masukkan IP dan prefix (contoh 192.168.1.0/24): ")

jaringan = ipaddress.ip_network(ip, strict=False)

print("Network address :", jaringan.network_address)
print("Broadcast       :", jaringan.broadcast_address)
print("Subnet mask     :", jaringan.netmask)
print("Jumlah host     :", jaringan.num_addresses - 2)
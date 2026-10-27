import ipaddress

ip = input("Masukkan IP dan prefix (contoh 192.168.1.0/24): ")

try:
    jaringan = ipaddress.ip_network(ip, strict=False)
except ValueError:
    print("Input tidak valid, contoh yang benar: 192.168.1.0/24")
    exit()

host_awal = jaringan.network_address + 1
host_akhir = jaringan.broadcast_address - 1

print("Network address :", jaringan.network_address)
print("Broadcast       :", jaringan.broadcast_address)
print("Subnet mask     :", jaringan.netmask)
print("Range host      :", host_awal, "sampai", host_akhir)
print("Jumlah host     :", jaringan.num_addresses - 2)
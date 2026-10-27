from kalkulator import hitung_subnet

ip = input("Masukkan IP dan prefix (contoh 192.168.1.0/24): ")

try:
    hasil = hitung_subnet(ip)
except ValueError:
    print("Input tidak valid, contoh yang benar: 192.168.1.0/24")
    exit()

print("Network address :", hasil["network"])
print("Broadcast       :", hasil["broadcast"])
print("Subnet mask     :", hasil["mask"])
print("Range host      :", hasil["host_awal"], "sampai", hasil["host_akhir"])
print("Jumlah host     :", hasil["jumlah_host"])
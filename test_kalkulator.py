from kalkulator import hitung_subnet, bagi_subnet, cek_ip

# Hitung subnet
assert hitung_subnet("192.168.1.0/24")["jumlah_host"] == 254
assert hitung_subnet("192.168.1.0/30")["jumlah_host"] == 2
assert hitung_subnet("192.168.1.0/31")["jumlah_host"] == 2
assert hitung_subnet("192.168.1.5/32")["jumlah_host"] == 1

# Bagi subnet
assert len(bagi_subnet("192.168.1.0/24", 4)) == 4
assert str(bagi_subnet("192.168.1.0/24", 4)[1]) == "192.168.1.64/26"

# Cek IP
assert cek_ip("192.168.1.25", "192.168.1.0/26")["termasuk"] is True
assert cek_ip("192.168.1.100", "192.168.1.0/26")["termasuk"] is False
assert cek_ip("8.8.8.8", "8.8.8.0/24")["jenis"] == "Public"

print("Semua tes lulus")
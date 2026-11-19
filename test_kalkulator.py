
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

# Tes subnet mask biner
assert hitung_subnet("192.168.1.0/24")["mask_biner"] == "11111111.11111111.11111111.00000000"
assert hitung_subnet("10.0.0.0/8")["mask_biner"] == "11111111.00000000.00000000.00000000"
assert hitung_subnet("192.168.1.0/26")["mask_biner"] == "11111111.11111111.11111111.11000000"

# Tes network address biner
assert hitung_subnet("192.168.1.0/24")["network_biner"] == "11000000.10101000.00000001.00000000"

print("Semua tes lulus")

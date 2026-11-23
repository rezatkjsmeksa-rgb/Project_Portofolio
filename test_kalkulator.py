from kalkulator import hitung_subnet, bagi_subnet, cek_ip, konversi_mask, urai_kebutuhan, vlsm

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

# Konversi prefix dan mask
assert str(konversi_mask("24")["mask"]) == "255.255.255.0"
assert konversi_mask("255.255.255.192")["prefix"] == 26
assert konversi_mask("/26")["jumlah_host"] == 62

try:
    konversi_mask("255.255.0.255")
    assert False, "seharusnya error"
except ValueError:
    pass

# VLSM
hasil_vlsm = vlsm("192.168.1.0/24", [("Siswa", 100), ("Guru", 50), ("Lab", 20)])
assert [str(subnet) for nama, host, subnet in hasil_vlsm] == [
    "192.168.1.0/25",
    "192.168.1.128/26",
    "192.168.1.192/27",
]
assert urai_kebutuhan("Guru:50, 20") == [("Guru", 50), ("Subnet 2", 20)]

try:
    vlsm("192.168.1.0/24", [("A", 200), ("B", 100)])
    assert False, "seharusnya error"
except ValueError:
    pass

print("Semua tes lulus")
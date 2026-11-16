import math
import ipaddress


def hitung_subnet(teks):
    jaringan = ipaddress.ip_network(teks, strict=False)
    prefix = jaringan.prefixlen

    if prefix == 32:
        # Satu alamat saja, dipakai sebagai satu host
        host_awal = jaringan.network_address
        host_akhir = jaringan.network_address
        jumlah_host = 1
    elif prefix == 31:
        # Link point-to-point: kedua alamat bisa dipakai host
        host_awal = jaringan.network_address
        host_akhir = jaringan.broadcast_address
        jumlah_host = 2
    else:
        # Kasus umum: alamat pertama = network, terakhir = broadcast
        host_awal = jaringan.network_address + 1
        host_akhir = jaringan.broadcast_address - 1
        jumlah_host = jaringan.num_addresses - 2

    return {
        "network": jaringan.network_address,
        "broadcast": jaringan.broadcast_address,
        "mask": jaringan.netmask,
        "host_awal": host_awal,
        "host_akhir": host_akhir,
        "jumlah_host": jumlah_host,
    }


def bagi_subnet(teks, jumlah):
    jaringan = ipaddress.ip_network(teks, strict=False)
    if jumlah < 2:
        raise ValueError("Jumlah bagian minimal 2")

    tambahan_bit = math.ceil(math.log2(jumlah))
    prefix_baru = jaringan.prefixlen + tambahan_bit
    hasil = list(jaringan.subnets(new_prefix=prefix_baru))
    return hasil[:jumlah]


def cek_ip(ip_teks, jaringan_teks):
    alamat = ipaddress.ip_address(ip_teks.strip())
    jaringan = ipaddress.ip_network(jaringan_teks, strict=False)
    return {
        "termasuk": alamat in jaringan,
        "jenis": "Private" if alamat.is_private else "Public",
    }
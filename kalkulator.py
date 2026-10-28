import math
import ipaddress


def hitung_subnet(teks):
    jaringan = ipaddress.ip_network(teks, strict=False)
    return {
        "network": jaringan.network_address,
        "broadcast": jaringan.broadcast_address,
        "mask": jaringan.netmask,
        "host_awal": jaringan.network_address + 1,
        "host_akhir": jaringan.broadcast_address - 1,
        "jumlah_host": jaringan.num_addresses - 2,
    }


def bagi_subnet(teks, jumlah):
    jaringan = ipaddress.ip_network(teks, strict=False)
    if jumlah < 2:
        raise ValueError("Jumlah bagian minimal 2")

    tambahan_bit = math.ceil(math.log2(jumlah))
    prefix_baru = jaringan.prefixlen + tambahan_bit
    hasil = list(jaringan.subnets(new_prefix=prefix_baru))
    return hasil[:jumlah]
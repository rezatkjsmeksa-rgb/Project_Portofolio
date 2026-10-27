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
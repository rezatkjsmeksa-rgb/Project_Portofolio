import math
import ipaddress


def hitung_host(jaringan):
    prefix = jaringan.prefixlen
    if prefix == 32:
        return 1
    if prefix == 31:
        return 2
    return jaringan.num_addresses - 2


def ke_biner(alamat):
    return ".".join(format(oktet, "08b") for oktet in alamat.packed)


def hitung_subnet(teks):
    jaringan = ipaddress.ip_network(teks, strict=False)
    prefix = jaringan.prefixlen

    if prefix == 32:
        # Satu alamat saja, dipakai sebagai satu host
        host_awal = jaringan.network_address
        host_akhir = jaringan.network_address
    elif prefix == 31:
        # Link point-to-point: kedua alamat bisa dipakai host
        host_awal = jaringan.network_address
        host_akhir = jaringan.broadcast_address
    else:
        # Kasus umum: alamat pertama = network, terakhir = broadcast
        host_awal = jaringan.network_address + 1
        host_akhir = jaringan.broadcast_address - 1

    return {
        "network": jaringan.network_address,
        "broadcast": jaringan.broadcast_address,
        "mask": jaringan.netmask,
        "host_awal": host_awal,
        "host_akhir": host_akhir,
        "jumlah_host": hitung_host(jaringan),
        "network_biner": ke_biner(jaringan.network_address),
        "mask_biner": ke_biner(jaringan.netmask),
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


def konversi_mask(teks):
    teks = teks.strip().lstrip("/")
    jaringan = ipaddress.IPv4Network("0.0.0.0/" + teks)
    return {
        "prefix": jaringan.prefixlen,
        "mask": jaringan.netmask,
        "mask_biner": ke_biner(jaringan.netmask),
        "jumlah_host": hitung_host(jaringan),
    }


def urai_kebutuhan(teks):
    daftar = []
    for nomor, bagian in enumerate(teks.split(","), start=1):
        bagian = bagian.strip()
        if bagian == "":
            continue
        if ":" in bagian:
            nama, jumlah = bagian.split(":", 1)
            nama = nama.strip()
        else:
            nama, jumlah = f"Subnet {nomor}", bagian
        daftar.append((nama, int(jumlah)))
    return daftar


def vlsm(jaringan_teks, daftar_kebutuhan):
    jaringan = ipaddress.IPv4Network(jaringan_teks, strict=False)
    if not daftar_kebutuhan:
        raise ValueError("Isi kebutuhan host dulu")

    urut = sorted(daftar_kebutuhan, key=lambda item: item[1], reverse=True)
    alamat_sekarang = int(jaringan.network_address)
    batas = int(jaringan.broadcast_address)
    hasil = []

    for nama, host in urut:
        if host < 1:
            raise ValueError("Kebutuhan host minimal 1")
        bit_host = math.ceil(math.log2(host + 2))
        ukuran = 2 ** bit_host
        if alamat_sekarang + ukuran - 1 > batas:
            raise ValueError("Jaringan tidak cukup untuk semua kebutuhan")
        subnet = ipaddress.IPv4Network((alamat_sekarang, 32 - bit_host))
        hasil.append((nama, host, subnet))
        alamat_sekarang += ukuran

    return hasil
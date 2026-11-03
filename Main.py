from kalkulator import hitung_subnet, bagi_subnet, cek_ip
from database import buat_tabel, simpan, ambil_riwayat, hapus_semua


def hitung():
    ip = input("Masukkan IP dan prefix (contoh 192.168.1.0/24): ")
    try:
        hasil = hitung_subnet(ip)
    except ValueError:
        print("Input tidak valid, contoh yang benar: 192.168.1.0/24")
        return

    print("Network address :", hasil["network"])
    print("Broadcast       :", hasil["broadcast"])
    print("Subnet mask     :", hasil["mask"])
    print("Range host      :", hasil["host_awal"], "sampai", hasil["host_akhir"])
    print("Jumlah host     :", hasil["jumlah_host"])

    simpan(ip, hasil)
    print("(Hasil disimpan ke riwayat)")


def bagi():
    ip = input("Masukkan IP dan prefix (contoh 192.168.1.0/24): ")
    try:
        jumlah = int(input("Dibagi jadi berapa subnet? "))
        daftar = bagi_subnet(ip, jumlah)
    except ValueError:
        print("Input tidak valid, cek IP dan jumlah subnetnya.")
        return

    for nomor, subnet in enumerate(daftar, start=1):
        print(nomor, ".", subnet, "| host:", subnet.num_addresses - 2)


def cek():
    ip = input("Masukkan alamat IP yang dicek (contoh 192.168.1.25): ")
    jaringan = input("Masukkan jaringan (contoh 192.168.1.0/26): ")
    try:
        hasil = cek_ip(ip, jaringan)
    except ValueError:
        print("Input tidak valid, cek penulisan IP dan jaringannya.")
        return

    if hasil["termasuk"]:
        print("IP ini TERMASUK dalam jaringan tersebut.")
    else:
        print("IP ini TIDAK termasuk dalam jaringan tersebut.")
    print("Jenis IP :", hasil["jenis"])


def lihat_riwayat():
    data = ambil_riwayat()
    if not data:
        print("Riwayat masih kosong.")
        return

    print("\n10 perhitungan terakhir:")
    for waktu, ip, network, broadcast, host in data:
        print(waktu, "|", ip, "| network:", network, "| broadcast:", broadcast, "| host:", host)


def hapus_riwayat():
    yakin = input("Hapus semua riwayat? (y/n): ")
    if yakin.lower() == "y":
        hapus_semua()
        print("Riwayat berhasil dihapus.")
    else:
        print("Dibatalkan.")


def menu():
    while True:
        print("\n===== SUBNET CALCULATOR =====")
        print("1. Hitung Subnet")
        print("2. Bagi Subnet")
        print("3. Cek IP dalam Subnet")
        print("4. Lihat Riwayat")
        print("5. Hapus Riwayat")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            hitung()
        elif pilihan == "2":
            bagi()
        elif pilihan == "3":
            cek()
        elif pilihan == "4":
            lihat_riwayat()
        elif pilihan == "5":
            hapus_riwayat()
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


buat_tabel()
menu()
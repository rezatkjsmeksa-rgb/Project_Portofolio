from kalkulator import hitung_subnet, bagi_subnet
from database import buat_tabel, simpan, ambil_riwayat


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


def lihat_riwayat():
    data = ambil_riwayat()
    if not data:
        print("Riwayat masih kosong.")
        return

    print("\n10 perhitungan terakhir:")
    for waktu, ip, network, broadcast, host in data:
        print(waktu, "|", ip, "| network:", network, "| broadcast:", broadcast, "| host:", host)


def menu():
    while True:
        print("\n===== SUBNET CALCULATOR =====")
        print("1. Hitung Subnet")
        print("2. Bagi Subnet")
        print("3. Lihat Riwayat")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            hitung()
        elif pilihan == "2":
            bagi()
        elif pilihan == "3":
            lihat_riwayat()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


buat_tabel()
menu()
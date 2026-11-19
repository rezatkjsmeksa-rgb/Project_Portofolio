
import csv

from kalkulator import hitung_subnet, bagi_subnet, cek_ip, hitung_host
from database import buat_tabel, simpan, ambil_riwayat, hapus_semua, ambil_semua


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
    print("Network (biner) :", hasil["network_biner"])
    print("Mask (biner)    :", hasil["mask_biner"])

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
        print(nomor, ".", subnet, "| host:", hitung_host(subnet))


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


def ekspor_csv():
    data = ambil_semua()
    if not data:
        print("Riwayat masih kosong, tidak ada yang diekspor.")
        return

    nama_file = input("Nama file (tekan Enter untuk riwayat_subnet.csv): ")
    if nama_file.strip() == "":
        nama_file = "riwayat_subnet.csv"
    if not nama_file.endswith(".csv"):
        nama_file += ".csv"

    with open(nama_file, "w", newline="", encoding="utf-8") as berkas:
        penulis = csv.writer(berkas)
        penulis.writerow(["Waktu", "Input", "Network", "Broadcast", "Jumlah Host"])
        penulis.writerows(data)
    print("Riwayat berhasil diekspor ke", nama_file)


def menu():
    while True:
        print("\n===== SUBNET CALCULATOR =====")
        print("1. Hitung Subnet")
        print("2. Bagi Subnet")
        print("3. Cek IP dalam Subnet")
        print("4. Lihat Riwayat")
        print("5. Hapus Riwayat")
        print("6. Ekspor Riwayat ke CSV")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

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
            ekspor_csv()
        elif pilihan == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


buat_tabel()
menu()

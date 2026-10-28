from kalkulator import hitung_subnet, bagi_subnet


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


def menu():
    while True:
        print("\n===== SUBNET CALCULATOR =====")
        print("1. Hitung Subnet")
        print("2. Bagi Subnet")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            hitung()
        elif pilihan == "2":
            bagi()
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


menu()
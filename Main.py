from kalkulator import hitung_subnet


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


def menu():
    while True:
        print("\n===== SUBNET CALCULATOR =====")
        print("1. Hitung Subnet")
        print("2. Keluar")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            hitung()
        elif pilihan == "2":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


menu()
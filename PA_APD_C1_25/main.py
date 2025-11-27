# main.py
from auth import register, login
from admin import admin_menu
from customer import tampilan_menu_customer, lihat_tiket_merchandise, pesanan_tiket_merchandise, hapus_dari_keranjang
from customer import pilih_opsi_selanjutnya, pilih_opsi_selanjutnya_p2, keranjang_customer, lihat_keranjang, update_keranjang
from prettytable import PrettyTable

def show_menu():
    table = PrettyTable()
    table.field_names = ["No", "Menu"]
    table.add_row(["1", "Registrasi"])
    table.add_row(["2", "Login"])
    table.add_row(["3", "Keluar"])
    table.title = "Official Store MotoGP"
    print(table)

def show_login_menu():
    print()
    table = PrettyTable()
    table.field_names = ["No", "Login Sebagai"]
    table.add_row(["1", "Admin"])
    table.add_row(["2", "Customer"])
    table.add_row(["3", "Kembali"])
    table.title = "Pilih Login"
    print(table)

def input_aman(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print()
            print("===| Pilihan Kosong, Silakan Coba Lagi! |===")
            print()
        else:
            return value

def main():
    Login = False
    Role = None
    current_username = None

    while True:
        if not Login:
            show_menu()
            Pilihan = input_aman("Masukkan Pilihan Anda -> ")

            if Pilihan == '1':
                print()
                print("===| Registrasi Pengguna Baru |===")
                username = input_aman("Masukkan Username Anda: ")
                password = input_aman("Masukkan Password Anda: ")
                success, msg = register(username, password)
                print(msg)

            elif Pilihan == '2':
                while True:
                    show_login_menu()
                    login_Pilihan = input("Masukkan Pilihan Anda -> ").strip()
                    if login_Pilihan == "":
                        print("===| Pilihan Kosong, Silakan Coba Lagi! |===")
                        continue
                    if login_Pilihan == '1':
                        role = "admin"
                        break
                    elif login_Pilihan == '2':
                        role = "customer"
                        break
                    elif login_Pilihan == '3':
                        print()
                        print("===| Kembali Ke Menu Utama |===")
                        break
                    else:
                        print()
                        print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")

                if login_Pilihan == '3':
                    continue

                print()
                print(f"===| Login Sebagai {role.capitalize()} |===")
                username = input_aman("Masukkan Username Anda: ")
                password = input_aman("Masukkan Password Anda: ")
                success, msg, Role = login(username, password)
                if success and Role == role:
                    print(msg)
                    Login = True
                    current_username = username
                else:
                    print(msg)

            elif Pilihan == '3':
                print()
                print("===| Terima Kasih Telah Menggunakan Official Store MotoGP! |===")
                print()
                break
            else:
                print()
                print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")

        elif Login:
            if Role == "admin":
                admin_menu()
                admin_Pilihan = input("Masukkan Pilihan Anda -> ").strip()
                if admin_Pilihan == "":
                    print("===| Pilihan Kosong, Silakan Coba Lagi! |===")
                    continue
                if admin_Pilihan == '9':
                    print()
                    print("===| Kembali Ke Menu Utama |===")
                    Login = False
                    Role = None
                    continue
                else:
                    print()
                    print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")

            elif Role == "customer":
                tampilan_menu_customer()
                customer_Pilihan = input("Masukkan Pilihan Anda -> ").strip()
                if customer_Pilihan == "":
                    print()
                    print("===| Pilihan Kosong, Silakan Coba Lagi! |===")
                    continue
                if customer_Pilihan == '1':
                    print()
                    lihat_tiket_merchandise()
                    hasil = pilih_opsi_selanjutnya() 
                    if hasil == "kembali":
                        continue
                elif customer_Pilihan == '2':
                    while True:
                        print()
                        lihat_tiket_merchandise()
                        pesanan_tiket_merchandise(current_username)  
                        hasil = pilih_opsi_selanjutnya_p2() 
                        if hasil == "kembali":
                            break
                        elif hasil == "lanjut":
                            continue
                elif customer_Pilihan == '3':  
                    while True:
                        keranjang_customer()
                        pilih = input("Pilih menu keranjang -> ").strip()
                        if pilih == '1':
                            lihat_keranjang(current_username)
                            # === Tambahkan opsi ubah/hapus setelah lihat keranjang ===
                            print("\n===| Pilih Opsi Berikut |===")
                            print("1. Ubah Jumlah Item")
                            print("2. Hapus Item dari Keranjang")
                            print("3. Kembali ke Menu Keranjang")
                            while True:
                                sub_pilih = input("Masukkan Pilihan Anda -> ").strip()
                                if sub_pilih == '1':
                                    try:
                                        nomor = int(input("Masukkan nomor item: "))
                                        jumlah_baru = int(input("Masukkan jumlah baru: "))
                                        success, msg = update_jumlah_item_keranjang(current_username, nomor, jumlah_baru)
                                        print()
                                        print(msg)
                                    except ValueError:
                                        print()
                                        print("❌ Input tidak valid!")
                                elif sub_pilih == '2':
                                    try:
                                        nomor = int(input("Masukkan nomor item: "))
                                        success, msg = hapus_dari_keranjang(current_username, nomor)
                                        print()
                                        print(msg)
                                    except ValueError:
                                        print()
                                        print("❌ Input tidak valid!")
                                elif sub_pilih == '3':
                                    print()
                                    print("===| Kembali ke Menu Keranjang |===")
                                    break
                                else:
                                    print()
                                    print("❌ Pilihan tidak valid!")
                        elif pilih == '2':
                            lihat_keranjang(current_username)
                            try:
                                nomor = int(input("Masukkan nomor item yang dihapus: "))
                                success, msg = hapus_dari_keranjang(current_username, nomor)
                                print()
                                print(msg)
                            except ValueError:
                                print()
                                print("❌ Input tidak valid!")
                        elif pilih == '3':
                            break  # Kembali ke menu customer
                        else:
                            print()
                            print("❌ Pilihan tidak valid!")
                elif customer_Pilihan == '4':
                    print()
                elif customer_Pilihan == '5':
                    print()
                elif customer_Pilihan == '6':
                    print()
                    print("===| Kembali Ke Menu Utama |===")
                    Login = False
                    Role = None
                else:
                    print()
                    print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")

if __name__ == "__main__":
    main()
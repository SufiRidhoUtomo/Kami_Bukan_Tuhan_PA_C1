from auth import register, login, clear
from admin import admin_menu
from customer import (
    tampilan_menu_customer, lihat_tiket_merchandise, pesanan_tiket_merchandise,
    keranjang_customer, lihat_keranjang, pilih_opsi_selanjutnya,
    pilih_opsi_selanjutnya_p2, hapus_dari_keranjang
)
from prettytable import PrettyTable

def show_menu():
    clear()
    table = PrettyTable()
    table.field_names = ["No", "Menu"]
    table.add_row(["1", "Registrasi"])
    table.add_row(["2", "Login"])
    table.add_row(["3", "Keluar"])
    table.title = "Official Store MotoGP"
    print(table)

def show_login_menu():
    clear()
    table = PrettyTable()
    table.field_names = ["No", "Login Sebagai"]
    table.add_row(["1", "Admin"])
    table.add_row(["2", "Customer"])
    table.add_row(["3", "Kembali"])
    table.title = "Pilih Login"
    print(table)

def main():
    Login = False
    Role = None
    current_username = None

    while True:
        if not Login:
            show_menu()
            Pilihan = input("Masukkan Pilihan Anda -> ")

            if Pilihan == '1':
                print()
                print("===| Registrasi Pengguna Baru |===")
                username = input("Masukkan Username Anda: ")
                password = input("Masukkan Password Anda: ")
                success, msg = register(username, password)
                print(msg)

            elif Pilihan == '2':
                while True:
                    show_login_menu()
                    login_Pilihan = input("Masukkan Pilihan Anda -> ").strip()

                    if login_Pilihan == '1':
                        role = "admin"
                        break
                    elif login_Pilihan == '2':
                        role = "customer"
                        break
                    elif login_Pilihan == '3':
                        role = None  
                        break
                    else:
                        print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")
                        continue  
                
                if role is None:
                    print("===| Kembali Ke Menu Utama |===")
                    continue 
                
                print()
                print(f"===| Login Sebagai {role.capitalize()} |===")
                username = input("Masukkan Username Anda: ")
                password = input("Masukkan Password Anda: ")

                success, msg, returned_role = login(username, password)

                if success and returned_role == role:
                    print(msg)
                    Login = True
                    Role = returned_role
                    current_username = username
                else:
                    print(msg)

            elif Pilihan == '3':
                print("===| Terima Kasih Telah Menggunakan Official Store MotoGP! |===")
                break
            else:
                print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")

        elif Login:
            if Role == "admin":
                admin_menu()
                admin_Pilihan = input("Masukkan Pilihan Anda -> ").strip()
                if admin_Pilihan == '9':
                    print("===| Kembali Ke Menu Utama |===")
                    Login = False
                    Role = None
                else:
                    print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")

            elif Role == "customer": 
                while True:  
                    tampilan_menu_customer()
                    customer_Pilihan = input("Masukkan Pilihan Anda -> ").strip()
                    
                    if customer_Pilihan == '1':
                        lihat_tiket_merchandise()
                        pilih_opsi_selanjutnya()  
                    
                    elif customer_Pilihan == '2':
                        while True:
                            lihat_tiket_merchandise()
                            pesanan_tiket_merchandise(current_username)
                            hasil = pilih_opsi_selanjutnya_p2()
                            if hasil == "kembali":
                                break
                            
                    elif customer_Pilihan == '3':
                        while True:
                            keranjang_customer()
                            pilih = input("Pilih menu keranjang -> ").strip()
                            if pilih == '1':
                                lihat_keranjang(current_username)
                            elif pilih == '2':
                                lihat_keranjang(current_username)
                                try:
                                    nomor = int(input("Nomor Item yang Dihapus -> "))
                                    success, msg = hapus_dari_keranjang(current_username, nomor)
                                    print(msg)
                                except ValueError:
                                    print("===| Input Tidak Valid! |===")
                            elif pilih == '3':
                                break
                            else:
                                print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")
                    
                    elif customer_Pilihan == '6':
                        print("===| Kembali Ke Menu Utama |===")
                        Login = False
                        Role = None
                        break  
                    
                    else:
                        print("===| Fitur Belum Tersedia |===")

if __name__ == "__main__":
    main()
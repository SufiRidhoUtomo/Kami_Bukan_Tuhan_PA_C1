from auth import register, login
from admin import show_all_users
from customer import show_customer_menu
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
    table = PrettyTable()
    table.field_names = ["No", "Login Sebagai"]
    table.add_row(["1", "Admin"])
    table.add_row(["2", "Customer"])
    table.add_row(["3", "Kembali"])
    table.title = "Pilih Login"
    print(table)

def main():
    logged_in = False
    user_role = None

    while True:
        if not logged_in:
            show_menu()
            choice = input("Pilih menu: ")

            if choice == '1':
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                success, msg = register(username, password)
                print(msg)

            elif choice == '2':
                while True:
                    show_login_menu()
                    login_choice = input("Pilih login: ")
                    if login_choice == '1':
                        role = "admin"
                        break
                    elif login_choice == '2':
                        role = "customer"
                        break
                    elif login_choice == '3':
                        break
                    else:
                        print("Pilihan tidak valid.")
                else:
                    continue

                username = input("Username: ")
                password = input("Password: ")
                success, msg, user_role = login(username, password)
                if success and user_role == role:
                    print(msg)
                    logged_in = True
                else:
                    print(msg)

            elif choice == '3':
                print("Keluar dari program.")
                break

            else:
                print("Pilihan tidak valid.")

        else:
            if user_role == "admin":
                print("\n=== Menu Admin ===")
                print("1. Lihat Daftar Pengguna")
                print("2. Logout")
                admin_choice = input("Pilih menu: ")
                if admin_choice == '1':
                    show_all_users()
                elif admin_choice == '2':
                    logged_in = False
                    user_role = None
                    print("Berhasil logout.")
                else:
                    print("Pilihan tidak valid.")

            elif user_role == "customer":
                show_customer_menu()
                customer_choice = input("Pilih menu: ")
                if customer_choice == '4':
                    logged_in = False
                    user_role = None
                    print("Berhasil logout.")
                else:
                    print("Fitur belum tersedia.")

if __name__ == "__main__":
    main()
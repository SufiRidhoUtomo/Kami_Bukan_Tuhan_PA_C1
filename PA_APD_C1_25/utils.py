from tabulate import tabulate
import os

def clear_screen():
    """Membersihkan layar konsol"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    """Mencetak header dengan garis"""
    print("=" * 50)
    print(f"{text:^50}")
    print("=" * 50)

def get_valid_input(prompt, validation_func, error_msg):
    """Mendapatkan input yang valid dari user"""
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print(error_msg)

def print_table(data, headers):
    """Mencetak tabel menggunakan tabulate"""
    if not data:
        print("Tidak ada data untuk ditampilkan")
        return
    print(tabulate(data, headers=headers, tablefmt="grid", stralign="center"))

def input_integer(prompt, min_val=None, max_val=None):
    """Input integer dengan validasi"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Nilai minimal adalah Rp {min_val:,}")
                continue
            if max_val is not None and value > max_val:
                print(f"Nilai maksimal adalah Rp {max_val:,}")
                continue
            return value
        except ValueError:
            print("Input harus berupa angka")

def input_float(prompt, min_val=None, max_val=None):
    """Input float dengan validasi"""
    while True:
        try:
            value = float(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Nilai harus antara {min_val} dan {max_val}")
                continue
            return value
        except ValueError:
            print("Input harus berupa angka")

def pause():
    """Pause untuk menunggu input user"""
    input("\nTekan Enter untuk melanjutkan...")
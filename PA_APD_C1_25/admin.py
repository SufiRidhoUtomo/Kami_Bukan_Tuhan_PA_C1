import json
import os
from prettytable import PrettyTable
from auth import clear

Simpan_Data = "data.json"

def load_data():
    if not os.path.exists(Simpan_Data):
        default_data = {
            "tickets": [],
            "merchandise": [],
            "transactions": []
        }
        save_data(default_data)
    with open(Simpan_Data, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(Simpan_Data, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def admin_menu():
    clear()
    table = PrettyTable()
    table.field_names = ["No", "Menu Admin"]
    table.add_row(["1", "Tambah Tiket/Merchandise"])
    table.add_row(["2", "Ubah Harga Tiket/Merchandise"])
    table.add_row(["3", "Hapus Tiket/Merchandise"])
    table.add_row(["4", "Lihat Registrasi Customer"])
    table.add_row(["5", "Lihat Pesanan Customer"])
    table.add_row(["6", "Ubah Transaksi Customer"])
    table.add_row(["7", "Lihat Pesanan Customer"])
    table.add_row(["8", "Lihat Jumlah Transaksi dan Pendapatan"])
    table.add_row(["9", "Kembali"])
    table.title = "Official Store MotoGP"
    print(table)

def _tampilkan_daftar(items, kategori):
    if not items:
        print(f"\nBelum ada {kategori}.")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Stok", "Harga"]
    for item in items:
        table.add_row([
            item["id"],
            item["name"],
            item["stock"],
            f"Rp{item['price']:,}"
        ])
    print(f"DAFTAR {kategori.upper()}")
    print(table)

def tambah_stok():
    data = load_data()
    print("[1] Tiket")
    print("[2] Merchandise")
    pilih = input("Pilih kategori: ").strip()

    if pilih == '1':
        items = data["tickets"]
        kategori = "tiket"
    elif pilih == '2':
        items = data["merchandise"]
        kategori = "merchandise"
    else:
        print("Pilihan tidak valid!")
        return

    _tampilkan_daftar(items, kategori)

    try:
        item_id = int(input(f"\nMasukkan ID {kategori} yang akan ditambah stoknya: "))
        item = next((x for x in items if x["id"] == item_id), None)
        if not item:
            print(f"{kategori.capitalize()} dengan ID tersebut tidak ditemukan!")
            return

        tambah = int(input("Jumlah stok yang ditambahkan: "))
        if tambah <= 0:
            print("Jumlah harus lebih dari 0!")
            return

        item["stock"] += tambah
        save_data(data)
        print(f"Stok '{item['name']}' berhasil ditambah menjadi {item['stock']}.")

    except ValueError:
        print("Input tidak valid!")

def kurangi_stok():
    data = load_data()
    print("[1] Tiket")
    print("[2] Merchandise")
    pilih = input("Pilih kategori: ").strip()

    if pilih == '1':
        items = data["tickets"]
        kategori = "tiket"
    elif pilih == '2':
        items = data["merchandise"]
        kategori = "merchandise"
    else:
        print("Pilihan tidak valid!")
        return

    _tampilkan_daftar(items, kategori)

    try:
        item_id = int(input(f"ID {kategori} yang diambil: "))
        item = next((x for x in items if x["id"] == item_id), None)
        if not item:
            print("Barang tidak ditemukan!")
            return

        jumlah = int(input("Jumlah yang diambil: "))
        if jumlah <= 0 or jumlah > item["stock"]:
            print("Jumlah tidak valid atau melebihi stok!")
            return

        item["stock"] -= jumlah
        save_data(data)
        print(f"Stok '{item['name']}' sekarang: {item['stock']}")

    except ValueError:
        print("Input tidak valid!")

def lihat_barang():
    data = load_data()
    print("" + "="*60)

    if data["tickets"]:
        table_tiket = PrettyTable()
        table_tiket.field_names = ["ID", "Nama Tiket", "Stok", "Harga"]
        for t in data["tickets"]:
            table_tiket.add_row([t["id"], t["name"], t["stock"], f"Rp{t['price']:,}"])
        print("TIKET MOTOGP")
        print(table_tiket)
    else:
        print("TIKET: Belum ada data.")

    if data["merchandise"]:
        table_merch = PrettyTable()
        table_merch.field_names = ["ID", "Nama Merchandise", "Stok", "Harga"]
        for m in data["merchandise"]:
            table_merch.add_row([m["id"], m["name"], m["stock"], f"Rp{m['price']:,}"])
        print("MERCHANDISE")
        print(table_merch)
    else:
        print("MERCHANDISE: Belum ada data.")

def lihat_customer():
    data = load_data()
    if not data["users"]:
        print("Belum ada customer terdaftar.")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Username", "Role", "Saldo"]
    for u in data["users"]:
        table.add_row([u["id"], u["username"], u["role"], f"Rp{u['balance']:,}"])
    print("DAFTAR PENGGUNA")
    print(table)

def lihat_transaksi():
    data = load_data()
    if not data["transactions"]:
        print("Belum ada transaksi.")
        return

    table = PrettyTable()
    table.field_names = ["ID Transaksi", "User", "Item", "Jumlah", "Total", "Tipe"]
    for t in data["transactions"]:
        table.add_row([
            t["id_transaksi"],
            t["username"],
            t["item_nama"],
            t["jumlah"],
            f"Rp{t['total_harga']:,}",
            t["tipe"]
        ])
    print("RIWAYAT TRANSAKSI")
    print(table)
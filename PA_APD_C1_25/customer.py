import os
import json
from prettytable import PrettyTable
from auth import clear

Simpan_Data = "data.json"

def load_data():
    if not os.path.exists(Simpan_Data):
        print(f"File '{Simpan_Data}' tidak ditemukan. Membuat file baru...")
        default_data = {
            "users": {},
            "tickets": [],
            "merchandise": [],
            "orders": [],
            "balances": {}
        }
        save_data(default_data)
    
    with open(Simpan_Data, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(Simpan_Data, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def tampilan_menu_customer():
    clear()
    table = PrettyTable()
    table.field_names = ["No", "Menu Customer"]
    table.add_row(["1", "Lihat Tiket/Merchandise"])
    table.add_row(["2", "Pesan Tiket/Merchandise"])
    table.add_row(["3", "Lihat dan Ubah Keranjang Belanja"])
    table.add_row(["4", "Bayar Pesanan"])
    table.add_row(["5", "Top Up Saldo"])
    table.add_row(["6", "Kembali"])
    table.title = "Official Store MotoGP"
    print(table)

def lihat_tiket_merchandise():
    clear()
    data = load_data()

    t1 = PrettyTable()
    t1.field_names = ["ID", "Nama Tiket", "Harga", "Stok"]
    for t in data["tickets"]:
        t1.add_row([t["id"], t["name"], f"Rp{t['price']:,}", t["stock"]])
    t1.title = "Daftar Tiket MotoGP"
    print(t1)

    t2 = PrettyTable()
    t2.field_names = ["ID", "Nama Merchandise", "Harga", "Stok"]
    for m in data["merchandise"]:
        t2.add_row([m["id"], m["name"], f"Rp{m['price']:,}", m["stock"]])
    t2.title = "Daftar Merchandise MotoGP"
    print(t2)

def pilih_opsi_selanjutnya():
    print()
    print("===| Klik ENTER Untuk Kembali |===")
    return enter_to_continue()

def pilih_opsi_selanjutnya_p2():
    print()
    print("===| Pilih Opsi Berikut |===")
    print("1. Tambah Pesanan Lain")
    print("2. Kembali ke Menu Customer")
    while True:
        pilihan = input("Masukkan Pilihan Anda -> ").strip()
        if pilihan == '1':
            return "lanjut"
        elif pilihan == '2':
            print()
            print("===| Kembali ke Menu Customer |===")
            return "kembali"
        else:
            print()
            print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")

def pesanan_tiket_merchandise(username):
    print()
    print("===| Pemesanan Tiket |===")
    try:
        item_id = int(input("Masukkan ID Tiket -> "))
        jumlah = int(input("Jumlah -> "))
        if 1 <= item_id <= 5:
            success, msg = update_keranjang(username, item_id, jumlah, "ticket")
            print("===| Tiket Berhasil Ditambahkan ke Keranjang! |===")
            print(msg)
        else:
            print("===| ID Tiket Tidak Valid! |===")
    except ValueError:
        print("===| Input Tidak Valid! |===")
        return

    print()
    print("===| Pemesanan Merchandise |===")
    try:
        item_id = int(input("Masukkan ID Merchandise -> "))
        jumlah = int(input("Jumlah -> "))
        if 6 <= item_id <= 10:
            success, msg = update_keranjang(username, item_id, jumlah, "merchandise")
            print("===| Merchandise Berhasil Ditambahkan ke Keranjang! |===")
            print(msg)
        else:
            print("===| ID Merchandise Tidak Valid! |===")
    except ValueError:
        print("===| Input Tidak Valid! |===")

def keranjang_customer():
    clear()
    table = PrettyTable()
    table.field_names = ["No", "Menu Keranjang"]
    table.add_row(["1", "Lihat Isi Keranjang"])
    table.add_row(["2", "Hapus Item dari Keranjang"])
    table.add_row(["3", "Kembali"])
    table.title = "Menu Keranjang"
    print(table)

def lihat_keranjang(username):
    data = load_data()
    if username not in data["users"]:
        print("===| Username Tidak Ditemukan! |===")
        return

    user = data["users"][username]
    if user.get("role") != "customer":
        print("===| Hanya Customer yang Bisa Mengakses Keranjang! |===")
        return

    cart = user.get("cart", [])
    if not cart:
        clear()
        print("===| Keranjang Anda Kosong |===")
        return

    table = PrettyTable()
    table.field_names = ["No", "Nama", "Harga", "Qty", "Total"]
    total = 0
    for i, item in enumerate(cart, 1):
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        table.add_row([i, item["name"], f"Rp{item['price']:,}", item["quantity"], f"Rp{subtotal:,}"])
    
    clear()
    print("===| Isi Keranjang Anda |===")
    print(table)
    print(f"===| Total: Rp{total:,} |===")

    print()
    print("===| Pilih Opsi Berikut |===")
    print("1. Ubah Jumlah Item")
    print("2. Hapus Item dari Keranjang")
    print("3. Kembali ke Menu Keranjang")
    while True:
        pilihan = input("Masukkan Pilihan Anda -> ").strip()
        if pilihan == '1':
            try:
                nomor = int(input("Nomor Item -> "))
                jumlah_baru = int(input("Jumlah Baru -> "))
                success, msg = update_jumlah_item_keranjang(username, nomor, jumlah_baru)
                print()
                print(msg)
            except ValueError:
                print("===| Input Tidak Valid! |===")
        elif pilihan == '2':
            try:
                nomor = int(input("Nomor Item -> "))
                success, msg = hapus_dari_keranjang(username, nomor)
                print()
                print(msg)
            except ValueError:
                print("===| Input Tidak Valid! |===")
        elif pilihan == '3':
            print("===| Kembali ke Menu Keranjang |===")
            break
        else:
            print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")

def hapus_dari_keranjang(username, nomor_item):
    data = load_data()
    if username not in data["users"]:
        return False, "===| Username Tidak Ditemukan! |==="

    user = data["users"][username]
    if user.get("role") != "customer":
        return False, "===| Hanya Customer yang Bisa Mengakses Keranjang! |==="

    cart = user.get("cart", [])
    if not cart:
        return False, "===| Keranjang Anda Kosong |==="

    if nomor_item < 1 or nomor_item > len(cart):
        return False, "===| Nomor Item Tidak Valid! |==="

    item = cart.pop(nomor_item - 1)
    item_type = item["type"]
    item_id = item["item_id"]

    if item_type == "ticket":
        for t in data["tickets"]:
            if t["id"] == item_id:
                t["stock"] += item["quantity"]
                break
    else:
        for m in data["merchandise"]:
            if m["id"] == item_id:
                m["stock"] += item["quantity"]
                break

    user["cart"] = cart
    save_data(data)
    return True, f"===| {item['name']} x{item['quantity']} Dihapus dari Keranjang! Stok Sekarang: {t['stock'] if item_type == 'ticket' else m['stock']} |==="

def update_keranjang(username, item_id, jumlah_baru, item_type):
    if jumlah_baru <= 0:
        return hapus_item_dari_keranjang_berdasarkan_id(username, item_id, item_type)

    data = load_data()
    if username not in data["users"]:
        return False, "===| Username Tidak Ditemukan! |==="

    user = data["users"][username]
    if user.get("role") != "customer":
        return False, "===| Hanya Customer yang Bisa Mengakses Keranjang! |==="

    # Pilih daftar
    if item_type == "ticket":
        items = data["tickets"]
    elif item_type == "merchandise":
        items = data["merchandise"]
    else:
        return False, "===| Jenis Item Tidak Valid! |==="

    target = None
    for item in items:
        if item["id"] == item_id:
            target = item
            break
    if not target:
        return False, "===| Item Tidak Ditemukan! |==="

    if target["stock"] < jumlah_baru:
        return False, f"===| Stok Tidak Cukup! Tersedia: {target['stock']} |==="

    cart = user.get("cart", [])
    existing = None
    for c in cart:
        if c["item_id"] == item_id and c["type"] == item_type:
            existing = c
            break

    if existing:
        selisih = jumlah_baru - existing["quantity"]
        if selisih > 0:
            target["stock"] -= selisih
        elif selisih < 0:
            target["stock"] += abs(selisih)
        existing["quantity"] = jumlah_baru
    else:
        target["stock"] -= jumlah_baru
        cart.append({
            "item_id": item_id,
            "name": target["name"],
            "price": target["price"],
            "quantity": jumlah_baru,
            "type": item_type
        })

    user["cart"] = cart
    save_data(data)
    return True, f"===| {target['name']} x{jumlah_baru} Di Keranjang. Stok: {target['stock']} |==="

def hapus_item_dari_keranjang_berdasarkan_id(username, item_id, item_type):
    data = load_data()
    if username not in data["users"]:
        return False, "===| Username Tidak Ditemukan! |==="

    user = data["users"][username]
    cart = user.get("cart", [])
    for i, item in enumerate(cart):
        if item["item_id"] == item_id and item["type"] == item_type:
            # Kembalikan stok
            if item_type == "ticket":
                for t in data["tickets"]:
                    if t["id"] == item_id:
                        t["stock"] += item["quantity"]
                        break
            else:
                for m in data["merchandise"]:
                    if m["id"] == item_id:
                        m["stock"] += item["quantity"]
                        break
            cart.pop(i)
            user["cart"] = cart
            save_data(data)
            return True, f"===| {item['name']} Dihapus dari Keranjang. Stok Dikembalikan. |==="
    return False, "===| Item Tidak Ditemukan di Keranjang! |==="

def update_jumlah_item_keranjang(username, nomor_item, jumlah_baru):
    data = load_data()
    if username not in data["users"]:
        return False, "===| Username Tidak Ditemukan! |==="

    user = data["users"][username]
    cart = user.get("cart", [])
    if not cart or nomor_item < 1 or nomor_item > len(cart):
        return False, "===| Nomor Item Tidak Valid! |==="

    item = cart[nomor_item - 1]
    return update_keranjang(username, item["item_id"], jumlah_baru, item["type"])

def hapus_item_dari_keranjang_berdasarkan_id(username, item_id, item_type):
    data = load_data()
    if username not in data["users"]:
        return False, "===| Username Tidak Ditemukan! |==="

    user = data["users"][username]
    cart = user.get("cart", [])
    for i, item in enumerate(cart):
        if item["item_id"] == item_id and item["type"] == item_type:
            # Kembalikan stok
            if item_type == "ticket":
                for t in data["tickets"]:
                    if t["id"] == item_id:
                        t["stock"] += item["quantity"]
                        break
            else:
                for m in data["merchandise"]:
                    if m["id"] == item_id:
                        m["stock"] += item["quantity"]
                        break
            cart.pop(i)
            user["cart"] = cart
            save_data(data)
            return True, f"===| {item['name']} Dihapus dari Keranjang. Stok Dikembalikan. |==="
    return False, "===| Item Tidak Ditemukan di Keranjang! |==="

def update_jumlah_item_keranjang(username, nomor_item, jumlah_baru):
    data = load_data()
    if username not in data["users"]:
        return False, "===| Username Tidak Ditemukan! |==="

    user = data["users"][username]
    cart = user.get("cart", [])
    if not cart or nomor_item < 1 or nomor_item > len(cart):
        return False, "===| Nomor Item Tidak Valid! |==="

    item = cart[nomor_item - 1]
    return update_keranjang(username, item["item_id"], jumlah_baru, item["type"])

def enter_to_continue():
    input() 
    return "kembali"
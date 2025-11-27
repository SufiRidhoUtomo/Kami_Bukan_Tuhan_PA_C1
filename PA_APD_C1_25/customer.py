import os
import json
from prettytable import PrettyTable

Simpan_Data = "data.json"

def load_data():
    with open(Simpan_Data, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(Simpan_Data, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def tambah_ke_keranjang(username, item_id, quantity, item_type):
    data = load_data()
    user = None
    for u in data["users"]:
        if u["username"] == username:
            user = u
            break
    if not user:
        print()
        return False, "===| Username Tidak Ditemukan! |==="

    if item_type == "ticket":
        items = data["tickets"]
    elif item_type == "merchandise":
        items = data["merchandise"]
    else:
        print()
        return False, "===| Item Tidak valid! |==="

    item = None
    for x in items:
        if x["id"] == item_id:
            item = x
            break
    if not item:
        print()
        return False, "===| Item Tidak Ditemukan! |==="

    if item["stock"] < quantity:
        print()
        return False, f"Stok Tidak Cukup! Tersedia: {item['stock']}"

    item["stock"] -= quantity

    cart = user.get("cart", [])
    existing = None
    for c in cart:
        if c["item_id"] == item_id and c["type"] == item_type:
            existing = c
            break

    if existing:
        existing["quantity"] += quantity
    else:
        cart.append({
            "item_id": item_id,
            "name": item["name"],
            "price": item["price"],
            "quantity": quantity,
            "type": item_type
        })
    
    user["cart"] = cart
    save_data(data) 
    
    return True, f"{item['name']} x{quantity} Ditambahkan ke Keranjang. Stok Tersedia: {item['stock']}"

def hapus_dari_keranjang(username, nomor_item):
    data = load_data()
    user = None
    for u in data["users"]:
        if u["username"] == username:
            user = u
            break
    if not user:
        print()
        return False, "===| Username Tidak Ditemukan! |==="

    cart = user.get("cart", [])
    if not cart:
        print()
        return False, "===| Keranjang Kosong! |==="

    # Validasi nomor
    if nomor_item < 1 or nomor_item > len(cart):
        print()
        return False, "===| Nomor Item Tidak Valid! |==="

    item = cart.pop(nomor_item - 1)

    if item["type"] == "ticket":
        items = data["tickets"]
    else:
        items = data["merchandise"]
    
    for x in items:
        if x["id"] == item["item_id"]:
            x["stock"] += item["quantity"]
            break

    user["cart"] = cart
    save_data(data)  
    
    return True, f"{item['name']} x{item['quantity']} Item Dihapus dari Keranjang! Stok Sekarang: {x['stock']}"

def show_customer_menu():
    table = PrettyTable()
    table.field_names = ["No", "Menu Customer"]
    table.add_row(["1", "Lihat Tiket"])
    table.add_row(["2", "Lihat Merchandise"])
    table.add_row(["3", "Beli Tiket/Merchandise"])
    table.add_row(["4", "Lihat Keranjang"])
    table.add_row(["5", "Kembali"])
    table.title = "Customer Menu"
    print(table)

def tampilan_menu_customer():
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
    table = PrettyTable()
    table.field_names = ["No", "Tiket", "Harga", "Stok"]
    table.add_row(["1", "General Admission", "115000", "100"])
    table.add_row(["2", "Standard Grandstand", "400000", "100"])
    table.add_row(["3", "Premium Grandstand", "1000000", "100"])
    table.add_row(["4", "VIP Hospitality Suites Deluxe", "10000000", "100"])
    table.add_row(["5", "VIP Hospitality Suites Premium", "12000000", "100"])
    table.title = "Daftar Tiket dan Merchandise MotoGP"
    print(table)

    table = PrettyTable()
    table.field_names = ["No", "Merchandise", "Harga", "Stok"]
    table.add_row(["6", "Jersey Driver dan Team", "300000", "100"])
    table.add_row(["7", "Topi (Caps)", "150000", "100"])
    table.add_row(["8", "Hoodie dan Jaket MotoGP", "500000", "100"])
    table.add_row(["9", "Key Chain", "25000", "100"])
    table.add_row(["10", "Merchandise Eksklusif", "2000000", "100"])
    print(table)

def pilih_opsi_selanjutnya():
    print()
    print("===| Pilih Opsi Berikut |===")
    print("1. Kembali ke Menu Customer")
    input_pilihan = input("Masukkan Pilihan Anda -> ").strip()
    if input_pilihan == '1':
        print()
        print("===| Kembali ke Menu Customer |===")
        return "kembali"  
    else:
        print()
        print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")
        return pilih_opsi_selanjutnya()

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
        item_id = int(input("Masukkan ID Tiket Yang Ingin Dipesan -> "))
        jumlah = int(input("Masukkan Jumlah Tiket Yang Ingin Dipesan -> "))
        success, msg = update_keranjang(username, item_id, jumlah, "ticket")
        print("Tiket Berhasil Ditambahkan ke Keranjang!")
        print(msg)  # opsional
    except ValueError:
        print("===| Input Tidak Valid! |===")
        return

    print("===| Pemesanan Merchandise |===")
    try:
        item_id = int(input("Masukkan ID Merchandise Yang Ingin Dipesan -> "))
        jumlah = int(input("Masukkan Jumlah Merchandise Yang Ingin Dipesan -> "))
        success, msg = update_keranjang(username, item_id, jumlah, "merchandise")
        print("Merchandise Berhasil Ditambahkan ke Keranjang!")
        print(msg)  # opsional
    except ValueError:
        print("===| Input Tidak Valid! |===")

def keranjang_customer():
    table = PrettyTable()
    print()
    table.field_names = ["No", "Menu Keranjang"]
    table.add_row(["1", "Lihat Isi Keranjang"])
    table.add_row(["2", "Hapus Item dari Keranjang"])
    table.add_row(["3", "Kembali"])
    table.title = "Menu Keranjang"
    print(table)

def lihat_keranjang(username):
    data = load_data()
    user = next((u for u in data["users"] if u["username"] == username), None)
    if not user:
        print()
        print("===| Username Tidak Ditemukan! |===")
        return

    cart = user.get("cart", [])
    if not cart:
        print()
        print("===| Keranjang Kosong! |===")
        return

    table = PrettyTable()
    table.field_names = ["No", "Nama", "Harga", "Qty", "Total"]
    total = 0
    for i, item in enumerate(cart, 1):
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        table.add_row([i, item["name"], f"Rp{item['price']:,}", item["quantity"], f"Rp{subtotal:,}"])
    
    print()
    print("===| Isi Keranjang Anda |===")
    print(table)
    print(f"Total: Rp{total:,}\n")

    print("===| Pilih Opsi Berikut |===")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")
    print("3. Kembali ke Menu Keranjang")
    while True:
        pilihan = input("Masukkan Pilihan Anda -> ").strip()
        if pilihan == '1':
            try:
                nomor = int(input("Masukkan Nomor Item -> "))
                success, msg = ubah_stok_dari_keranjang(username, nomor, "tambah")
                print()
                print(msg)
            except ValueError:
                print()
                print("===| Input Tidak Valid! |===")
        elif pilihan == '2':
            try:
                nomor = int(input("MMasukkan Nomor Item -> "))
                success, msg = ubah_stok_dari_keranjang(username, nomor, "kurangi")
                print()
                print(msg)
            except ValueError:
                print()
                print("===| Input Tidak Valid! |===")
        elif pilihan == '3':
            print()
            print("===| Kembali ke Menu Keranjang |===")
            break
        else:
            print()
            print("===| Pilihan Tidak Valid, Silakan Coba Lagi! |===")

def hapus_dari_keranjang(username, nomor_item):
    data = load_data()
    user = next((u for u in data["users"] if u["username"] == username), None)
    if not user:
        print()
        return False, "===| Username Tidak Ditemukan! |==="

    cart = user.get("cart", [])
    if not cart:
        print()
        return False, "===| Keranjang Kosong! |==="

    if nomor_item < 1 or nomor_item > len(cart):
        print()
        return False, "===| Nomor Item Tidak Valid! |==="

    item = cart.pop(nomor_item - 1)  

    if item["type"] == "ticket":
        items = data["tickets"]
    elif item["type"] == "merchandise":
        items = data["merchandise"]
    else:
        print()
        return False, "===| Jenis Barang Tidak Valid! |==="

    for x in items:
        if x["id"] == item["item_id"]:
            x["stock"] += item["quantity"]
            break

    user["cart"] = cart
    save_data(data) 
    
    return True, f"{item['name']} x{item['quantity']} Item Dihapus dari Keranjang! Stok Sekarang: {x['stock']}"

def ubah_stok_dari_keranjang(username, nomor_item, aksi):
    data = load_data() 
    user = next((u for u in data["users"] if u["username"] == username), None)
    if not user:
        print()
        return False, "===| Username Tidak Ditemukan! |==="

    cart = user.get("cart", [])
    if not cart or nomor_item < 1 or nomor_item > len(cart):
        print()
        return False, "===| Nomor Item Tidak Valid! |==="

    item = cart[nomor_item - 1]  

    daftar = data["tickets"] if item["type"] == "ticket" else data["merchandise"]
    barang = next((x for x in daftar if x["id"] == item["item_id"]), None)
    if not barang:
        print()
        return False, "===| Barang Tidak Ditemukan! |==="

    if aksi == "tambah":
        barang["stock"] += item["quantity"]
        msg = f"Stok {barang['name']} Ditambahkan Sebanyak {item['quantity']}. Stok Sekarang: {barang['stock']}"
    elif aksi == "kurangi":
        if barang["stock"] < item["quantity"]:
            print()
            return False, f"Stok Tidak Cukup! Stok Tersedia: {barang['stock']}"
        barang["stock"] -= item["quantity"]
        print()
        msg = f"Stok {barang['name']} Dikurangi Sebanyak {item['quantity']}. Stok Sekarang: {barang['stock']}"

    save_data(data)  
    return True, msg

# customer.py
def update_keranjang(username, item_id, jumlah_baru, item_type):
    """
    Tambahkan atau perbarui jumlah item di keranjang.
    Jumlah_baru = jumlah akhir yang diinginkan (bukan selisih!)
    """
    if jumlah_baru <= 0:
        # Jika jumlah <= 0, anggap sebagai hapus
        return hapus_item_dari_keranjang_berdasarkan_id(username, item_id, item_type)

    data = load_data()
    user = next((u for u in data["users"] if u["username"] == username), None)
    if not user:
        return False, "❌ User tidak ditemukan!"

    # Cari barang di stok
    daftar = data["tickets"] if item_type == "ticket" else data["merchandise"]
    barang = next((x for x in daftar if x["id"] == item_id), None)
    if not barang:
        return False, "❌ Barang tidak ditemukan!"

    cart = user.get("cart", [])
    existing_item = None
    for item in cart:
        if item["item_id"] == item_id and item["type"] == item_type:
            existing_item = item
            break

    if existing_item:
        jumlah_lama = existing_item["quantity"]
        selisih = jumlah_baru - jumlah_lama

        if selisih > 0:
            # Tambah jumlah → kurangi stok
            if barang["stock"] < selisih:
                return False, f"❌ Stok tidak mencukupi! Tersedia: {barang['stock']}"
            barang["stock"] -= selisih
        elif selisih < 0:
            # Kurangi jumlah → tambah stok
            barang["stock"] += abs(selisih)

        existing_item["quantity"] = jumlah_baru
        pesan = f"✅ {barang['name']} diubah menjadi x{jumlah_baru}. Stok: {barang['stock']}"
    else:
        # Item baru → kurangi stok
        if barang["stock"] < jumlah_baru:
            return False, f"❌ Stok tidak mencukupi! Tersedia: {barang['stock']}"
        barang["stock"] -= jumlah_baru
        cart.append({
            "item_id": item_id,
            "name": barang["name"],
            "price": barang["price"],
            "quantity": jumlah_baru,
            "type": item_type
        })
        pesan = f"✅ {barang['name']} x{jumlah_baru} ditambahkan ke keranjang. Stok: {barang['stock']}"

    user["cart"] = cart
    save_data(data)
    return True, pesan

def hapus_item_dari_keranjang_berdasarkan_id(username, item_id, item_type):
    data = load_data()
    user = next((u for u in data["users"] if u["username"] == username), None)
    if not user:
        return False, "❌ User tidak ditemukan!"

    cart = user.get("cart", [])
    for i, item in enumerate(cart):
        if item["item_id"] == item_id and item["type"] == item_type:
            # Kembalikan stok
            daftar = data["tickets"] if item_type == "ticket" else data["merchandise"]
            for x in daftar:
                if x["id"] == item_id:
                    x["stock"] += item["quantity"]
                    break
            cart.pop(i)
            user["cart"] = cart
            save_data(data)
            return True, f"✅ {item['name']} dihapus dari keranjang. Stok dikembalikan."

    return False, "❌ Item tidak ditemukan di keranjang."

def ubah_jumlah_item(username):
    lihat_keranjang(username)
    try:
        nomor = int(input("Nomor item: "))
        jumlah_baru = int(input("Jumlah baru: "))
        
        # Ambil item dari keranjang
        data = load_data()
        user = next((u for u in data["users"] if u["username"] == username), None)
        if user and user["cart"]:
            item = user["cart"][nomor - 1]
            success, msg = update_keranjang(
                username,
                item["item_id"],
                jumlah_baru,
                item["type"]
            )
            print(msg)
    except (ValueError, IndexError):
        print("❌ Input tidak valid!")
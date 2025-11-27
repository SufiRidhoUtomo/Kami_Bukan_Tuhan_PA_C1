import json
import os

def load_data():
    """Memuat data dari file JSON atau membuat data default jika file tidak ada"""
    if not os.path.exists('data.json'):
        # Data default dengan tiket dan merchandise yang spesifik
        default_data = {
            "users": [
                {"id": 1, "username": "admin", "password": "admin123", "role": "admin", "balance": 150000000, "cart": []},
                {"id": 2, "username": "customer", "password": "customer123", "role": "customer", "balance": 500000, "cart": []}
            ],
            "tickets": [
                {"id": 1, "name": "General Admission", "price": 115000, "stock": 100, "type": "General Admission"},
                {"id": 2, "name": "Standard Grandstand", "price": 400000, "stock": 100, "type": "Standard Grandstand"},
                {"id": 3, "name": "Premium Grandstand", "price": 1000000, "stock": 100, "type": "Premium Grandstand"},
                {"id": 4, "name": "VIP Hospitality Suites Deluxe", "price": 10000000, "stock": 100, "type": "VIP Hospitality Suites Deluxe"},
                {"id": 5, "name": "VIP Hospitality Suites Premium", "price": 12000000, "stock": 100, "type": "VIP Hospitality Suite Premium"}
            ],
            "merchandise": [
                {"id": 1, "name": "Jersey Driver dan Team", "price": 300000, "stock": 100, "type": "Jersey"},
                {"id": 2, "name": "Topi (Caps)", "price": 150000, "stock": 100, "type": "Topi"},
                {"id": 3, "name": "Hoodie dan Jaket MotoGP", "price": 500000, "stock": 100, "type": "Hoodie"},
                {"id": 4, "name": "Key Chain", "price": 25000, "stock": 100, "type": "Aksesoris"},
                {"id": 5, "name": "Merchandise Eksklusif", "price": 2000000, "stock": 100, "type": "Eksklusif"}
            ],
            "transactions": []
        }
        save_data(default_data)
        return default_data
    
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Jika file JSON rusak, buat data default
        default_data = {
            "users": [
                {"id": 1, "username": "admin", "password": "admin123", "role": "admin", "balance": 150000000, "cart": []},
                {"id": 2, "username": "customer", "password": "customer123", "role": "customer", "balance": 500000, "cart": []}
            ],
            "tickets": [
                {"id": 1, "name": "General Admission", "price": 115000, "stock": 100, "type": "General Admission"},
                {"id": 2, "name": "Standard Grandstand", "price": 400000, "stock": 100, "type": "Standard Grandstand"},
                {"id": 3, "name": "Premium Grandstand", "price": 1000000, "stock": 100, "type": "Premium Grandstand"},
                {"id": 4, "name": "VIP Hospitality Suites Deluxe", "price": 10000000, "stock": 100, "type": "VIP Hospitality Suites Deluxe"},
                {"id": 5, "name": "VIP Hospitality Suites Premium", "price": 12000000, "stock": 100, "type": "VIP Hospitality Suite Premium"}
            ],
            "merchandise": [
                {"id": 1, "name": "Jersey Driver dan Team", "price": 300000, "stock": 100, "type": "Jersey"},
                {"id": 2, "name": "Topi (Caps)", "price": 150000, "stock": 100, "type": "Topi"},
                {"id": 3, "name": "Hoodie dan Jaket MotoGP", "price": 500000, "stock": 100, "type": "Hoodie"},
                {"id": 4, "name": "Key Chain", "price": 25000, "stock": 100, "type": "Aksesoris"},
                {"id": 5, "name": "Merchandise Eksklusif", "price": 2000000, "stock": 100, "type": "Eksklusif"}
            ],
            "transactions": []
        }
        save_data(default_data)
        return default_data

def save_data(data):
    """Menyimpan data ke file JSON"""
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

def get_next_id(collection_name):
    """Mendapatkan ID berikutnya untuk koleksi tertentu"""
    data = load_data()
    if collection_name in data and data[collection_name]:
        return max(item["id"] for item in data[collection_name]) + 1
    return 1

def add_user(username, password, role="customer"):
    """Menambahkan user baru"""
    data = load_data()
    new_id = get_next_id("users")
    new_user = {
        "id": new_id,
        "username": username,
        "password": password,
        "role": role,
        "balance": 0,
        "cart": []
    }
    data["users"].append(new_user)
    save_data(data)
    return new_user

def get_user_by_username(username):
    """Mendapatkan user berdasarkan username"""
    data = load_data()
    for user in data["users"]:
        if user["username"] == username:
            return user
    return None

def update_user(user):
    """Memperbarui data user"""
    data = load_data()
    for i, u in enumerate(data["users"]):
        if u["id"] == user["id"]:
            data["users"][i] = user
            break
    save_data(data)
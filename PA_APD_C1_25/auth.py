import json
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

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

def register(username, password):
    data = load_data()
    if username in data["users"]:
        return False, "===| Username Telah Digunakan, Silakan Coba Lagi! |==="
    
    data["users"][username] = {
        "password": password,
        "role": "customer",
        "cart": []
    }
    save_data(data)
    return True, "===| Berhasil Registrasi! |==="

def login(username, password):
    data = load_data()  
    if username in data["users"]:
        user = data["users"][username]
        if user["password"] == password:
            return True, f"===| Login Berhasil |===", user["role"] 
    return False, "===| Gagal Login! |===", None
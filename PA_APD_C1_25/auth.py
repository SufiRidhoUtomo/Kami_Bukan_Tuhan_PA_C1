# auth.py
import json
import os
os.system("cls")

Simpan_Data = "users.json"

def load_users():
    if not os.path.exists(Simpan_Data):
        with open(Simpan_Data, "w") as f:
            json.dump({"users": {}}, f)
    with open(Simpan_Data, "r") as f:
        return json.load(f)["users"]

def save_users(users_dict):
    with open(Simpan_Data, "w") as f:
        json.dump({"users": users_dict}, f)

def register(username, password):
    users = load_users()
    if username in users:
        print()
        return False, "===| Username Telah Digunakan, Silakan Coba Lagi! |==="
    users[username] = {"password": password, "role": "customer"}
    save_users(users)
    print()
    return True, "===| Berhasil Registrasi! |==="

def login(username, password):
    users = load_users()
    if username in users:
        user_data = users[username]
        if user_data["password"] == password:
            print()
            return True, f"===| Login Sebagai {user_data['role']} |===", user_data["role"]
        else:
            print()
            return False, "===| Username atau Password Salah, Silahkan Coba lagi! |===", None
    else:
        print()
        return False, "===| Username atau Password Salah, Silahkan Coba lagi! |===", None
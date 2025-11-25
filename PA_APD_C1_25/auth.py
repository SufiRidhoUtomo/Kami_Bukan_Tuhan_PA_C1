import json
import os

DB_FILE = "users.json"

def load_users():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({"users": {}}, f)
    with open(DB_FILE, "r") as f:
        return json.load(f)["users"]

def save_user(username, password, role="customer"):
    data = {"users": load_users()}
    data["users"][username] = {"password": password, "role": role}
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def register(username, password):
    users = load_users()
    if username in users:
        return False, "Username sudah terdaftar!"
    save_user(username, password, "customer")
    return True, "Registrasi berhasil sebagai customer!"

def login(username, password):
    users = load_users()
    if username in users:
        user_data = users[username]
        if user_data["password"] == password:
            return True, f"Login berhasil sebagai {user_data['role']}", user_data["role"]
    return False, "Username atau password salah!", None
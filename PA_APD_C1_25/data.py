import json
import os

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
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

def get_next_id(collection_name):
    data = load_data()
    if collection_name in data and data[collection_name]:
        return max(item["id"] for item in data[collection_name]) + 1
    return 1

def add_user(username, password, role="customer"):
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
    data = load_data()
    for user in data["users"]:
        if user["username"] == username:
            return user
    return None

def update_user(user):
    data = load_data()
    for i, u in enumerate(data["users"]):
        if u["id"] == user["id"]:
            data["users"][i] = user
            break
    save_data(data)
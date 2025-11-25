# Fungsi untuk menangani data admin (jika diperlukan di masa mendatang)
# Contoh: fungsi untuk menampilkan semua user, menghapus user, dll

from auth import load_users

def get_all_users():
    users = load_users()
    return users

def show_all_users():
    users = get_all_users()
    print("\nDaftar Pengguna:")
    for username, data in users.items():
        print(f"- {username} ({data['role']})")
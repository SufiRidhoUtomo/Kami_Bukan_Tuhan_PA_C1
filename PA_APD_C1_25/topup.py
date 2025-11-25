from data import update_user
from utils import clear_screen, print_header, input_integer, pause

def top_up(user):
    """Fungsi untuk top up balance"""
    clear_screen()
    print_header("TOP UP BALANCE")
    
    print(f"Saldo saat ini: Rp {user['balance']:,}")
    amount = input_integer(
        "Masukkan jumlah yang ingin ditambahkan: Rp ",
        min_val=10000,  # Minimal top up 10rb sesuai permintaan
        max_val=10000000
    )
    
    # Perbarui saldo user
    user["balance"] += amount
    update_user(user)
    
    print(f"\nTop up sebesar Rp {amount:,} berhasil!")
    print(f"Saldo terbaru: Rp {user['balance']:,}")
    pause()
    return user
from data import update_user
from utils import clear_screen, print_header, input_integer, pause

def top_up(user):
    clear_screen()
    print_header("TOP UP BALANCE")
    
    print(f"Saldo saat ini: Rp {user['balance']:,}")
    amount = input_integer(
        min_val=10000,  
        max_val=10000000
    )
    
    user["balance"] += amount
    update_user(user)
    
    print(f"\nTop up sebesar Rp {amount:,} berhasil!")
    print(f"Saldo terbaru: Rp {user['balance']:,}")
    pause()
    return user
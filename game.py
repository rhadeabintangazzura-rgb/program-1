secret_number = 999
jumlah_percobaan = 0

print("=" * 40)
print("Selamat datang di Game Tebak Angka!")
print("=" * 40)
print(f"Angka rahasia berada di antara 1-1000")
print()

try:
    while True:
        try:
            guess_number = int(input("Masukkan tebakan angka Anda: "))
            jumlah_percobaan += 1
            
            if guess_number == secret_number:
                print()
                print("=" * 40)
                print(f"🎉 Selamat! Angka yang benar adalah {secret_number}")
                print(f"Anda berhasil dalam {jumlah_percobaan} percobaan")
                print("=" * 40)
                break
            elif guess_number < secret_number:
                print(f"❌ Tebakan terlalu kecil! Coba angka yang lebih besar.")
            else:
                print(f"❌ Tebakan terlalu besar! Coba angka yang lebih kecil.")
            print()
        except ValueError:
            print("⚠️  Input salah! Masukkan angka yang valid.")
            print()
except KeyboardInterrupt:
    print("\nPermainan dibatalkan. Sampai jumpa!")
    exit()
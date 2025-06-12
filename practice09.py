def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"{amount} so'm muvaffaqiyatli qo'shildi.")
    else:
        print("Yaroqsiz miqdor.")
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("Hisobda yetarli mablag' mavjud emas.")
    elif amount <= 0:
        print("Yaroqsiz miqdor.")
    else:
        balance -= amount
        print(f"{amount} so'm yechildi.")
    return balance

def check_balance(balance):
    print(f"Hozirgi balans: {balance} so'm")

def main():
    balance = 0.0

    while True:
        print("\n=== ATM Menyusi ===")
        print("1 - Balansni ko'rish")
        print("2 - Pul qo'shish (deposit)")
        print("3 - Pul yechish (withdraw)")
        print("4 - Chiqish")

        tanlov = input("Amalni tanlang (1-4): ")

        if tanlov == "1":
            check_balance(balance)
        elif tanlov == "2":
            amount = float(input("Qo'shiladigan summani kiriting: "))
            balance = deposit(balance, amount)
        elif tanlov == "3":
            amount = float(input("Yechiladigan summani kiriting: "))
            balance = withdraw(balance, amount)
        elif tanlov == "4":
            print("Dasturdan chiqildi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov! Iltimos, qaytadan urinib ko'ring.")
main()

def is_strong_password(password: str):
    return len(password) >= 8

def main():
    parol = input("Parolni kiriting: ")

    if is_strong_password(parol):
        print("Kuchli parol ")
    else:
        print("Parol juda qisqa, kamida 8 ta belgi bo'lishi kerak")
main()
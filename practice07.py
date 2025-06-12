def main():
    def savol_ber(savol: str, togri_javob: str):
        print("Savol:", savol)
        javob = input("Javobingiz: ")
        if javobni_tekshir(javob, togri_javob):
            print("To'g'ri javob!")
        else:
            print(f"Noto'g'ri. To'g'ri javob: {togri_javob}")

    def javobni_tekshir(foydalanuvchi_javobi, togri_javob):
        return foydalanuvchi_javobi.strip().lower() == togri_javob.strip().lower()
    savol_ber("O'zbekiston poytaxti qaysi shahar? ", "Toshkent")
main()
def is_valid_phone_number( phone: str):
    """Telefon raqam 9 ta raqamdan iboratligini tekshiradi"""
    return phone.isdigit() and len(phone) == 9
def main():
    phone = input("Telefon raqamingizni kiriting (faqat 9 ta raqam): ")
    if is_valid_phone_number(phone):
        print("Telefon raqam to'g'ri.")
    else:
        print("Xato: Telefon raqam 9 ta raqamdan iborat bo'lishi kerak.")
main()

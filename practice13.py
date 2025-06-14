def is_palindrome(text: str) -> bool:
    return text == text[::-1]

text = input("So'z kiriting: ")
if is_palindrome(text):
    print("Teskarisi blan bir xil ")
else:
    print("Teskarisi blan bir xil emas")

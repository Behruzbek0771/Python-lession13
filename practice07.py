def main():
    def ask_question(question: str, correct_answer: str):
        print("question:", question)
        javob = input("Javobingiz: ")
        if ask_question(javob, correct_answer):
            print("To'g'ri javob!")
        else:
            print(f"Noto'g'ri. To'g'ri javob: {correct_answer}")

    def ask_question(user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.strip().lower()
    ask_question("O'zbekiston poytaxti qaysi shahar? ", "Toshkent")
main()
def calculate_age(birth_year, current_year):
    result = current_year-birth_year
    return result
def main():
    birth_year = int(input( " tug'ulgan kuninggiz:"))
    current_year = int(input( "Hozirga yil: "))
    if calculate_age(birth_year, current_year) > 18:
        print(" Siz balog'atga yetgansiz ")
        print(calculate_age(birth_year, current_year))
    else:
        print(" Siz balog'atga yetmagansiz ")
main()
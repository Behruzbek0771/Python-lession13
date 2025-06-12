def is_even(number):
    result = number %2 == 0
    return result
def main():
    number = int(input( "Number kriting: "))
    if is_even(number):
        print( f"{number}-juft son")
    else:
        print( f"{number}-toq son")
main()

def main():
    print("This program converts US dollars to Pounds Sterling\n")

    convert_to_pounds = lambda dollars: dollars * 0.79

    dollars = eval(input("Enter the amount in dollars: "))
    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "pounds.")

main()
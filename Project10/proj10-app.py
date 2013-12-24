from currency import Currency

def main():
    print("This Program starts an acount with 1000 USD and deduct expenses in variety of currencies")

    curr = Currency(1000, 'USD')

    while True:
        print("Current Account Balance : %s" % curr)
        code = input("Enter expenses to be deducted. Enter 'q' to quit : ")

        if code.lower() == 'q':
            print("Program is quitting. Thanks for using.")
            break

        if len(code) != 7:
            print("Enter input in  correct format!!!")
            continue

        amount = 0
        try:
            amount = float(code[0:3])
        except ValueError:
            print("Enter amount in int or float")
            continue

        if code[4:7] not in ("USD", "EUR", "SEK", "CAD", "CNY", "GBP"):
            print("Enter only valid currencies.")
            continue

        deduct_amount = Currency(amount, code[4:7])
        curr = curr - deduct_amount

if __name__ == "__main__":
    main()
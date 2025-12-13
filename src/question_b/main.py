from question_b import get_stock_list

def main():
    stocks = get_stock_list()

    while True:
        print("\n1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter option: ")

        if choice == "1":
            print("\nStock Report")
            print("Company\t\tSymbol")
            for stock in stocks:
                print(f"{stock.get_company_name()}\t{stock.get_symbol()}")
        elif choice == "2":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
#add import
import question_d

def stock_purchase_history():
    aapl = question_d.Stock('AAPL', 'Apple Inc')
    cat = question_d.Stock('CAT', 'Caterpillar')
    ek = question_d.Stock('EK', 'Eastman Kodak')
    goog = question_d.Stock('GOOG', 'Google')
    msft = question_d.Stock('MSFT', 'Microsoft')
    stock_dictionary = {aapl.return_symbol() : aapl.return_company_name(),
                        cat.return_symbol() : cat.return_company_name(),
                        ek.return_symbol() : ek.return_company_name(),
                        goog.return_symbol() : goog.return_company_name(),
                        msft.return_symbol() : msft.return_company_name()}
    for symbol, name in stock_dictionary.items():
        print (f"{symbol} | {name}")


def menu():
    print("""
1-Display stock purchase history
2-Exit
          """)
    selection = input('Type a selection and press Enter: ')
    if selection == "1":
        stock_purchase_history()
        menu()
    elif selection == "2":
        print('Exiting...')
    else:
        print('INPUT INVALID. Type a selection from the menu and press Enter:  ')
        menu()

def main():
    menu()
main()
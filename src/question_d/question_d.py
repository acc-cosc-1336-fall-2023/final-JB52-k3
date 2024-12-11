#write functions here, don't add input('') statements here!
class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def return_symbol(self):
        return self.__symbol
    
    def return_company_name(self):
        return self.__company_name
    
    def stock_purchase_history(self):
        aapl = Stock('AAPL', 'Apple Inc')
        cat = Stock('CAT', 'Caterpillar')
        ek = Stock('EK', 'Eastman Kodak')
        goog = Stock('GOOG', 'Google')
        msft = Stock('MSFT', 'Microsoft')
        stock_dictionary = {aapl.return_symbol : aapl.return_company_name,
                            cat.return_symbol : cat.return_company_name,
                            ek.return_symbol : ek.return_company_name,
                            goog.return_symbol : goog.return_company_name,
                            msft.return_symbol : msft.return_company_name,}
        for stock in stock_dictionary:
            print (stock)
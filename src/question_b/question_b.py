#write functions here, don't add input('') statements here!
class Stock:
    
    __symbol = ""
    __company_name = ""
    
    def __init__(self, symbol, company_name):

        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

    def get_stock_list():
        stock_list = []

        stock1 = Stock('AAPL', 'Apple Inc')
        stock_list.append(stock1)

        stock2 = Stock('CAT', 'Caterpillar')
        stock_list.append(stock2)

        stock3 = Stock('EK', 'Eastman Kodak')
        stock_list.append(stock3)

        stock4 = Stock('GOOG', 'Google')
        stock_list.append(stock4)

        stock5 = Stock('MSFT', 'Microsoft')
        stock_list.append(stock5)

        return stock_list
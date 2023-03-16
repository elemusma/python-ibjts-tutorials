from ibapi.client import *
from ibapi.wrapper import *
import time

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
    # def __init__(self, wrapper):
    #     super().__init__(wrapper)

    
    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        print(f'contract details: {contractDetails.longName}')
        print(f'contract details: {contractDetails.stockType}')
        print(f'contract details: {contractDetails.priceMagnifier}')
        # return super().contractDetails(reqId, contractDetails)

    
    def contractDetailsEnd(self, reqId: int):
        print('End of contract')
        # return super().contractDetailsEnd(reqId)
        self.disconnect()

    
def main():
    app = TestApp()

    app.connect('127.0.0.1', 7496, 1000)

    mycontract = Contract()
    mycontract.symbol = 'AAPL'
    mycontract.secType = 'STK'
    mycontract.exchange = 'SMART'
    mycontract.currency = 'USD'
    mycontract.primaryExchange = 'ISLAND'

    time.sleep(3)

    app.reqContractDetails(1, mycontract)

    app.run()


if __name__ == '__main__':
    main()
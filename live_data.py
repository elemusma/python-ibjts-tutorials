from ibapi.client import *
from ibapi.wrapper import *

class RequestMarketData(EClient, EWrapper):
    # def __init__(self, wrapper):
    #     super().__init__(wrapper)
    def __init__(self):
        EClient.__init__(self, self)


    def nextValidId(self, orderId: int):
        # return super().nextValidId(orderId)

        mycontract = Contract()
        mycontract.symbol = 'AAPL'
        mycontract.secType = 'STK'
        mycontract.exchange = 'SMART'
        mycontract.currency = 'USD'
        # mycontract.primaryExchange = 'ISLAND'

        self.reqMarketDataType(4)
        self.reqMktData(orderId, mycontract, "", 0, 0, [])


    def tickPrice(self, reqId, tickType, price, attrib):
        print(f'tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attribs: {attrib}')
        # return super().tickPrice(reqId, tickType, price, attrib)


    def tickSize(self, reqId, tickType, size):
        # return super().tickSize(reqId, tickType, size)
        print(f'tickSize. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, size: {size}')

    
app = RequestMarketData()
app.connect('127.0.0.1', 7497, 2000)
app.run()
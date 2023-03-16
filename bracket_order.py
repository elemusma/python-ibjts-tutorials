from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import ComboLeg
from ibapi.tag_value import TagValue

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)


    def nextValidId(self, orderId: int):
        #Order Info
        mycontract = Contract()
        mycontract.symbol = 'AAPL'
        mycontract.secType = 'STK'
        mycontract.exchange = 'SMART'
        mycontract.currency = 'USD'

        parent = Order()
        parent.orderId = orderId
        parent.orderType = 'LMT'
        parent.lmtPrice = 140
        parent.action = 'BUY'
        parent.totalQuantity = 5
        parent.transmit = False

        profit_taker = Order()
        profit_taker.orderId = parent.orderId + 1
        profit_taker.parentId = parent.orderId
        profit_taker.action = 'SELL'
        profit_taker.orderType = ''
        profit_taker.lmtPrice = 137
        profit_taker.transmit = False

        stop_loss = Order()
        stop_loss.orderId = parent.orderId + 2
        stop_loss.parentId = parent.orderId
        stop_loss.orderType = 'STP'
        stop_loss.action = 'SELL'
        stop_loss.totalQuantity = 5
        stop_loss.transmit = False

        self.placeOrder(parent.orderId, mycontract, parent)
        self.placeOrder(profit_taker.orderId, mycontract, profit_taker)
        self.placeOrder(stop_loss.orderId, mycontract, stop_loss)


    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        # return super().openOrder(orderId, contract, order, orderState)
        print(f'openOrder. orderId: {orderId}, contract: {contract}, order: {order}')


    def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
        # return super().orderStatus(orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice)
        print(f'orderStatus. orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillPrice: {avgFillPrice}, permId: {permId}, parentId: {parentId}, lastFillPrice: {lastFillPrice}, clientId: {clientId}, whyHeld: {whyHeld}, mktCapPrice: {mktCapPrice}')


    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        # return super().execDetails(reqId, contract, execution)
        print(f'execDetails. reqId: {reqId}, contract: {contract}, execution: {execution}')



app = TestApp()
app.connect('127.0.0.1', 7497, 1511)
app.run()
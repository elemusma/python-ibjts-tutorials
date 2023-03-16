from ibapi.client import *
from ibapi.wrapper import *

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)


    def error(self, reqId, errorCode, errorString):
        print(f'Error: {reqId} {errorCode} {errorString}')


    def nextValidId(self, orderId: int):
        # return super().nextValidId(orderId)
        self.start()


    def updatePortfolio(self, contract: Contract, position: Decimal, marketPrice: float, marketValue: float, averageCost: float, unrealizedPNL: float, realizedPNL: float, accountName: str):
        # return super().updatePortfolio(contract, position, marketPrice, marketValue, averageCost, unrealizedPNL, realizedPNL, accountName)
        print(f'UpdatePortfolio. Symbol: {contract.symbol}, SecType: {contract.secType}, Exchange: {contract.exchange}, Position: {position}, MarketPrice: {marketPrice}, MarketValue: {marketValue}, AverageCost: {averageCost}, UnrealizedPNL: {unrealizedPNL}, RealizedPNL: {realizedPNL}, AccountName: {accountName}')


    def updateAccountValue(self, key: str, val: str, currency: str, accountName: str):
        # return super().updateAccountValue(key, val, currency, accountName)
        print(f'UpdateAccountValue. Key: {key}, Value: {val}, Currency: {currency}, AccountName: {accountName}')


    def updateAccountTime(self, timeStamp: str):
        # return super().updateAccountTime(timeStamp)
        print(f'updateAccountTime. Time: {timeStamp}')


    def accountDownloadEnd(self, accountName: str):
        # return super().accountDownloadEnd(accountName)
        print(f'AccountDownloadEnd. Account {accountName}')


    def start(self):
        #Account number can be ommitted when using reqAccountUpdates with single account structure
        self.reqAccountUpdates(True, '')


    def stop(self):
        self.reqAccountUpdates(False, '')
        self.done = True
        self.disconnect()


app = TestApp()
app.connect('127.0.0.1', 7497, 1511)
app.run()
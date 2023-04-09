# import ibapi.wrapper as wrapper
# import ibapi.client as client
from ibapi.client import *
from ibapi.wrapper import *
import ibapi.contract as contract
import pandas as pd

class TestApp(EWrapper, EClient):
    def __init__(self):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)

        self.rsi_values = pd.Series()

        self.connect("127.0.0.1", 7497, clientId=0)

    def nextValidId(self, orderId:int):
        self.start()

    def start(self):
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"

        self.reqHistoricalData(1, contract, "", "1 D", "1 hour", "TRADES", 1, 1, False, [])

    def historicalData(self, reqId:int, bar):
        self.rsi_values = self.calculate_rsi(self.rsi_values, bar.close)
    
    def calculate_rsi(self, rsi_values, close_prices, n=14):
        deltas = close_prices.diff()
        seed = deltas[:n + 1]
        up = seed[seed >= 0].sum() / n
        down = -seed[seed < 0].sum() / n
        rs = up / down
        rsi = 100 - (100 / (1 + rs))
        rsi_values = rsi_values.append(pd.Series(rsi, index=[bar.date]))
        return rsi_values

    def stop(self):
        self.disconnect()

app = TestApp()
app.run()
print(app.rsi_values)

from datetime import datetime , timezone

class Trade:
    def __init__(self,trade_id,price,qty,buyer_id,seller_id,timestamp):
        self.trade_id = trade_id
        self.price = price
        self.qty = qty
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.timestamp = timestamp
    
    def __repr__(self):
        return f'[ Trade {self.trade_id} , time-> {self.timestamp} , traded_qty -> {self.qty} @ exec_price -> {self.price}]'
    
    def show_trade_info(self):
        print(f"Trade {self.trade_id} executed at ruppe {self.exec_price} of quantity {self.traded_qty} shares made by buyer {self.buyer_id} and seller {self.seller_id} at {self.timestamp}")     

''''''

trd_1 = Trade('1231',210,15,'1xyZ','trader_13',datetime.now(timezone.utc))

print(trd_1)

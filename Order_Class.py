from datetime import datetime, timezone

from zoneinfo import ZoneInfo

class Order:
    def __init__(self ,order_id ,agent_id ,order_type ,side ,qty,price=None,timestamp = None):  # thinking of making 
        
        self.order_id = order_id
        self.agent_id = agent_id
        self.price = price
        self.qty = qty
        self.type = order_type  # LIMIT / MARKET type
        self.side = side  # BUY / SELL
        self.timestamp = timestamp
        self.order_status = 'Pending'

    # self refers the particluar instance of class...! 

    def __repr__(self):
        return f"[ORDER ID {self.order_id} -> {self.side} {self.qty} @ {self.price}]"

    def show_order_info(self):
        print(self)     

''''''


odr = Order('O1','1XYZ','LIMIT','BUY',10,210)

# checking if it works 

odr.show_order_info()

# first task finished !

print(odr.timestamp)






# Ignore now
# Understand this , Later !!

'''
def __repr__(self):
    return f"[{self.order_type}] {self.side} {self.qty} @ {self.price} by Agent {self.agent_id} (Status: {self.order_status})

'''
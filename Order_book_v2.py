import time

from datetime import datetime, timezone

from Trade_Class import Trade

from collections import defaultdict

class OrderBook:
    def __init__(self):
        self.bids = defaultdict(list)     # This made our below task of appending any list having new key , easy !
        self.asks = defaultdict(list)     # As Mentioned Above , and Refered Below !
        self.trades = []                  # will store the Trade Objects , after each executed trade !

    def __repr__(self):
        return f'Bids -> {self.bids}  Asks -> {self.asks}'    


    def add_place_limit_order(self,L_Order):   # places limit order in orderbook !
        
        if L_Order.timestamp == None:   # when order have no timestamp then do make one. As in market order case where it become limit ,we will let it carry the old timestamp it had !
            L_Order.timestamp = datetime.now(timezone.utc)   # Time object is made which is aware of timezone 

        if L_Order.side == 'BUY':    # matches market order !
            self.bids[L_Order.price].append(L_Order)          #  eg. self.bids[210] == [Order]      # HERE (Ref.)
        
        elif L_Order.side == 'SELL':
            self.asks[L_Order.price].append(L_Order)          #  eg. self.asks[211] == [Order]

    ''' As you can see,one thing the new ordes are added in the last ,
    as we are using append method ,, and there is no problem with that,
    as we just do match the orders from start , so start order get the
    priority , becoz they were first , and it is time priority based .
    FIFO System '''


    def add_match_market_order(self,M_Order):

        if M_Order.type != 'MARKET': return 'Not Market Order'

        if M_Order.timestamp == None:
            M_Order.timestamp = datetime.now(timezone.utc)   # Time is measured 



      # Handles case when M_order IS SO BIG , IT EATS ALL ORDERs and there is stll qty left to fill , so it waits as limit buy
        
        if M_Order.side == "BUY" and len(self.asks) == 0:
            
            self.add_place_limit_order(M_Order)  # Places the Market Order into Orderbook ,(it becomes limit order for while) if there are No Orders left to match with ! 
            return f" Remaining quantity of ORDER ID {M_Order.order_id} will be filled when new orders appear !! " 
        


    # MATCHING LOGIC , MARKET BUY !
       
        if M_Order.side == 'BUY' and len(self.asks) != 0 :     # reject order , if no liquidity present in orderbook!
        # len checks if there is no key value pair in dictionary -> that it is empty 

            m1 = min(self.asks.keys())  # Finds key with MINIMUM Price Value

            n = len(self.asks[m1])
            
            for i in range(n):     #  becoz first orders are those which came first ,, in time. you can check append rule of list. 
                
                ord_list = self.asks[m1]      # Order list with minimum ask
                
                O1 = self.asks[m1][i]    # list having price m1 is accessed and its i'th order object 
                z = M_Order.qty - O1.qty
                
                
                if z == 0:  # incoming order qty matches sitting order qty !
                    
                    self.trades.append(Trade('trade_123',O1.price,O1.qty,M_Order.agent_id,O1.agent_id,datetime.now(timezone.utc)))
                    
                    self.asks[m1].pop(i)  # fully fill order is removed  # update orderbook
                    
                    if i == n:
                        del self.asks[m1]   # Removes or Delete the key value pair associated with key 'm1' that is ord_list
                    
                    return f'{self.trades[-1]} successful '   # A full complete trade Executed ,, with NO Complexity unlike Below ! 
                

                elif z < 0:  # incoming order qty is less then limit order
                    
                    self.trades.append(Trade('trade_230', O1.price, M_Order.qty, M_Order.agent_id, O1.agent_id, datetime.now(timezone.utc)))
                    
                    self.asks[m1][i].qty = abs(z)   # qty of real order got updated instead of duplicate O1 varable-> # update orderbook
                    
                    return self.trades[-1]  # the RECENT one will be the LAST one ! , previous - check this->  # return f'{Trade} success , after total {abs(i)} trades at ! '
                


                # last case is going to taste good 

                elif z > 0:  # incoming order qty is more then sitting order
                    
                    self.trades.append(Trade('trade_231', O1.price, O1.qty, M_Order.agent_id, O1.agent_id, datetime.now(timezone.utc)))
                    
                    self.asks[m1].pop(i)    # update orderbook
                    
                    M_Order.qty = z    # quantity of Order updated  (Market Order) 
                    
                    if i == n:
                        del self.asks[m1]    # list with price key 'm1' will be deleted 
                        
                        return self.add_match_market_order(M_Order)     # calling the same fucntion , recursively !


                            ###############################################################
        
        


    # Handles the case when order is so big that it sells so much , bids becomes vanished and it waits as limit sell , to fill full qty !
        
        if M_Order.side == "SELL" and len(self.bids) == 0:
            
            self.add_place_limit_order(M_Order)  
            return f" Remaining quantity of ORDER ID {M_Order.order_id} will be filled when new orders appear !! " 

        # MATCHING LOGIC , MARKET SELL !
        if M_Order.side == 'SELL' and len(self.bids) != 0 :

            m1 = max(self.bids.keys())
            n = len(self.bids[m1])
            
            for i in range(n):
                
                ord_list = self.bids[m1]      # Order list with maximum Bid
                O1 = ord_list[i]
                z = M_Order.qty - O1.qty
                
                
                if z == 0:
                    
                    self.trades.append(Trade('hj',O1.price,O1.qty,O1.agent_id,M_Order.agent_id,datetime.now(timezone.utc)))
                    
                    self.bids[m1].pop(i)   # update orderbook
                    
                    if i == n:
                        del self.bids[m1]   # Removes or Delete the key value pair associated with key 'm1' that is ord_list
                    return f'{self.trades[-1]} successful '   # A full complete trade Executed ,, with NO Complexity unlike Below ! 
                
                elif z < 0:
                    
                    self.trades.append(Trade('df',O1.price,M_Order.qty,O1.agent_id,M_Order.agent_id,datetime.now(timezone.utc)))
                    
                    self.bids[m1][i].qty = abs(z)            # update orderbook
                    return f'{self.trades[-1]} successful '
                
                elif z > 0:
                    
                    self.trades.append(Trade('ka',O1.price,O1.qty,M_Order.agent_id,O1.agent_id,datetime.now(timezone.utc)))
                    
                    ord_list.pop(i)    # update orderbook
                    
                    M_Order.qty = z    # quantity of Order updated  (Market Order)
                    
                    if i == n:
                        del self.bids[m1]    # list with key will be deleted 
                        
                        return self.add_match_market_order(M_Order)     # calling the same fucntion , recursively !
                    






''''''





import Order_Class

odr1 = Order_Class.Order('O12','1XYZ','LIMIT','BUY',10,210)

Odr_book = OrderBook()

Odr_book.add_place_limit_order(odr1)

print(Odr_book)

time.sleep(6)

ord2 = Order_Class.Order('O31','agent9','MARKET','SELL',9)

print(Odr_book.add_match_market_order(ord2))

time.sleep(5)

print(Odr_book)




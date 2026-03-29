# Binance Futures Testnet Trading Bot

Features
--------
*   Market & Limit Orders
*   BUY / SELL support
*   CLI interface
*   Input validation 
*   Logging
*   Error handling
    

Setup
-----
```bash
git clone cd trading_botpip install -r requirements.txt  
```

Create .env:
-----
```bash 
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret   
```

Usage
-----
### MARKET
```bash   
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.1   ```

### LIMIT
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.1 --price 70000  \
```

Sample Output
-------------
### Market order - BUY
```
===== ORDER SUMMARY =====
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.1
Price    : Market

===== ORDER RESPONSE =====
Order ID     : 13006325187
Status       : FILLED
Executed Qty : 0.100
Avg Price    : 66573.40000

===== STATUS =====
Order executed successfully
```

### Market Order - SELL
```
===== ORDER SUMMARY =====
Symbol   : BTCUSDT
Side     : SELL
Type     : MARKET
Quantity : 0.1
Price    : Market

===== ORDER RESPONSE =====
Order ID     : 13006338901
Status       : FILLED
Executed Qty : 0.100
Avg Price    : 66552.60000

===== STATUS =====
Order executed successfully
```

### Limit Order - BUY
```
===== ORDER SUMMARY =====
Symbol   : BTCUSDT
Side     : BUY
Type     : LIMIT
Quantity : 0.1
Price    : 60000.0

===== ORDER RESPONSE =====
Order ID     : 13006340561
Status       : NEW
Executed Qty : 0.000
Avg Price    : 0.00

===== STATUS =====
Order placed and waiting in order book
```
### Limit Order - SELL
``` 
===== ORDER SUMMARY =====
Symbol   : BTCUSDT
Side     : SELL
Type     : LIMIT
Quantity : 0.1
Price    : 70000.0

===== ORDER RESPONSE =====
Order ID     : 13006342009
Status       : NEW
Executed Qty : 0.000
Avg Price    : 0.00

===== STATUS =====
Order placed and waiting in order book
 ```

Logs
----
```
logs/trading.log
```

Assumptions
-----------
*   Binance Futures Testnet used 
*   Minimum notional ≈ 100 USDT
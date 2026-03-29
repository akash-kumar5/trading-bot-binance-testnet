**Binance Futures Testnet Trading Bot**

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
`git clone cd trading_botpip install -r requirements.txt   `

Create .env:

Plain 
`BINANCE_API_KEY=your_keyBINANCE_API_SECRET=your_secret   `

Usage
-----
### MARKET
`   python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.1   `

### LIMIT
`   python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.1 --price 70000   `

Sample Output
-------------
``` python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.1

Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.1
Price: None

Order Response:
Order ID: 13005895509
Status: FILLED
Executed Qty: 0.100
Avg Price: 66678.00000
```

Assumptions
-----------
*   Binance Futures Testnet used 
*   Minimum notional ≈ 100 USDT
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

### 1\. Clone the repository
```bash
   git clone https://github.com//trading-bot-binance-testnet.gitcd trading_bot   
   ```

### 2\. Create virtual environment (recommended)

```bash
   python -m venv .venv   
   ```

Activate it:

**Windows:**
```bash
   .venv\Scripts\activate   
   ```

**Mac/Linux:**
```bash
   source .venv/bin/activate   
   ```

### 3\. Install dependencies

```bash 
   pip install -r requirements.txt   
   ```

### 4\. Configure environment variables

Create a .env file in the root directory:
```bash  
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here   
```

### 5\. Important Notes

*   Uses **Binance Futures Testnet (USDT-M)**    
*   Ensure API keys are generated from Futures Testnet    
*   Minimum order value must be ≥ 100 USDT

Usage
-----
### MARKET
```bash   
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.1 

```

### LIMIT
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.1 --price 70000
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


made by Akash.
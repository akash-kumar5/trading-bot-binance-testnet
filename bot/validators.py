def validate_order(symbol, side, order_type, quantity, price):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if order_type.upper() == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")

    if order_type.upper() == "MARKET" and price is not None:
        raise ValueError("Price should not be provided for MARKET order")
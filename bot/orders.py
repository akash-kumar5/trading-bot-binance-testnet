from bot.client import BinanceClient
import time

client = BinanceClient()

def create_order(symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    # Step 1: place order
    response = client.place_order(**params)

    order_id = response.get("orderId")

    # Step 2: fetch updated order (important)
    time.sleep(1)  # small delay for execution

    updated_order = client.client.futures_get_order(
        symbol=symbol.upper(),
        orderId=order_id
    )

    return updated_order
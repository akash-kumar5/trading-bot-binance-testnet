import argparse
from bot.orders import create_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot CLI"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        # Validate input
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        logger.info(f"Placing order: {vars(args)}")

        # Place order
        response = create_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        logger.info(f"Response: {response}")

        # ===== ORDER SUMMARY =====
        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        print(f"Price    : {args.price if args.price else 'Market'}")

        # ===== ORDER RESPONSE =====
        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

        # ===== STATUS MESSAGE =====
        print("\n===== STATUS =====")
        status = response.get("status")

        if status == "FILLED":
            print("Order executed successfully")
        elif status == "NEW":
            print("Order placed and waiting in order book")
        else:
            print(f"Order status: {status}")

    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)

        print("\n===== ERROR =====")
        print(f"{str(e)}")

        # hint for mistakes
        if "Price required" in str(e):
            print("Hint: LIMIT orders require --price argument")
        elif "notional" in str(e):
            print("Hint: Increase quantity to meet minimum order value (~100 USDT)")


if __name__ == "__main__":
    main()
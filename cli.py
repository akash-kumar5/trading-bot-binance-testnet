import argparse
from bot.orders import create_order
from bot.validators import validate_order
from bot.logging_config import setup_logger
from bot.client import BinanceClient

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        logger.info(f"Placing order: {vars(args)}")

        response = create_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        logger.info(f"Response: {response}")

        print("\nOrder Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")

        print("\nOrder Response:")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        

        print("\n✅ Order placed successfully")
        if response.get("status") == "NEW":
            print(" Order is open and waiting to be filled")

    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
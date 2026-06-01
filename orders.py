from bot.client import get_client
from bot.logging_config import logger

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):

    try:

        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Sending order request: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"Order response: {response}")

        return response

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise
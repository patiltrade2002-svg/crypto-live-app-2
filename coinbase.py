import json
import websockets
from feeds.shared import PRICES
from feeds.config import COINS

PRODUCT_MAP = {v["coinbase"]: k for k, v in COINS.items()}

async def run_coinbase():
    uri = "wss://ws-feed.exchange.coinbase.com"

    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps({
            "type": "subscribe",
            "channels": [{
                "name": "ticker",
                "product_ids": list(PRODUCT_MAP.keys())
            }]
        }))

        while True:
            msg = json.loads(await ws.recv())

            if msg.get("type") == "ticker":
                coin = PRODUCT_MAP.get(msg["product_id"])
                if coin:
                    PRICES[coin]["Coinbase"] = float(msg["price"])
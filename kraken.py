import json
import websockets
from feeds.shared import PRICES
from feeds.config import COINS

PAIR_MAP = {v["kraken"]: k for k, v in COINS.items()}

async def run_kraken():
    uri = "wss://ws.kraken.com"

    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps({
            "event": "subscribe",
            "pair": list(PAIR_MAP.keys()),
            "subscription": {"name": "ticker"}
        }))

        while True:
            msg = json.loads(await ws.recv())

            if isinstance(msg, list):
                pair = msg[-1]
                coin = PAIR_MAP.get(pair)

                if coin:
                    price = float(msg[1]["c"][0])
                    PRICES[coin]["Kraken"] = price
# Coin configuration (20 coins)

COINS = {
    # High volume / low spread
    "BTC":  {"coinbase": "BTC-USD",  "kraken": "XBT/USD"},
    "ETH":  {"coinbase": "ETH-USD",  "kraken": "ETH/USD"},
    "SOL":  {"coinbase": "SOL-USD",  "kraken": "SOL/USD"},
    "BNB":  {"coinbase": "BNB-USD",  "kraken": "BNB/USD"},
    "XRP":  {"coinbase": "XRP-USD",  "kraken": "XRP/USD"},

    # High volume / high spread
    "ADA":   {"coinbase": "ADA-USD",   "kraken": "ADA/USD"},
    "AVAX":  {"coinbase": "AVAX-USD",  "kraken": "AVAX/USD"},
    "DOGE":  {"coinbase": "DOGE-USD",  "kraken": "DOGE/USD"},
    "LINK":  {"coinbase": "LINK-USD",  "kraken": "LINK/USD"},
    "MATIC": {"coinbase": "MATIC-USD", "kraken": "MATIC/USD"},

    # Low volume / high spread
    "SUSHI": {"coinbase": "SUSHI-USD", "kraken": "SUSHI/USD"},
    "1INCH": {"coinbase": "1INCH-USD", "kraken": "1INCH/USD"},
    "COMP":  {"coinbase": "COMP-USD",  "kraken": "COMP/USD"},
    "ENJ":   {"coinbase": "ENJ-USD",   "kraken": "ENJ/USD"},
    "YFI":   {"coinbase": "YFI-USD",   "kraken": "YFI/USD"},

    # Low volume / low spread
    "ZEC":   {"coinbase": "ZEC-USD",   "kraken": "ZEC/USD"},
    "DASH":  {"coinbase": "DASH-USD",  "kraken": "DASH/USD"},
    "KSM":   {"coinbase": "KSM-USD",   "kraken": "KSM/USD"},
    "OMG":   {"coinbase": "OMG-USD",   "kraken": "OMG/USD"},
    "BAND":  {"coinbase": "BAND-USD",  "kraken": "BAND/USD"},
}

# Trading fees (round-trip)
FEES = {
    "Coinbase": 0.006,   # 0.6%
    "Kraken":   0.004    # 0.4%
}
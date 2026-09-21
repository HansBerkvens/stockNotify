from dataclasses import dataclass

@dataclass
class Stock:
    ticker: str
    alias: str = ''
    price_min: float | None = None
    price_max: float | None = None

STOCKS = [
    Stock('AGNC', '', 9.8, None),
    Stock('AVGO', '', 300, None),
    Stock('CRDO', '', 150, None),
    Stock('EME', '', 600, 950),
    Stock('MSFT', '', 350, None),
    Stock('QYLE.DE', '', 14.4, None),
    Stock('SKHY', '', 175, None),
    Stock('PUIG.MC', '', 15, None),
    Stock('SY7D.DE', '', 14.3, None),
    Stock('GOOG', '', 300, None),
    Stock('AMZN', '', 220, None),
    Stock('ASML.AS', '', 1325, None),
    Stock('EUNL.DE', '', 120, None),
    Stock('CSPX.DE', '', 680, None),
    Stock('EXSA.DE', '', 60, None),
]

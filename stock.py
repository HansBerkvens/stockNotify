from dataclasses import dataclass

@dataclass
class Stock:
    ticker: str
    alias: str = ''
    price_min: float | None = None
    price_max: float | None = None
    explanation: str = ''

STOCKS = [
    Stock('AGNC', 'AGNC', 8.5, 9, 'price jumpy between $9.00 and $10.50 in 3 year window.\nRevenue & Profit on a steady climb. PE ratio of 5 is very low.\n14% div - monthly\nhttps://divvydiary.com/en/agnc-investment-stock-US00123Q1040'),
    Stock('AVGO', 'Broadcom', 300, None),
    Stock('CRDO', 'Credo', 150, None),
    Stock('EME', 'Emcor', 600, 950, 'Share price growing nice and steadily. Revenue growing nice and steadily, profit margin is on the low side. ROIC of 36% is amazing. Operating CF outpacing CapEx.'),
    Stock('MSFT', 'Microsoft', 450, None),
    Stock('QYLE.DE', 'Global x Nasdaq', 14.4, None, 'Global X 12% div - monthly payout.\nhttps://divvydiary.com/en/global-x-nasdaq-100-covered-call-ucits-dis-etf-IE00BM8R0J59'),
    Stock('SKHY', '', 175, None, 'Revenue growing from 30 (2023) to 66 to 97 to (ttm) 189 trillion, explosive growth. Revenue growing with it with profit margins 30% (2024), 45%, 85% (ttm). PE ratio of 9.05 is low. Located in Asia for non-western coverage.'),
    Stock('PUIG.MC', 'PUIG Brands', 16, None),
    Stock('META', 'Meta', 580, 740),
    Stock('SY7D.DE', '', 14.4, None, 'Preferably trade on Xetra, not on tradegate. Global X 12% Europe - monthly payout\nhttps://divvydiary.com/en/global-x-euro-stoxx-50-covered-call-ucits-dis-etf-IE000SAXJ1M1'),
    Stock('GOOG', 'Google', 310, None, 'Google will always bounce back from a dip.'),
    Stock('AMZN', 'Amazon', 220, None),
    Stock('ASML.AS', 'ASML', 1400, None),
    Stock('EUNL.DE', 'World ETF', 123, None),
    Stock('CSPX.AS', 'S&P500 ETF', 680, None),
    Stock('EXSA.DE', 'Europe 600 ETF', 60, None),
    Stock('YETI', 'Yeti Holdings', 36, None, 'Good numbers, price is a bit volatile bouncing 35-45 with spikes to 25 and 55. Consider near 35.')
]

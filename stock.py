from dataclasses import dataclass

@dataclass
class Stock:
    ticker: str
    alias: str = ''
    price_min: float | None = None
    price_max: float | None = None
    explanation: str = ''

STOCKS = [

    ################################################################################ De Giro
    Stock('ABN.AS', 'ABN Amro', 38.0, 45),
    Stock('MFG', 'Mizuho', 8, 11),
    Stock('AGNC', 'AGNC', 8.1, 9, 'price jumpy between $9.00 and $10.50 in 3 year window.\nRevenue & Profit on a steady climb. PE ratio of 5 is very low.\n14% div - monthly\nhttps://divvydiary.com/en/agnc-investment-stock-US00123Q1040'),
    Stock('ARCC', 'Ares Capital', 18, 20, '12 Nov 26, i am inclined to jump on the doubt train, calling it bouncing 18-20'),
    Stock('ASRNL.AS', 'ASR', 70, 85, ''),
    Stock('SAN.MC', 'Banco Santander', 9, 14, ''),
    Stock('AVGO', 'Broadcom', 300, 480),
    Stock('CRDO', 'Credo', 100, 200),
    Stock('CVC.AS', 'CVC Capital Partners', 12.5, 17.5, ''),
    Stock('DX', 'Dynex Capital', 9, 12, '[2026-11-12] DX not doing well, Sep 2026 number are terrible, but I dont feel like selling at the all time low of $10.06.'),
    Stock('EME', 'Emcor', 600, 950, 'Share price growing nice and steadily. Revenue growing nice and steadily, profit margin is on the low side. ROIC of 36% is amazing. Operating CF outpacing CapEx.'),
    Stock('EXLS', 'ExlService Holdings', 35, 50, ''),
    Stock('EXPN.L', 'Experian PLC', 2500, 3500, ''),
    Stock('HTGC', 'Hercules Capital', 14, 19, ''),
    Stock('INGA.AS', 'ING', 27, 35, ''),
    Stock('MEGP.L', 'ME Group International', 90, 140, ''),
    Stock('MSFT', 'Microsoft', 450, None),
    Stock('NRDS', 'Nerdwallet', 6.5, 15, ''),
    Stock('NEWT', 'NewtekOne, Inc.', 10.3, 14, 'Price incredibly jumpy between $10 and $15 on 3 year window'),
    Stock('NN.AS', 'NN Group', 70, 90, ''),
    Stock('OSB.L', 'OSB Group', 425, 600, ''),
    Stock('PGY', 'Pagaya', 10, 30, ''),
    Stock('PRX.AS', 'Prosus', 30, 45, ''),
    Stock('O', 'Realty Income Corp', 56, None, 'Price seems jumpy between 56 and 60+, buy below 56'),
    Stock('SOUN', 'SoundHound AI', None, 5, ''),
    Stock('SGHC', 'Super Group (SGHC)', 7.5, 16, ''),
    Stock('VLK.AS', 'Van Lanschot Kempen', 52, 80, ''),

    ################################################################################ De Giro
    Stock('SY7D.DE', 'Global X Europe 50', 14.4, 15.0, '12% div - monthly payout.\nhttps://divvydiary.com/en/global-x-euro-stoxx-50-covered-call-ucits-dis-etf-IE000SAXJ1M1'),
    Stock('QYLE.DE', 'Global X Nasdaq 100', 14.4, 15.0, '12% div - monthly payout.\nhttps://divvydiary.com/en/global-x-nasdaq-100-covered-call-ucits-dis-etf-IE00BM8R0J59'),
    Stock('XY7D.DE', 'Global X S&P 500', 13.2, 14.1, '10% div - monthly payout.\nhttps://divvydiary.com/en/global-x-s-and-p-500-covered-call-ucits-etf-IE0002L5QB31'),

    ################################################################################ Scalable
    Stock('GOOG', 'Google', 270, None, 'Google will always bounce back from a dip.'),
    Stock('AMZN', 'Amazon', 225, 320, ''),
    Stock('AAPL', 'Apple', 300, 400, ''),
    Stock('ASML.AS', 'ASML', 1400, None),
    Stock('KO', 'Coca-Cola', 80, 110, ''),
    Stock('DLR', 'Digital Realty Trust', 175, 200, ''),
    Stock('IAEA.AS', 'AEX ETF', 10.65, None, ''),
    Stock('IB1T.DE', 'Bitcoin ETF', 5.75, 7.5, ''),
    Stock('EUNL.DE', 'World ETF', 125, None),
    Stock('CSPX.AS', 'S&P500 ETF', 710, None),
    Stock('EXSA.DE', 'Europe 600 ETF', 60, None),
    Stock('MCD', 'BBBB', 255, 300, ''),
    Stock('META', 'Meta', 580, 730),
    Stock('NVDA', 'Nvidia', 125, 250, ''),
    Stock('G24.DE', 'Scout24', 80, 105, ''),
    Stock('SKHY', 'SK Hynix', 130, 180, 'Revenue growing from 30 (2023) to 66 to 97 to (ttm) 189 trillion, explosive growth. Revenue growing with it with profit margins 30% (2024), 45%, 85% (ttm). PE ratio of 9.05 is low. Located in Asia for non-western coverage.'),
    Stock('SLR.MC', 'Solaria Energia', 10, 22, ''),
    Stock('TTWO', 'Take-Two Interactive Software', 207, 245, ''),
    Stock('0700.HK', 'Tencent Holdings', 350, 600, ''),
    Stock('VRT', 'Vertiv', 175, 320, ''),
    Stock('XNAS.DE', 'Nasdaq ETF', 53.5, 75, ''),

    ################################################################################ Prospects
    Stock('PUIG.MC', 'PUIG Brands', 16, None),
    Stock('YETI', 'Yeti Holdings', 36, None, 'Good numbers, price is a bit volatile bouncing 35-45 with spikes to 25 and 55. Consider near 35.')
]


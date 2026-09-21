import yfinance as yf
import pandas as pd
from stock import STOCKS, Stock
from mail import send_notification
import logging
import sys
logging.basicConfig(level=logging.INFO, format="%(name)s:%(levelname)s:%(asctime)s\t\t%(message)s", datefmt="%H:%M:%S", force=True, stream=sys.stdout)

logging.info('At least the logger works')


send_notification('Stock Notify', 'Starting run')
sentences = []
for s in STOCKS:
    try:
        price = yf.Ticker(s.ticker).history(period=f'1d', auto_adjust=False)['Close'].item()
        if s.price_min is not None and price <= s.price_min:
            sentences.append(f'Ticker {s.ticker} ({s.alias}) fell below {s.price_min}.')
        elif s.price_max is not None and s.price_max <= price:
            sentences.append(f'Ticker {s.ticker} ({s.alias}) rose above {s.price_min}.')
        else:
            sentences.append(f'Ticker {s.ticker} is at {price:.2f} which is between {s.price_min} and {s.price_max}')
    except Exception:
        pass

if sentences:
    logging.info(f'Trying to send {len(sentences)} sentences.')
    body = '\n'.join(sentences)
    print(body)
    # send_notification('Stock Notify Action', body)


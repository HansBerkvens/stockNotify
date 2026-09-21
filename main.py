import yfinance as yf
import pandas as pd
from stock import STOCKS, Stock
from mail import send_notification
import logging
import sys
logging.basicConfig(level=logging.INFO, format="%(name)s:%(levelname)s:%(asctime)s\t\t%(message)s", datefmt="%H:%M:%S", force=True, stream=sys.stdout)

print('At least the logger works', flush=True)


send_notification('Stock Notify', 'Starting run')
sentences = []
for s in STOCKS:
    try:
        price = yf.Ticker(s.ticker).history(period=f'1d', auto_adjust=False)['Close'].item()
        print(f'{s.ticker} = {price:.2f}', flush=True)
        if s.price_min is not None and price <= s.price_min:
            sentences.append(f'Ticker {s.ticker} ({s.alias}) fell below {s.price_min}.')
        elif s.price_max is not None and s.price_max <= price:
            sentences.append(f'Ticker {s.ticker} ({s.alias}) rose above {s.price_min}.')
        else:
            sentences.append(f'Ticker {s.ticker} is at {price:.2f} which is between {s.price_min} and {s.price_max}')
    except Exception as e:
        print(str(e).split('\n'), flush=True)
        pass

if sentences:
    print(f'Trying to send {len(sentences)} sentences.', flush=True)
    body = '\n'.join(sentences)
    print(body, flush=True)
    # send_notification('Stock Notify Action', body)


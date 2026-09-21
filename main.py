import yfinance as yf
from stock import STOCKS, Stock
from mail import send_notification
import logging

logging.basicConfig(level=logging.INFO, format="%(name)s:%(levelname)s:%(asctime)s\t\t%(message)s", datefmt="%H:%M:%S", force=True)


send_notification('Stock Notify', 'Starting run')
sentences = []
for s in STOCKS:
    try:
        price = yf.Ticker(s.ticker).history(period=f'1d', auto_adjust=False)['Close'].item()
        logging.info(f'{s.ticker} = {price:.2f}')
        if s.price_min is not None and price <= s.price_min:
            sentences.append(f'Ticker {s.ticker} ({s.alias}) fell below {s.price_min}.')
        elif s.price_max is not None and s.price_max <= price:
            sentences.append(f'Ticker {s.ticker} ({s.alias}) rose above {s.price_min}.')
        else:
            sentences.append(f'Ticker {s.ticker} is at {price:.2f} which is between {s.price_min} and {s.price_max}')
    except Exception as e:
        logging.info(str(e).split('\n'))
        pass

if sentences:
    body = '\n'.join(sentences)
    send_notification('Stock Notify Action', body)


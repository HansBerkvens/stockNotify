import yfinance as yf
from stock import STOCKS, Stock
from mail import send_notification
import logging

logging.basicConfig(level=logging.INFO, format="%(name)s:%(levelname)s:%(asctime)s\t\t%(message)s", datefmt="%H:%M:%S", force=True)

stocks = [s for s in STOCKS if '.DE' in s.ticker]
sentences = []
for s in STOCKS:
    try:
        price = yf.Ticker(s.ticker).history(period=f'1d', auto_adjust=False)['Close'].item()
        logging.info(f'{s.ticker} = {price:.2f}')

        if s.price_min is not None and price <= s.price_min:
            violation = f'fell below {s.price_min}, might be a good buy.'
        elif s.price_max is not None and s.price_max <= price:
            violation = f'rose above {s.price_max}, might be time to sell.'
        else:
            continue

        name = s.alias if s.alias else s.ticker

        explanation = s.explanation if s.explanation else ''

        sentence = f'Instrument {name} {violation}\n{explanation}\n\n'

        sentences.append(sentence)
    except Exception as e:
        logging.info(str(e).split('\n'))
        pass

if sentences:
    body = '\n'.join(sentences)
    send_notification(f'Stock Notify Action ({len(sentences)}', body)


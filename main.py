import yfinance as yf
import pandas as pd
from stock import STOCKS, Stock
from mail import send_notification


if __name__ == '__main__':

    sentences = []
    for s in STOCKS:
        try:
            price = yf.Ticker(s.ticker).history(period=f'1d', auto_adjust=False)['Close'].item()
            if s.price_min is not None and price <= s.price_min:
                sentences.append(f'Ticker {s.ticker} ({s.alias}) fell below {s.price_min}.')
            elif s.price_max is not None and s.price_max <= price:
                sentences.append(f'Ticker {s.ticker} ({s.alias}) rose above {s.price_min}.')
            else:
                sentences.append(f'Ticker {s.ticker} is still between {s.price_min} and {s.price_max}')
        except Exception:
            pass

    if sentences:
        body = '\n'.join(sentences)
        send_notification('Stock Notify Action', body)


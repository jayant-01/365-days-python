import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

stock = ['AAPL','MSFT','GOOG','AMZN']

print(yf.download(stock, period='imo'))



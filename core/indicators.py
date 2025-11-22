import ta
import pandas as pd

def rsi_strategy(df):
    rsi = ta.momentum.RSIIndicator(df['close']).rsi()
    return rsi.iloc[-1]

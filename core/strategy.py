from core.indicators import rsi_strategy

def get_signal(df):
    rsi = rsi_strategy(df)

    if rsi < 30:
        return "up"     # oversold → BUY
    elif rsi > 70:
        return "down"   # overbought → SELL
    else:
        return None

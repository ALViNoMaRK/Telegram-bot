import time
from config import *
from core.pocket_api import PocketAPI
from core.strategy import get_signal
from telegram.notifier import notify
import yfinance as yf

po = PocketAPI(PO_EMAIL, PO_PASSWORD)

print("Logging in...")
if not po.login():
    print("Login failed")
    notify("❌ Pocket Option login FAILED")
    exit()

notify("✅ Bot started successfully!")

while True:
    # get price candles
    df = yf.download(CURRENCY.replace("/", ""), period="1d", interval="1m")

    signal = get_signal(df)

    if signal:
        result = po.trade(CURRENCY, TRADE_AMOUNT, signal, TRADE_DURATION)
        notify(f"📊 Signal: {signal}\nResult: {result}")

    time.sleep(60)

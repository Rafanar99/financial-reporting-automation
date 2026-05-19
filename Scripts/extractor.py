"""
extractor.py — Extração de dados históricos via yfinance
"""

import time
import yfinance as yf
import pandas as pd
from curl_cffi.requests import Session


TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM"]


def _make_session() -> Session:
    return Session(verify=False)


def _download_single(ticker: str, session: Session, max_retries: int = 3) -> pd.Series | None:
    """Baixa um ticker usando period='1y' com retry e backoff progressivo."""
    for attempt in range(1, max_retries + 1):
        try:
            tk = yf.Ticker(ticker, session=session)
            df = tk.history(period="1y", auto_adjust=True)

            if not df.empty:
                return df["Close"]
            else:
                print(f"  ⚠ sem dados (tentativa {attempt}/{max_retries})")
        except Exception as e:
            print(f"  ✗ erro: {e} (tentativa {attempt}/{max_retries})")

        if attempt < max_retries:
            wait = attempt * 10  # 10s, 20s, 30s
            print(f"  ⏳ aguardando {wait}s...")
            time.sleep(wait)

    return None


def get_closing_prices(
    tickers: list[str] = TICKERS,
) -> pd.DataFrame:

    print(f"[Extractor] Baixando último ano de dados...")
    print(f"[Extractor] Tickers: {', '.join(tickers)}")

    session = _make_session()
    all_prices = {}

    for i, ticker in enumerate(tickers):
        print(f"[Extractor] [{i+1}/{len(tickers)}] {ticker}...", end=" ")

        series = _download_single(ticker, session)

        if series is not None:
            all_prices[ticker] = series
            print("✓")
        else:
            print("✗ falhou")

        if i < len(tickers) - 1:
            time.sleep(5)  # 5s entre cada ticker

    prices = pd.DataFrame(all_prices)
    prices.dropna(how="all", inplace=True)

    print(f"\n[Extractor] {len(prices)} pregões — {len(all_prices)}/{len(tickers)} tickers. ✓")
    return prices


if __name__ == "__main__":
    df = get_closing_prices()
    print(df.tail())

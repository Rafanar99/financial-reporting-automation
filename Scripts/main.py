"""
main.py — Orquestrador principal do Financial Report Automation
Executa o pipeline completo: extração → processamento → relatório.

Uso:
    python main.py
"""

import sys
import time

from extractor import get_closing_prices, TICKERS
from processor import process_all
from report_generator import generate_report

OUTPUT_DIR = "output"
ASSETS_DIR = "assets"


def main() -> None:
    start = time.time()

    print("=" * 60)
    print("  Financial Report Automation")
    print("=" * 60)

    # ── Etapa 1: Extração ──────────────────────────────────────
    print("\n📥  ETAPA 1 — Extração de dados (yfinance)")
    print("-" * 60)
    try:
        prices = get_closing_prices(tickers=TICKERS)
    except Exception as e:
        print(f"[ERRO] Falha na extração: {e}")
        sys.exit(1)

    # ── Etapa 2: Processamento ────────────────────────────────
    print("\n⚙️   ETAPA 2 — Processamento (pandas)")
    print("-" * 60)
    try:
        data = process_all(prices)
    except Exception as e:
        print(f"[ERRO] Falha no processamento: {e}")
        sys.exit(1)

    # ── Etapa 3: Relatório ────────────────────────────────────
    print("\n📊  ETAPA 3 — Geração do relatório (openpyxl + matplotlib)")
    print("-" * 60)
    try:
        generate_report(data, output_dir=OUTPUT_DIR, assets_dir=ASSETS_DIR)
    except Exception as e:
        print(f"[ERRO] Falha na geração do relatório: {e}")
        sys.exit(1)

    elapsed = time.time() - start
    print(f"\n✅  Pipeline concluído em {elapsed:.1f}s")
    print("=" * 60)


if __name__ == "__main__":
    main()

"""
processor.py — Cálculos e métricas com Pandas
"""

import pandas as pd
import numpy as np


TRADING_DAYS_YEAR = 252  # dias úteis usados para anualizar volatilidade


# ──────────────────────────────────────────────
# Cálculos principais
# ──────────────────────────────────────────────

def calc_daily_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Retorno percentual diário de cada ativo."""
    return prices.pct_change().dropna()


def calc_cumulative_returns(daily_returns: pd.DataFrame) -> pd.DataFrame:
    """
    Retorno acumulado diário de cada ativo (base 0 no primeiro dia).
    Fórmula: (1 + r1) * (1 + r2) * ... - 1
    """
    return (1 + daily_returns).cumprod() - 1


def calc_kpis(prices: pd.DataFrame, daily_returns: pd.DataFrame) -> pd.DataFrame:
    """
    Gera a tabela de KPIs — uma linha por ativo.

    Colunas produzidas:
        Ticker, Preço Inicial, Preço Final,
        Retorno Acumulado (%), Volatilidade (% a.a.),
        Melhor Dia (%), Pior Dia (%), Ranking
    """
    kpis = pd.DataFrame(index=prices.columns)

    kpis["Ticker"]              = prices.columns
    kpis["Preço Inicial"]       = prices.iloc[0]
    kpis["Preço Final"]         = prices.iloc[-1]
    kpis["Retorno Acumulado %"] = ((prices.iloc[-1] / prices.iloc[0]) - 1) * 100
    kpis["Volatilidade % a.a."] = (
        daily_returns.std() * np.sqrt(TRADING_DAYS_YEAR) * 100
    )
    kpis["Melhor Dia %"]        = daily_returns.max() * 100
    kpis["Pior Dia %"]          = daily_returns.min() * 100

    # Ranking: 1 = maior retorno acumulado
    kpis["Ranking"] = kpis["Retorno Acumulado %"].rank(ascending=False).astype(int)
    kpis = kpis.sort_values("Ranking").reset_index(drop=True)

    return kpis


def calc_correlation(daily_returns: pd.DataFrame) -> pd.DataFrame:
    """Matriz de correlação de Pearson entre os retornos diários."""
    return daily_returns.corr()


# ──────────────────────────────────────────────
# Função de orquestração
# ──────────────────────────────────────────────

def process_all(prices: pd.DataFrame) -> dict:
    """
    Recebe o DataFrame de preços e retorna um dicionário com todos
    os artefatos calculados:

        {
            "prices":       DataFrame — preços de fechamento brutos
            "daily":        DataFrame — retornos diários
            "cumulative":   DataFrame — retornos acumulados
            "kpis":         DataFrame — tabela de KPIs por ativo
            "correlation":  DataFrame — matriz de correlação
        }
    """
    print("[Processor] Calculando retornos diários...")
    daily = calc_daily_returns(prices)

    print("[Processor] Calculando retornos acumulados...")
    cumulative = calc_cumulative_returns(daily)

    print("[Processor] Calculando KPIs...")
    kpis = calc_kpis(prices, daily)

    print("[Processor] Calculando matriz de correlação...")
    correlation = calc_correlation(daily)

    print("[Processor] Processamento concluído. ✓")
    return {
        "prices":      prices,
        "daily":       daily,
        "cumulative":  cumulative,
        "kpis":        kpis,
        "correlation": correlation,
    }


if __name__ == "__main__":
    from extractor import get_closing_prices
    prices = get_closing_prices()
    data = process_all(prices)
    print(data["kpis"].to_string())

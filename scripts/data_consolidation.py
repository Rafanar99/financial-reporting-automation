"""
Multi-Entity Financial Data Consolidation
Consolidates financial data from multiple entities/countries with currency conversion
"""

import pandas as pd
from datetime import datetime

class FinancialConsolidator:
    def __init__(self, fx_rates=None):
        self.fx_rates = fx_rates or {}
        
    def consolidate_entities(self, data_files):
        consolidated = []
        for file in data_files:
            df = pd.read_excel(file) if file.endswith('.xlsx') else pd.read_csv(file)
            df['Entity'] = file.split('/')[-1].split('.')[0]
            if 'Currency' in df.columns and 'Amount' in df.columns:
                df['Amount_USD'] = df.apply(
                    lambda row: row['Amount'] * self.fx_rates.get(row['Currency'], 1), axis=1
                )
            consolidated.append(df)
        return pd.concat(consolidated, ignore_index=True)
    
    def calculate_variances(self, df, actual_col='Actual', budget_col='Budget'):
        df['Variance_Abs'] = df[actual_col] - df[budget_col]
        df['Variance_Pct'] = ((df[actual_col] - df[budget_col]) / df[budget_col] * 100).round(2)
        return df

if __name__ == "__main__":
    fx_rates = {
        'BRL': 0.20, 'ARS': 0.004, 'COP': 0.00025,
        'PEN': 0.27, 'CLP': 0.0011, 'UYU': 0.026
    }
    consolidator = FinancialConsolidator(fx_rates)
    print("Financial Consolidator initialized")
    print(f"Supporting {len(fx_rates)} currencies")

"""
API Integration for Financial Data
Sample implementation for pulling data from ERP/accounting systems
"""

import requests
import pandas as pd
from datetime import datetime, timedelta

class FinancialAPIClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {api_key}'} if api_key else {}
        
    def fetch_financial_data(self, entity_id, start_date, end_date):
        endpoint = f"{self.base_url}/financial-data"
        params = {
            'entity_id': entity_id,
            'start_date': start_date,
            'end_date': end_date
        }
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            return pd.DataFrame(data.get('results', []))
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return pd.DataFrame()
    
    def fetch_multiple_entities(self, entity_ids, start_date, end_date):
        all_data = []
        for entity_id in entity_ids:
            df = self.fetch_financial_data(entity_id, start_date, end_date)
            if not df.empty:
                df['entity_id'] = entity_id
                all_data.append(df)
        return pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()

if __name__ == "__main__":
    # Template - replace with your actual API details
    # client = FinancialAPIClient(
    #     base_url='https://api.your-erp-system.com',
    #     api_key='your-api-key'
    # )
    print("API Integration module ready")
    print("Replace placeholder values with your actual API configuration")

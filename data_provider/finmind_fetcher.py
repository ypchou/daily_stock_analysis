import requests
import pandas as pd

class FinMindFetcher:
    BASE_URL = "https://api.finmindtrade.com/api/v4/data"

    def __init__(self):
        pass

    def get_stock_data(self, stock_id, start_date, end_date):
        """
        Fetch stock data for a specific stock within a date range.
        
        :param stock_id: Stock ID for which to fetch data.
        :param start_date: Start date for data in 'YYYY-MM-DD' format.
        :param end_date: End date for data in 'YYYY-MM-DD' format.
        :return: DataFrame containing stock data.
        """
        params = {
            'dataset': 'StockPrice',
            'stock_id': stock_id,
            'date': f"{start_date},{end_date}"
        }
        
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'SUCCESS':
                return pd.DataFrame(data['data'])
            else:
                print("Error: ", data['message'])
                return None
        else:
            print("Failed to fetch data: ", response.status_code)
            return None

# Example usage
if __name__ == "__main__":
    fetcher = FinMindFetcher()
    stock_data = fetcher.get_stock_data("2330", "2021-01-01", "2021-12-31")
    print(stock_data)
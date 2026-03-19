import requests
import time

class FinMindFetcher(BaseFetcher):
    def __init__(self):
        super().__init__()
        self.api_url = "https://api.finmind.ai/api/v4/data"

    def fetch_data(self, stock_code, start_date, end_date):
        self.validate_stock_code(stock_code)
        params = {"dataset": "TaiwanStockPrice", "stock_id": stock_code, "start_date": start_date, "end_date": end_date}
        response = self._make_request(params)
        return self.process_response(response)

    def _make_request(self, params):
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            time.sleep(0.5)  # Rate limit
            return response.json()
        except requests.RequestException as e:
            print(f"Error during API request: {e}")
            raise

    def validate_stock_code(self, stock_code):
        if not isinstance(stock_code, str) or len(stock_code) != 4:
            raise ValueError(f"Invalid stock code: {stock_code}. Taiwan stock codes must be 4 characters long.")

    def process_response(self, response):
        if response.get('success'):
            return response['data']  # Assuming 'data' key contains the necessary information
        else:
            raise Exception(f"Failed to fetch data: {response.get('message')}")

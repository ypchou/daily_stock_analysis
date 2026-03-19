import requests

def fetch_taiwan_stock_data(stock_id, start_date, end_date):
    """
    Fetch Taiwan stock data using FinMind API.
    
    Parameters:
        stock_id (str): The stock identifier (e.g., '2330').
        start_date (str): The start date in format 'YYYY-MM-DD'.
        end_date (str): The end date in format 'YYYY-MM-DD'.
    
    Returns:
        dict: A dictionary containing stock data.
    """
    url = 'https://api.finmindtrade.com/api/v4/data'
    params = {
        'dataset': 'TaiwanStockPrice',
        'stock_id': stock_id,
        'start_date': start_date,
        'end_date': end_date
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error fetching data: {response.text}')

if __name__ == '__main__':
    # Example usage
    stock_id = '2330'  # Taiwan Semiconductor Manufacturing Company
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    data = fetch_taiwan_stock_data(stock_id, start_date, end_date)
    print(data)
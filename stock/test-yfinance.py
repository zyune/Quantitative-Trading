import yfinance as yf
# Define the stock symbol and time range
stock_symbol = 'MSFT'
start_date = '2010-01-01'
end_date = '2023-04-12'

# use download function to read the data, read it into a Pandas DataFrame
# msft_data = yf.download(stock_symbol, start=start_date, end=end_date)
help(yf.download)
# Save the data to a CSV file
# msft_data.to_csv('msft_stock_data.csv')

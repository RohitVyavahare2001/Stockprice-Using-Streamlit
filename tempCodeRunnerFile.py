ticker_symbol="AAPL"

ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",start="2020-01-01",end="2023-07-31")

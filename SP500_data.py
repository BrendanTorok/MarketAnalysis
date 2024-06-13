import pandas as pd
import yfinance as yf

sp500url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
data_table = pd.read_html(sp500url)
tickers = data_table[0]['Symbol'].tolist()

for i in range(len(tickers)):
    if tickers[i] == 'BRK.B':
        tickers[i] = 'BRK-B'
    elif tickers[i] == 'BF.B':
        tickers[i] = 'BF-B'


# Get key financial information for all stock tickers
def get_company_info(ticker):
    try:
        info = yf.Ticker(ticker).info
        return {
            'Ticker': ticker,
            'CompanyName': info.get('longName', ''),
            'Sector': info.get('sector', ''),
            'Industry': info.get('industry', ''),
            'Employees': info.get('fullTimeEmployees', ''),
            'PreviousClose': info.get('previousClose', ''),
            'FiftyDayAverage': info.get('fiftyDayAverage', ''),
            'TwoHundredDayAverage': info.get('twoHundredDayAverage', ''),
            'DividendRate': info.get('dividendRate', ''),
            'DividendYield': info.get('dividendYield', ''),
            'Beta': info.get('beta', ''),
            'ForwardPE': info.get('forwardPE', ''),
            'TrailingPE': info.get('trailingPE', ''),
            'Volume': info.get('volume', ''),
            'AverageVolume': info.get('averageVolume', ''),
            'MarketCap': info.get('marketCap', ''),
            'EnterpriseValue': info.get('enterpriseValue', ''),
            'ProfitMargin': info.get('profitMargins', ''),
            'FloatShares': info.get('floatShares', ''),
            'SharesOutstanding': info.get('sharesOutstanding', ''),
            'SharesShort': info.get('sharesShort', ''),
            'BookValue': info.get('bookValue', ''),
            'TotalCash': info.get('totalCash', ''),
            'EBITDA': info.get('ebitda', ''),
            'TotalDebt': info.get('totalDebt', ''),
            'TotalRevenue': info.get('totalRevenue', ''),
            'RevenuePerShare': info.get('revenuePerShare', ''),
            'FreeCashflow': info.get('freeCashflow', ''),
            'RevenueGrowth': info.get('revenueGrowth', ''),
            'GrossMargins': info.get('grossMargins', ''),
            'OperatingMargins': info.get('operatingMargins', '')
        }
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None


# Create dataframe that contains all S&P 500 stocks
sp500_data = []

for ticker in tickers:
    company_info = get_company_info(ticker)
    if company_info:
        sp500_data.append(company_info)

df_sp500_companies = pd.DataFrame(sp500_data)

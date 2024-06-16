import pandas as pd
import yfinance as yf

sp500url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
data_table = pd.read_html(sp500url)
tickers = data_table[0]['Symbol'].tolist()

for i in range(len(tickers)):
    tickers[i] = tickers[i].replace('.', '-')

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
            'DividendRate': info.get('dividendRate', ''),
            'DividendYield': info.get('dividendYield', ''),
            'payoutRatio': info.get('payoutRatio', ''),
            'fiveYearAvgDividendYield': info.get('fiveYearAvgDividendYield', ''),
            'Beta': info.get('beta', ''),
            'TrailingPE': info.get('trailingPE', ''),
            'ForwardPE': info.get('forwardPE', ''),
            'pegRatio': info.get('pegRatio', ''),
            'TrailingEPS': info.get('trailingEps', ''),
            'ForwardEPS': info.get('forwardEps', ''),
            'Volume': info.get('volume', ''),
            'AverageVolume': info.get('averageVolume', ''),
            'MarketCap': info.get('marketCap', ''),
            'fiftyTwoWeekLow': info.get('fiftyTwoWeekLow', ''),
            'fiftyTwoWeekHigh': info.get('fiftyTwoWeekHigh', ''),
            'fiftyDayAverageVolume': info.get('fiftyDayAverage', ''),
            'priceToSalesTrailing12Months': info.get('priceToSalesTrailing12Months', 0),
            'fiftyDayAverage': info.get('fiftyDayAverage', ''),
            'twoHundredDayAverage': info.get('twoHundredDayAverage', ''),
            'EnterpriseValue': info.get('enterpriseValue', ''),
            'EnterpriseToRevenue': info.get('enterpriseToRevenue', ''),
            'EnterpriseToEbitda': info.get('enterpriseToEbitda', ''),
            'ProfitMargin': info.get('profitMargins', ''),
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
            'OperatingMargins': info.get('operatingMargins', ''),
            'currentPrice': info.get('currentPrice', ''),
            'targetHighPrice': info.get('targetHighPrice', ''),
            'targetLowPrice': info.get('targetLowPrice', ''),
            'targetMeanPrice': info.get('targetMeanPrice', ''),
            'targetMedianPrice': info.get('targetMedianPrice', ''),
            'recommendationKey': info.get('recommendationKey', '')
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

df_sp500_companies.to_csv('sp500_company_info.csv', index=False)


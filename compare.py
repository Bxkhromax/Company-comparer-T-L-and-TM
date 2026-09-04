import yfinance as yf

def get_company_data(ticker):
    company = yf.Ticker(ticker)
    info = company.info
    return {
        "name": info.get("longName"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "revenue": info.get("totalRevenue"),
        "employees": info.get("fullTimeEmployees"),
    }

def compare(ticker1, ticker2):
    d1 = get_company_data(ticker1)
    d2 = get_company_data(ticker2)
    
    print(f"{d1['name']} vs {d2['name']}")
    print(f"Stock Price: ${d1['price']} vs ${d2['price']}")
    print(f"Market Cap: ${d1['market_cap']:,} vs ${d2['market_cap']:,}")
    print(f"Revenue: ${d1['revenue']:,} vs ${d2['revenue']:,}")
    print(f"Employees: {d1['employees']:,} vs {d2['employees']:,}")

compare("TSLA", "TM")

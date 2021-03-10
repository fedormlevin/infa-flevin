from fredapi import Fred
fred = Fred(api_key='YOUR API')

def treasury_ten_year():
    """
    Returns: 10-Year Treasury Constant Maturity Rate
    """
    treasury_lt = fred.get_series('DGS10')
    return treasury_lt

def treasury_one_year():
    """
    Returns: 1-Year Treasury Constant Maturity Rate
    """
    treasury_st = fred.get_series('DGS1')
    return treasury_st

def treasury_three_month():
    """
    Returns: 3-Month Treasury Constant Maturity Rate
    """
    treasury_stm = fred.get_series('DGS3MO')
    return treasury_stm

def unemployment_rate_us():
    """
    Return: Unemployment Rate
    """
    unempl = fred.get_series('UNRATE')
    return unempl

def unemployment_rate_by_state(start_date = '2020-01-01'):
    """
    Input: start date of the observations
    Returns: Unemployment Rate by State
    """
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    by_state = []
    for st in states:
        data = fred.get_series(f'{st}UR', observation_start=start_date)
        by_state.append(data)
    df_ur = pd.concat(by_state, axis=1)
    df_ur.columns = states
    return df_ur

def sp_500():
    """
    Returns: S&P 500 for last 10 years, Index
    """
    sp = fred.get_series('SP500')
    return sp

def gdp_us():
    """
    Returns: Real US GDP, Billions of Dollars
    """
    gdp = fred.get_series('GDPC1')
    gdp.dropna(inplace=True)
    return gdp

def inflation_breakeven_10yrs():
    """
    Returns: 10-Year Breakeven Inflation Rate
    Note: forward looking rate (10 years)
    """
    infl = fred.get_series('T10YIE')
    return infl

def inflation_breakeven_5yrs():
    """
    Returns: 5-Year Breakeven Inflation Rate
    Note: forward looking rate (5 years)
    """
    infl = fred.get_series('T5YIE')
    return infl

def consumption():
    """
    Returns: Real Personal Consumption Expenditures, Billions of Dollars
    """
    consmp = fred.get_series('PCEC96')
    consmp.dropna(inplace=True)
    return consmp

def consumer_price_index():
    """
    Returns: Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
    """
    cpi = fred.get_series('CPIAUCSL')
    cpi.dropna(inplace=True)
    return cpi

def recession_nber():
    """
    Returns: NBER based Recession Indicators for the United States from the Period following the Peak through the Trough
    """
    nber = fred.get_series('USREC')
    nber.dropna(inplace=True)
    return nber

def plot_spread_recession():
    """
    Returns: plot of Term Spread (10-year minus 3-month) and NBER recessions from 1981
    """
    ten = treasury_ten_year()
    ten = ten['1981-09-01':]
    thr = treasury_three_month()
    thr = thr['1981-09-01':]
    spr = ten - thr
    rec = recession_nber()
    ax = spr.plot(figsize=(12,6))
    (rec['1981':]*5).plot(ax=ax, style="--", linewidth=3)






